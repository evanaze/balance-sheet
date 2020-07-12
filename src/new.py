"""Updates the balance sheet for the month"""
import os
from . import balanceSheet


def main():
    "guides through the balance sheet workflow"
    # the balance sheet object
    bs = balanceSheet.BalanceSheet()
    l1 = (1, "Liability", "Student Loan", 7712, "Mohela")
    a1 = (1, "Asset", "Apple Stock", 2800, "7 Apple Stock")
    bs.insert(l1)
    bs.insert(a1)
    bs.read()
    bs.display()

if __name__ == "__main__":
    main()