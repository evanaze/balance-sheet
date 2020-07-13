"""Updates the balance sheet for the month"""
import os
from . import balanceSheet


def main():
    "guides through the balance sheet workflow"
    # the balance sheet object
    bs = balanceSheet.BalanceSheet()
    bs.read()
    bs.get_date()
    if not bs.last_date:
        print("Setting first balance sheet")
        bs.insert_date()
    else:
        print(bs.last_date)

if __name__ == "__main__":
    main()