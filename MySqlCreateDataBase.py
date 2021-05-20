#-------------------------------------------------------------------------#
# Create Database
#-------------------------------------------------------------------------#
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="edsonj",
  password="nvidia"						
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE RemoteData")











