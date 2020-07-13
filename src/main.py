"""Updates the balance sheet for the month"""
from datetime import datetime
from . import balanceSheet


class Program:
    def __init__(self):
        self.bs = balanceSheet.BalanceSheet()
        self.month_year = str(datetime.today().date().month) + "/" + str(datetime.today().date().year)

    def add(self):
        "Prompt the user to add new items to the balance sheet"
        done = False
        while not done:
            res = []
            a_o_l = input("Asset or Liability (a/l)? ")
            if a_o_l.lower() == "a":
                res.append("Asset")
            elif a_o_l.lower() == "l":
                res.append("Liability")
            else:
                print("Error: invalid input")
                continue
            name = input("Item name: ")
            res.append(name)
            val = input("Value: ")
            try:
                res.append(int(val))
            except ValueError:
                print("Error: invalid input")
                continue
            desc = input("Description (optional): ")
            res.append(desc)
            self.bs.insert(res)
            cont = input("Continue (y/n)? ")
            if cont.lower() == "n":
                done = True
            elif cont.lower() != "y":
                print("Error: invalid input")
                continue
    def modify(self):
        "Modifies entries in the current balance sheet"
        return 0
    
    def delete(self):
        "Deletes entries in the balance sheet"
        return 0

    def new(self):
        "Create a new balance sheet"
        self.add()
        print(f"Your current balance sheet for {self.month_year}")
        self.bs.display()

    def check_for_update(self):
        "Check if we need to make a new balance sheet for the month"
        return 0

    def check_init(self):
        "Checks if we have a previous balance sheet to carry through or edit"
        self.bs.get_date()
        if not self.bs.last_date:
            print("Setting first balance sheet")
            self.bs.insert_date(self.month_year)
            self.new()

    def run(self):
        "Guides through the balance sheet workflow"
        # check if we have a current balance sheet
        self.check_init()
        # read the saved balance sheet
        self.bs.read()
        if len(self.bs) == 0:
            print("Creating first Balance Sheet")
            self.new()
        print(f"\nBalance sheet for {self.month_year}:\n")
        self.bs.display()
        edit = input(f"\nEdit your current balance sheet for {self.month_year}? (y/n) ")
        if edit.lower() == 'y':
            print(f"Editing your balance sheet for {self.month_year}")
            next = input("add, modify, or delete? ")
            if next == "add":
                self.add()
            elif next == "modify":
                self.modify()
        else:
            print("Done!")


if __name__ == "__main__":
    Program().run()