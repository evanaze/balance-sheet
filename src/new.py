"""Updates the balance sheet for the month"""
import os
from . import utils, balanceSheet


def main():
    "guides through the balance sheet workflow"
    con = utils.sql_connection()
    if not "balancesheet.db" in set(os.listdir()):
        if con:
            utils.make_new(con)
        else:
            print("Error in forming connection")
    # the balance sheet object
    bs = balanceSheet.BalanceSheet(con)
    # utils.sql_insert(con, (1, "Liability", "Student Loan", 7712, "Mohela"))
    bs.read()


if __name__ == "__main__":
    main()