#!/usr/bin/python3
"""Filter states by name starting with N"""
import MySQLdb
from sys import argv


def filter_states(usr, pw, db):
    """Filter states by user input
    Args:
        usr: username
        pw: password
        db: database name
    """
    # Open database connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usr,
        passwd=pw,
        db=db,
        charset="utf8"
    )
    # prepare a cursor object using cursor() method
    cur = db.cursor()
    # execute SQL query using execute() method.
    try:
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cur.execute(query)
        # Fetch all the rows in a list of lists.
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        pass
        try:
            print("MySQL Error [{}]: {}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {}".format(e))
    # close the cursor object
    cur.close()
    # close the database connection
    db.close()


def main(*args):
    """Main function"""
    if len(args) == 3:
        filter_states(args[0], args[1], args[2])
        return
    if len(argv) == 4:
        filter_states(argv[1], argv[2], argv[3])
    # else:
        # print("Usage: username password database")


if __name__ == "__main__":
    main()
