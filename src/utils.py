"""Code adapted from https://likegeeks.com/python-sqlite3-tutorial/"""
import sqlite3

def sql_connection():
    try:
        con = sqlite3.connect("balancesheet.db")
        print("Connection is established: balancesheet.db")
        return con
    except sqlite3.Error:
        print(sqlite3.Error)

def sql_table(con):
    print(con)
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE balancesheet(id integer PRIMARY KEY, type text, name text, value real, description text)")
    con.commit()
