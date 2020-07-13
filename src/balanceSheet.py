""" The balance sheet object.

    Backend in SQL, persists in memory with Pandas.
"""
import os
from datetime import datetime
import pandas as pd 
import sqlite3


class BalanceSheet:
    "The balance sheet class"
    def __init__(self):
        self.sql_connection()       # opens the connection to the database
        self.sql_table()            # creates the tables if they have not been created
        self.get_date()             # get the date of the last balance sheet
        self.get_table_id()         # get the current table id

    def __len__(self):
        return len(self.data)

    def sql_connection(self):
        try:
            self.con = sqlite3.connect("balancesheet.db")
            print("Connection is established: balancesheet.db")
        except sqlite3.Error:
            print(sqlite3.Error)

    def sql_table(self):
        "makes a new empty balance sheet"
        cursorObj = self.con.cursor()
        cursorObj.execute("CREATE TABLE IF NOT EXISTS balancesheet(table_id integer, type text, name text, value real, description text)")
        cursorObj.execute("CREATE TABLE IF NOT EXISTS lastupdated(table_id integer PRIMARY KEY, date text)")
        self.con.commit()

    def read(self):
        "Reads the current balance sheet"
        cursorObj = self.con.cursor()
        cursorObj.execute("SELECT type, name, value, description FROM balancesheet")
        rows = cursorObj.fetchall()
        self.data = pd.DataFrame(rows, columns = ["Type", "Name", "Value", "Description"])
        self.data = self.data.set_index("Type").sort_index()

    def get_date(self):
        "Gets the most recent balance sheet"
        cursorObj = self.con.cursor()
        cursorObj = cursorObj.execute("SELECT date FROM lastupdated ORDER BY table_id DESC LIMIT 1")
        self.last_date = cursorObj.fetchone()[0]

    def get_table_id(self):
        # get the id number of the new table
        cursorObj = self.con.cursor()
        cursorObj = cursorObj.execute("SELECT MAX(table_id) FROM lastupdated")
        self.table_id = cursorObj.fetchone()[0]

    def insert_date(self, date):
        "inserts the newest date"
        cursorObj = self.con.cursor()
        if self.last_date != date:
            self.table_id += 1
        cursorObj = cursorObj.execute("INSERT INTO lastupdated(table_id, date) VALUES(?, ?)", (self.table_id, date))
        self.con.commit()

    def insert(self, item):
        "inserts an asset or liability"
        cursorObj = self.con.cursor()
        x = [self.table_id] + item
        cursorObj.execute('INSERT INTO balancesheet(table_id, type, name, value, description) VALUES(?, ?, ?, ?, ?)', x)
        self.con.commit()

    def display(self):
        "Displays the current state of the balance sheet"
        # assets
        try:
            ass = self.data.loc['Asset']
            print(f"\nAssets:\n{ass}")
            tot_ass = ass.Value.sum()
            print(f"Total Assets: {tot_ass}")
        except KeyError:
            print("No Assets")
            tot_ass = 0
        # liabilities
        try:
            liab = self.data.loc['Liability']
            print(f"\nLiabilities:\n{liab}")
            tot_liab = liab.Value.sum()
        except KeyError:
            print("No Liabilities")
            tot_liab = 0
        # net worth
        print(f"Total Liabilities: {tot_liab}")
        print(f"Net worth: {tot_ass - tot_liab}")

    