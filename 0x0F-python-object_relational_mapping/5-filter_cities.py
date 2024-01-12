#!/usr/bin/python3
"""A script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def main():
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities INNER JOIN states ON
                states.id=cities.state_id WHERE states.name=%s""",
                (sys.argv[4],))
    query_rows = cur.fetchall()
    cities = [row[0] for row in query_rows]
    print(*cities, sep=", ")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
