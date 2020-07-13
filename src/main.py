"""Updates the balance sheet for the month"""
from datetime import datetime
from . import balanceSheet


class Program:
    def __init__(self):
        self.bs = balanceSheet.BalanceSheet()
        self.month_year = str(datetime.today().date().month) + "/" + str(datetime.today().date().year)

    def check_init(self):
        "Checks if we have a previous balance sheet to carry through or edit"
        self.bs.get_date()
        if not self.bs.last_date:
            print("Setting first balance sheet")
            self.bs.insert_date(self.month_year)

    def run(self):
        "Guides through the balance sheet workflow"
        # read the saved balance sheet
        self.bs.read()
        self.check_init()
        if len(self.bs) == 0:
            print("Empty Balance sheet")

if __name__ == "__main__":
    Program().run()