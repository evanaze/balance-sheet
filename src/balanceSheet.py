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
        self.sql_connection()
        self.sql_table()

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
        cursorObj = cursorObj.execute("SELECT date FROM lastupdated ORDER BY table_id LIMIT 1")
        self.last_date = cursorObj.fetchone()
        print("Date:", self.last_date)

    def insert_date(self):
        "inserts the newest date"
        cursorObj = self.con.cursor()
        cursorObj = cursorObj.execute("SELECT MAX(table_id) FROM lastupdated")
        last_table = cursorObj.fetchone()[0]
        self.table_id = last_table + 1
        date = str(datetime.today().date().month) + "/" + str(datetime.today().date().year)
        cursorObj = cursorObj.execute("INSERT INTO lastupdated(table_id, date) VALUES(?, ?)", (self.table_id, date))
        self.con.commit()

    def insert(self, x):
        "inserts an asset or liability"
        cursorObj = self.con.cursor()
        cursorObj.execute('INSERT INTO balancesheet(table_id, type, name, value, description) VALUES(?, ?, ?, ?, ?)', x)
        self.con.commit()

    def display(self):
        "Displays the current state of the balance sheet"
        # assets
        ass = self.data.loc['Asset']
        print(f"\nAssets:\n{ass}")
        tot_ass = ass.Value.sum()
        print(f"Total Assets: {tot_ass}")
        # liabilities
        liab = self.data.loc['Liability']
        print(f"\nLiabilities:\n{liab}")
        tot_liab = liab.Value.sum()
        # net worth
        print(f"Total Liabilities: {tot_liab}")
        print(f"Net worth: {tot_ass - tot_liab}")

    