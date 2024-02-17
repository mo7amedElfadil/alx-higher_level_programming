#!/usr/bin/python3
"""Filter cities module"""
import MySQLdb


def select_cities(usr, pw, db, name):
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
        query = """SELECT cities.id, cities.name, states.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE BINARY states.name = %s
        ORDER BY cities.id ASC"""
        cur.execute(query, (name,))
        # Fetch all the rows in a list of lists.
        rows = cur.fetchall()
        for row in rows:
            print(row[1], end=(", ", "\n")[row == rows[-1]])

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
        select_cities(args[0], args[1], args[2], args[3])
        return
    from sys import argv
    if len(argv) == 5:
        select_cities(argv[1], argv[2], argv[3], argv[4])
    # else:
        # print("Usage: username password database")


if __name__ == "__main__":
    main()
