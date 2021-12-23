#PyMySQL can be installed with "python -m pip install pymysql"
import pymysql

#To be filled in with the user ID & password
u=''
p=''

#Open a connection to MySQL server, and store that connection in the variable "db"
db=pymysql.connect(
    host='localhost'
    #,port=3306 #optional
    ,user=u
    ,passwd=p
    ,db='dbtest'
                   )

#Cursor is used to execute SQL code
cursor=db.cursor()
cursor.execute('SELECT VERSION()')

#Storing the result of "SELECT VERSION()" to "data".
#"fetchone()" is used since the SQL code returns only one result
data=cursor.fetchone()

print('Database version is: %s'%data)

#Close the server connection
db.close()
