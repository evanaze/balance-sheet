"""Code adapted from https://likegeeks.com/python-sqlite3-tutorial/"""
import sqlite3

def sql_connection():
    try:
        con = sqlite3.connect("balancesheet.db")
        print("Connection is established: balancesheet.db")
        return con
    except sqlite3.Error:
        print(sqlite3.Error)

def make_new(con):
    "makes a new empty balance sheet"
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE balancesheet(id integer PRIMARY KEY, type text, name text, value real, description text)")
    con.commit()

def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO balancesheet(id, type, name, value, description) VALUES(?, ?, ?, ?, ?)', entities)
    con.commit()