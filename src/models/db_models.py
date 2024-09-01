from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    purchases = relationship('MutualFundPurchase', back_populates='user', cascade='all, delete-orphan')


class MutualFundPurchase(Base):
    __tablename__ = 'mutual_fund_purchases'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    fund_name = Column(String, nullable=False)
    units = Column(Integer, nullable=False)

    user = relationship('User', back_populates='purchases')
