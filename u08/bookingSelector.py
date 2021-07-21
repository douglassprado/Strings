import mysql.connector
import sys

# connects to the database and fetching the data from the table
def getDataFromDatabase():
    try:
        conn = mysql.connector.connect(
            user="airlineXreader",
            password="***pleaseREPLACE***",
            host="wi-winf.htwsaar.de",
            port=13307,
            database="airlineX"
        )
    except mysql.connector.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()
    conn.autocommit = True
    cur.execute("SELECT * FROM flightbookings ORDER BY price DESC")

    # convert the result to a list of tuples
    rows = list(cur)

    # generate an empty list
    resultList = []
    for row in rows:
        resultList.append(list(row))

    #close the db connection
    cur.close()
    conn.close()

    return resultList

# filters the given list
# returns a list with "Economy class" bookings only
def filterEconomyClass(bookingList):
    newList = filter(lambda x: [row for row in bookingList if x[5] == 'Y'], bookingList)
    return list(newList)

bookingList = getDataFromDatabase()
print('Now printing the initial list:')
print(bookingList)

# this is just an example, how to filter the initial booking list
economyList = bookingList.copy()
economyList = filterEconomyClass(economyList)
print('Now printing filtered list:')
print(economyList)

# your program starts here

# end of the program
print("**End of the program**")
