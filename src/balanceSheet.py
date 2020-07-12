""" The balance sheet object.

    Backend in SQL, persists in memory with Pandas.
"""
import os
from datetime import datetime
import pandas as pd 
import sqlite3
from . import utils


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
        cursorObj.execute("SELECT name FROM sqlite_master WHERE type='table'")
        if not cursorObj.fetchone():
            cursorObj.execute("CREATE TABLE IF NOT EXISTS balancesheet(table_id integer, type text, name text, value real, description text)")
            cursorObj.execute("CREATE TABLE IF NOT EXISTS lastupdated(table_id integer PRIMARY KEY, date text)")
        self.con.commit()

    def read(self):
        cursorObj = self.con.cursor()
        cursorObj.execute("SELECT * FROM balancesheet")
        rows = cursorObj.fetchall()
        self.data = pd.DataFrame(rows, columns = ["Table", "Type", "Name", "Value", "Description"])
        print(self.data)

    def insert(self, x):
        cursorObj = self.con.cursor()
        cursorObj.execute('INSERT INTO balancesheet(table_id, type, name, value, description) VALUES(?, ?, ?, ?, ?)', x)
        self.con.commit()