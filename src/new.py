"""Updates the balance sheet for the month"""
import os
from . import balanceSheet


def main():
    "guides through the balance sheet workflow"
    # the balance sheet object
    bs = balanceSheet.BalanceSheet()
    bs.read()
    # bs.display()

if __name__ == "__main__":
    main()