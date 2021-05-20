"""
Manage Multiparameter Sonde Registers and Insert them into a MySql Database
-------------------------
These are the device management drivers and libraries. They should be
used for the management of writing and reading of Multiparameter Sonde registers in the context of inserting data in the Mysql database.
"""
from pymodbus.client.sync import ModbusSerialClient	
from ctypes import *	
import mysql.connector	
from datetime import datetime
import time
import keyboard

#-------------------------------------------------------------------------#
# ModbusSerialClient Configurations From Aquatroll600
#-------------------------------------------------------------------------#
client=ModbusSerialClient(  
    method='rtu',   
    port='/dev/ttyUSB1',    
    baudrate=19200, 
    timeout=3,  
    parity='E', 
    stopbits=1, 
    bytesize=8  
)

#-------------------------------------------------------------------------#
# Convert From Hex To A Float Pointer
#-------------------------------------------------------------------------#
def convert(s):
    i=int(s,16)
    cp=pointer(c_int(i))
    fp=cast(cp,POINTER(c_float))
    return fp.contents.value

#-------------------------------------------------------------------------#
# Connecting Database MySql
#-------------------------------------------------------------------------#
mydb=mysql.connector.connect(
    host="localhost",
    user="edsonj",
    password="nvidia",
    database="RemoteData"
)
mycursor=mydb.cursor()

