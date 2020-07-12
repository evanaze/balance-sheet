from datetime import datetime
import pandas as pd 

class BalanceSheet:
    def __init__(self):
        self.data = pd.DataFrame()
        self.created_at = datetime.today().date()