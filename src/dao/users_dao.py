import csv
import os

import bcrypt


class UserDbDao:
    def __init__(self, csv_file='users.csv'):
        self.csv_file = csv_file
        self.conn = self._load_users_from_csv()

    def _load_users_from_csv(self):
        if not os.path.exists(self.csv_file):
            return {"users": {}}

        conn = {"users": {}}
        with open(self.csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = row["id"]
                conn["users"][user_id] = {
                    "id": user_id,
                    "username": row["username"],
                    "password": row["password"],
                    # Initialize purchases to an empty dict if it doesn't exist
                    "purchases": eval(row.get("purchases", "{}")) if row.get("purchases") else {}
                }
        return conn

    def _save_users_to_csv(self):
        with open(self.csv_file, mode='w', newline='') as file:
            fieldnames = ["id", "username", "password", "purchases"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in self.conn["users"].values():
                writer.writerow({
                    "id": user["id"],
                    "username": user["username"],
                    "password": user["password"],
                    "purchases": user.get("purchases", {})  # Ensure purchases field is always included
                })

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify_password(self, plain_password, hashed_password):
        return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

    def get_user_by_username(self, username):
        for user in self.conn["users"].values():
            if user["username"] == username:
                return user
        return None

    def add_user(self, user_id, username, password):
        if user_id in self.conn["users"]:
            raise ValueError(f"User with id {user_id} already exists.")
        hashed_password = self.hash_password(password)
        self.conn["users"][user_id] = {
            "id": user_id,
            "username": username,
            "password": hashed_password,
            "purchases": {}  # Initialize purchases
        }
        self._save_users_to_csv()

    def delete_user(self, user_id):
        if user_id in self.conn["users"]:
            del self.conn["users"][user_id]
            self._save_users_to_csv()
        else:
            raise ValueError(f"User with id {user_id} does not exist.")

    def update_user_password(self, user_id, new_password):
        if user_id in self.conn["users"]:
            hashed_password = self.hash_password(new_password)
            self.conn["users"][user_id]["password"] = hashed_password
            self._save_users_to_csv()
        else:
            raise ValueError(f"User with id {user_id} does not exist.")

    def generate_user_id(self):
        return str(len(self.conn["users"]) + 1)

    def purchase_mutual_fund(self, username, fund_name, units):
        user = next((user for user in self.conn["users"].values() if user["username"] == username), None)
        if not user:
            raise ValueError(f"User with username {username} does not exist.")

        if units <= 0:
            raise ValueError("Number of units must be positive.")

        if "purchases" not in user:
            user["purchases"] = {}

        if fund_name in user["purchases"]:
            user["purchases"][fund_name] += units
        else:
            user["purchases"][fund_name] = units

        self._save_users_to_csv()

    def show_mutual_funds(self, username):
        user = next((user for user in self.conn["users"].values() if user["username"] == username), None)
        if not user:
            raise ValueError(f"User with username {username} does not exist.")

        return user.get('purchases', {})
