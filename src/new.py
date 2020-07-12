"""Updates the balance sheet for the month"""
from . import utils


def main():
    con = utils.sql_connection()
    if con:
        utils.sql_table(con)


if __name__ == "__main__":
    main()