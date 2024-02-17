#!/usr/bin/python3
"""Select states module"""
import MySQLdb


def select_states(usr, pw, db):
    """Select states function
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
        cur.execute("""SELECT * FROM states ORDER BY id ASC""")
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
    if len(args) == 3:
        select_states(args[0], args[1], args[2])
        return
    from sys import argv
    if len(argv) == 4:
        select_states(argv[1], argv[2], argv[3])
    # else:
        # print("Usage: username password database")


if __name__ == "__main__":
    main()
