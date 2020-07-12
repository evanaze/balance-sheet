""" The balance sheet object.

    Backend in SQL, persists in memory with Pandas.
"""
from datetime import datetime
import pandas as pd 
import sqlite3


class BalanceSheet:
    "The balance sheet class"
    def __init__(self, con):
        self.con = con
        self.cursor = con.cursor()
        self.created_at = datetime.today().date()

    def read(self):
        self.data = self.cursor.execute("SELECT * FROM balancesheet")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)  