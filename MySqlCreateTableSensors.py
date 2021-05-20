#-------------------------------------------------------------------------#
# Create Table
#-------------------------------------------------------------------------#
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="edsonj",						
  password="nvidia",
database="RemoteData"
)
mycursor = mydb.cursor()

'''Sensors Table'''
mycursor.execute("CREATE TABLE Sensors (id INT AUTO_INCREMENT PRIMARY KEY, temperature FLOAT(25), pressure FLOAT(25), depth FLOAT(25), depthw FLOAT(25), surface FLOAT(25), conductivitya FLOAT(25), conductivitys FLOAT(25), resistivity FLOAT(25), salinity FLOAT(25), solidsd FLOAT(25), waterd FLOAT(25), pressureb FLOAT(25), ph FLOAT(25), phmv FLOAT(25), orp FLOAT(25), concetrationo FLOAT(25), saturationo FLOAT(25), pressureo FLOAT(25), voltage FLOAT(25), battery FLOAT(25), time DATETIME NOT NULL)")
mycursor.execute("ALTER TABLE Sensors ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")







