from datetime import datetime
import time
import sqlite3

def adapt_datetime(ts):
    return time.mktime(ts.timetuple())