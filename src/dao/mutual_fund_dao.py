import csv


class MutualFundDAO:
    def __init__(self, csv_file='mutual_fund_schemes.csv'):
        self.csv_file = csv_file

    def _load_funds(self):
        funds = []
        with open(self.csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                funds.append(row)
        return funds

    def get_fund_family_by_name(self, fund_name):
        """
        Fetch all funds matching the given fund name.

        :param fund_name: Name of the fund to search for.
        :return: List of funds matching the fund name.
        """
        funds = self._load_funds()
        matching_funds = [fund for fund in funds if fund_name.lower() in fund["Mutual_Fund_Family"].lower()]
        return matching_funds

    def get_fund_by_id(self, fund_id):
        """
        Fetch the fund matching the given fund ID.

        :param fund_id: ID of the fund to search for.
        :return: Fund matching the fund ID or None if not found.
        """
        funds = self._load_funds()  # Load all funds
        for fund in funds:
            if fund["Scheme_Code"] == fund_id:
                return fund
        return None


    def get_all_funds(self):
        """
        Fetch all funds from the CSV file.

        :return: List of all funds.
        """
        return self._load_funds()

    def get_all_fund_family_names(self):
        """
        Get the names of all funds from the CSV file.

        :return: List of all fund names.
        """
        funds = self._load_funds()
        fund_names = list({fund['Mutual_Fund_Family'] for fund in funds})
        return fund_names

    def get_mutual_fund_by_name(self, fund_name):
        """
        Fetch all funds matching the given fund name.

        :param fund_name: Name of the fund to search for.
        :return: List of funds matching the fund name.
        """
        funds = self._load_funds()
        matching_funds = [fund for fund in funds if fund_name.lower() in fund["Scheme_Name"].lower()]
        return matching_funds

