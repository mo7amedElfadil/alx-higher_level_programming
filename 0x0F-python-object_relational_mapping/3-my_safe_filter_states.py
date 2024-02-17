#!/usr/bin/python3
"""Safe Filter states by user input"""
import MySQLdb


def filter_states(usr, pw, db, name):
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
        # query with the name of the state to filter
        # alternative:
        # query =
        # "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(name)
        query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
        # execute the query passing the name as a parameter
        cur.execute(query, (name, ))
        # Fetch all the rows in a list of lists.
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
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
    if len(args) == 4:
        filter_states(args[0], args[1], args[2], args[3])
        return
    from sys import argv
    if len(argv) == 5:
        filter_states(argv[1], argv[2], argv[3], argv[4])
    # else:
        # print("Usage: username password database state_name")


if __name__ == "__main__":
    main()
