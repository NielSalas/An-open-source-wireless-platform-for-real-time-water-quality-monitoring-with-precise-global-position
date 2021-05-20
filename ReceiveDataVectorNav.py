"""
Manage Vector Nav data and Insert it into a MySql Database
-------------------------
These are the device management libraries and drivers. They should be
used for reading and managing the data structure in the context of inserting data into the Mysql database.
"""
import time
import serial   
import mysql.connector                                    
from datetime import datetime
import time
import keyboard
import math

#-------------------------------------------------------------------------#
# ModbusSerialClient Configurations From VectorNav
#-------------------------------------------------------------------------#
ser=serial.Serial(
port='/dev/ttyUSB0',
baudrate=115200,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)


#-------------------------------------------------------------------------#
# Connecting Database MySql
#-------------------------------------------------------------------------#
mydb = mysql.connector.connect(
  host="localhost",
  user="edsonj",
  password="nvidia",
  database="RemoteData"
)
mycursor = mydb.cursor()


#-------------------------------------------------------------------------#
# Reading Data
#-------------------------------------------------------------------------#
'''Start the loop to read all the records and insert them into the database indefinitely'''
t=0
while True:
    '''Read all data from VectorNav'''
    for i in range(1,16):
        ReadVectorNav=str(ser.readline())
    i=i+1

    ''' The received data is 
	data         type     unit   example
	----------------------------------------
	Yaw  	     float    deg    -019.362
	Pitch 	     float    deg    -000.006
	Roll 	     float    deg    -001.111
	Latitude     double   deg      +1942782.44944704
	Longitude    double   deg      -5804085.43324242
	Altitude     double   m      -1796897.165
	VelocityX    float    m/s    +000.042
	VelocityY    float    m/s    -000.095
	VelocityZ    float    m/s    -000.011
	AccelX       float    m/s    +00.027
	AccelY	     float    m/s^2  +00.174
	AccelZ	     float    m/s^2  -09.788
	AngularRateX float    rad/s  +00.001376
	AngularRateY float    rad/s  +00.000056
	AngularRateZ float    rad/s  +00.001192

	example:
	b'$VNISL,+055.379,+000.179,-002.805,-16.46550171,-071.49327846,+02484.419,+001.802,-000.775,-000.001,+00.053,+00.097,-09.725,+00.001451,+00.007649,+00.005773*6C\r\n'''

    '''Separate data to manage according to the type of data we read'''
    SplitData=ReadVectorNav.split(",",16)

    #-------------------------------------------------------------------------#
    # Managing Data from Reading
    #-------------------------------------------------------------------------#
    '''Convert each data to float type'''
    v1=float(SplitData[1])
    v2=float(SplitData[2])
    v3=float(SplitData[3])
    v4=float(SplitData[4])
    v5=float(SplitData[5])
    v6=float(SplitData[6])
    v7ned=float(SplitData[7])
    v8ned=float(SplitData[8])
    v9ned=float(SplitData[9])
    v10=float(SplitData[10])
    v11=float(SplitData[11])
    v12=float(SplitData[12])
    v13=float(SplitData[13])
    v14=float(SplitData[14])
    v15=float(SplitData[15][:10])
    '''Calculation of velocity with respect to the body v7, v8, v9'''
    v1r=math.radians(v1)
    v2r=math.radians(v2)
    v3r=math.radians(v3)  
    a=(math.cos(v3r))*(math.cos(v2r))
    b=(math.sin(v1r))*(math.cos(v2r))   
    c=-math.sin(v2r)
    d=(math.cos(v1r))*(math.sin(v2r))*(math.sin(v1r))-(math.sin(v1r)*(math.cos(v3r)))
    e=(math.cos(v3r))*(math.cos(v1r))+(math.sin(v3r))*(math.sin(v2r))*(math.sin(v1r))
    f=(math.cos(v2r))*(math.sin(v3r))
    g=(math.sin(v1r))*(math.sin(v3r))-(math.cos(v1r))*(math.cos(v3r))*(math.sin(v2r))
    h=(math.cos(v3r))*(math.sin(v2r))*(math.sin(v1r))-(math.cos(v1r))*(math.sin(v3r))
    i=(math.cos(v3r))*(math.cos(v2r))
    '''Velocity with respect to the body v7, v8, v9'''
    v7=a*v7ned+b*v8ned+c*v9ned
    v8=d*v7ned+e*v8ned+f*v9ned
    v9=g*v7ned+h*v8ned+i*v9ned
    
    '''Return the current UTC date and time for each measure'''
    MeasureTime = datetime.utcnow()

    #-------------------------------------------------------------------------#
	# Insert Data Into Database
    #-------------------------------------------------------------------------#
    '''Insert data into database table "Vectors" '''
    sql = "INSERT INTO Vectors (yaw, pitch, roll, latitude, longitude, altitude, velocityx, velocityy, velocityz, accelx, accely, accelz, angularratex, angularratey, angularratez, time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    valv = (v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,MeasureTime)
    mycursor.execute(sql, valv)
    mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)
    '''
    Loop ended when letter "p" is pressed
    '''
    t=t+1   
    if keyboard.is_pressed('p'):
        print('se presionó [p]arar!')
        break
