from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.db_models import User, MutualFundPurchase
from utils.common import hash_password, verify_password


class UserDbDao:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_username(self, username: str):
        return self.db.query(User).filter_by(username=username).first()

    def add_user(self, username: str, password: str):
        hashed_password = hash_password(password)
        new_user = User(username=username, password=hashed_password)
        try:
            self.db.add(new_user)
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise ValueError(f"User with username {username} already exists.")

    def delete_user(self, username: str):
        user = self.get_user_by_username(username)
        if user:
            self.db.delete(user)
            self.db.commit()
        else:
            raise ValueError(f"User with username {username} does not exist.")

    def update_user_password(self, username: str, new_password: str):
        user = self.get_user_by_username(username)
        if user:
            user.password = hash_password(new_password)
            self.db.commit()
        else:
            raise ValueError(f"User with username {username} does not exist.")

    def purchase_mutual_fund(self, username: str, fund_name: str, units: int):
        user = self.get_user_by_username(username)
        if not user:
            raise ValueError(f"User with username {username} does not exist.")
        if units <= 0:
            raise ValueError("Number of units must be positive.")

        purchase = next((p for p in user.purchases if p.fund_name == fund_name), None)
        if purchase:
            purchase.units += units
        else:
            new_purchase = MutualFundPurchase(user=user, fund_name=fund_name, units=units)
            self.db.add(new_purchase)

        self.db.commit()

    def show_mutual_funds(self, username: str):
        user = self.get_user_by_username(username)
        if not user:
            raise ValueError(f"User with username {username} does not exist.")
        return {purchase.fund_name: purchase.units for purchase in user.purchases}
