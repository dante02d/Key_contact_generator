import MySQLdb

dbHost="127.0.0.1"
#dbHost="10.10.100.38"
dbUser="root"
dbPassw =""
dbPassw="root"
dbDb="viperdb"

def connect():
     db1 = MySQLdb.connect(host=dbHost, # your host, usually localhost
                         user=dbUser, # your username
                         passwd=dbPassw, # your password
                         db=dbDb) # name of the data base


     return db1;

def getDataFromAQuerry(sql):
    db1 = connect()
    cur1 = db1.cursor(MySQLdb.cursors.DictCursor)

    # Use all the SQL you like

    cur1.execute(sql)

    # print all the first cell of all the rows

    rows =cur1.fetchall()

    cur1.close()
    db1.close()
    return rows