from dao.users_dao import UserDbDao
from dao.mutual_fund_dao import MutualFundDAO
from database import get_db


users_dao = UserDbDao(next(get_db()))
mutual_fund_dao = MutualFundDAO()