#-------------------------------------------------------------------------#
# Reading Registers
#-------------------------------------------------------------------------#
'''Trying for connect to Modbus Server/Slave'''
if client.connect():
    '''Start the loop to read all the records and insert them into the database indefinitely'''
    t=0
    while True:
        '''
        Reading from a discrete register with the below content, (address, count=1, unit=1) 
        address – The starting address to read from
        count – The number of registers to read
        unit – The slave unit this request is targeting
        '''
        res1=client.read_holding_registers(5450,count=5,unit=1)
        res1=client.read_holding_registers(5450,count=5,unit=1)
        res1=client.read_holding_registers(5450,count=5,unit=1)
        res2=client.read_holding_registers(5457,count=5,unit=1)
        res3=client.read_holding_registers(5464,count=5,unit=1)
        res4=client.read_holding_registers(5471,count=5,unit=1)
        res5=client.read_holding_registers(5478,count=5,unit=1)
        res6=client.read_holding_registers(5506,count=5,unit=1)
        res7=client.read_holding_registers(5513,count=5,unit=1)
        res8=client.read_holding_registers(5520,count=5,unit=1)
        res9=client.read_holding_registers(5527,count=5,unit=1)
        res10=client.read_holding_registers(5534,count=5,unit=1)	
        res11=client.read_holding_registers(5541,count=5,unit=1)
        res12=client.read_holding_registers(5555,count=5,unit=1)
        res13=client.read_holding_registers(5562,count=5,unit=1)
        res14=client.read_holding_registers(5569,count=5,unit=1)
        res15=client.read_holding_registers(5576,count=5,unit=1)
        res16=client.read_holding_registers(5583,count=5,unit=1)
        res17=client.read_holding_registers(5590,count=5,unit=1)
        res18=client.read_holding_registers(5653,count=5,unit=1)
        res19=client.read_holding_registers(5667,count=5,unit=1)
        res20=client.read_holding_registers(5674,count=5,unit=1)
        
        #-------------------------------------------------------------------------#
        # Managing Data from Reading Registers
        #-------------------------------------------------------------------------#
        '''Reading for Temperature Sensor'''
        res1a1=res1.registers[0]
        res1a2=res1.registers[1]
        res1a12=hex((res1a1<<16)|res1a2)[2:]
        res1a12a=convert(res1a12)
        s1=res1a12a
        
        '''Reading for Pressure Sensor'''
        res2a1=res2.registers[0]
        res2a2=res2.registers[1]
        res2a12=hex((res2a1<<16)|res2a2)[2:]
        res2a12a=convert(res2a12)
        s2=res2a12a
        
        '''Reading for Depth Sensor'''
        res3a1=res3.registers[0]
        res3a2=res3.registers[1]
        res3a12=hex((res3a1<<16)|res3a2)[2:]
        res3a12a=convert(res3a12)
        s3=res3a12a
        
        '''Reading for Level, Depth to Water Sensor'''
        res4a1=res4.registers[0]
        res4a2=res4.registers[1]
        res4a12=hex((res4a1<<16)|res4a2)[2:]
        res4a12a=convert(res4a12)
        s4=res4a12a
        
        '''Reading for Level, Surface Elevation Sensor'''
        res5a1=res5.registers[0]
        res5a2=res5.registers[1]
        res5a12=hex((res5a1<<16)|res5a2)[2:]
        res5a12a=convert(res5a12)
        s5=res5a12a
        
        '''Reading for Actual Conductivity Sensor'''
        res6a1=res6.registers[0]
        res6a2=res6.registers[1]
        res6a12=hex((res6a1<<16)|res6a2)[2:]
        res6a12a=convert(res6a12)
        s6=res6a12a
        
        '''Reading for Specific Conductivity Sensor'''
        res7a1=res7.registers[0]
        res7a2=res7.registers[1]
        res7a12=hex((res7a1<<16)|res7a2)[2:]
        res7a12a=convert(res7a12)
        s7=res7a12a
        
        '''Reading for Resistivity Sensor'''
        res8a1=res8.registers[0]
        res8a2=res8.registers[1]
        res8a12=hex((res8a1<<16)|res8a2)[2:]
        res8a12a=convert(res8a12)
        s8=res8a12a
        
        '''Reading for Salinity Sensor'''
        res9a1=res9.registers[0]
        res9a2=res9.registers[1]
        res9a12=hex((res9a1<<16)|res9a2)[2:]
        res9a12a=convert(res9a12)
        s9=res9a12a
        
        '''Reading for Total Dissolved Solids Sensor'''
        res10a1=res10.registers[0]
        res10a2=res10.registers[1]
        res10a12=hex((res10a1<<16)|res10a2)[2:]
        res10a12a=convert(res10a12)
        s10=res10a12a
        
        '''Reading for Density of water Sensor'''
        res11a1=res11.registers[0]
        res11a2=res11.registers[1]
        res11a12=hex((res11a1<<16)|res11a2)[2:]
        res11a12a=convert(res11a12)
        s11=res11a12a
        
        '''Reading for Barometric pressure Sensor'''
        res12a1=res12.registers[0]
        res12a2=res12.registers[1]
        res12a12=hex((res12a1<<16)|res12a2)[2:]
        res12a12a=convert(res12a12)
        s12=res12a12a
        
        '''Reading for pH Sensor'''
        res13a1=res13.registers[0]
        res13a2=res13.registers[1]
        res13a12=hex((res13a1<<16)|res13a2)[2:]
        res13a12a=convert(res13a12)
        s13=res13a12a
        
        '''Reading for pHmV Sensor'''
        res14a1=res14.registers[0]
        res14a2=res14.registers[1]
        res14a12=hex((res14a1<<16)|res14a2)[2:]
        res14a12a=convert(res14a12)
        s14=res14a12a
        
        '''Reading for ORP Sensor'''
        res15a1=res15.registers[0]
        res15a2=res15.registers[1]
        res15a12=hex((res15a1<<16)|res15a2)[2:]
        res15a12a=convert(res15a12)
        s15=res15a12a
        
        '''Reading for Dissolved Oxygen concetration Sensor'''
        res16a1=res16.registers[0]
        res16a2=res16.registers[1]
        res16a12=hex((res16a1<<16)|res16a2)[2:]
        res16a12a=convert(res16a12)
        s16=res16a12a
        
        '''Reading for Dissolved Oxygen %saturation Sensor'''
        res17a1=res17.registers[0]
        res17a2=res17.registers[1]
        res17a12=hex((res17a1<<16)|res17a2)[2:]
        res17a12a=convert(res17a12)
        s17=res17a12a
        
        '''Reading for Oxygen Partial Pressure Sensor'''
        res18a1=res18.registers[0]
        res18a2=res18.registers[1]
        res18a12=hex((res18a1<<16)|res18a2)[2:]
        res18a12a=convert(res18a12)
        s18=str(res18a12a)
        
        '''Reading for External Voltage Sensor'''
        res19a1=res19.registers[0]
        res19a2=res19.registers[1]
        res19a12=hex((res19a1<<16)|res19a2)[2:]
        res19a12a=convert(res19a12)
        s19=str(res19a12a)
        
        '''Reading for Battery Capacity(remaining) Sensor'''
        res20a1=res20.registers[0]
        res20a2=res20.registers[1]
        res20a12=hex((res20a1<<16)|res20a2)[2:]
        res20a12a=convert(res20a12)
        s20=res20a12a
        
        '''Return the current UTC date and time for each measure'''
        MeasureTime=datetime.utcnow()
        
        #-------------------------------------------------------------------------#
        # Insert Data Into Database
        #-------------------------------------------------------------------------#
        '''Insert data into database table "Sensors" '''
        sql="INSERT INTO Sensors (temperature, pressure, depth, depthw, surface, conductivitya, conductivitys, resistivity, salinity, solidsd, waterd, pressureb, ph, phmv, orp, concetrationo, saturationo, pressureo, voltage, battery, time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val=(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,MeasureTime)
        mycursor.execute(sql,val)
        mydb.commit()
        print("1 record inserted, ID:", mycursor.lastrowid)
        '''
        Loop ended when letter "p" is pressed
        '''
        t=t+1
        if keyboard.is_pressed('p'):
            print('se presionó [p]arar!')
            break
    '''Modbus disconnected alert'''    
else:
    print('Cannot connect to the Modbus Server/Slave')
