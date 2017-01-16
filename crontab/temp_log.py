#!/usr/bin/env python
import os
import time
import datetime
import glob
from time import strftime
import MySQLdb
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
sensor_temp = '/sys/bus/w1/devices/28-0000084be100//w1_slave'

def readTemp():
    temp_read = open (sensor_temp, 'r')
    lines = temp_read.readlines()
    temp_read.close()

    temp_find = lines[1].find('t=')
    if temp_find != -1:
        temp_strip = lines[1].strip()[temp_find+2:]
        temp_result_cel = float(temp_strip)/1000

    return round(temp_result_cel,2)


temp = readTemp()
print temp
   

# Variables for MySQL
db = MySQLdb.connect(host="localhost", user="root",passwd="masterkey", db="home_temp")
cur = db.cursor()

date_write = time.strftime("%Y-%m-%d")
time_write = time.strftime("%H:%M:%S")
print date_write
print time_write
sql = ("""INSERT INTO show_temp_tempmeasurmentsvalues (temp_value,tepm_measurment_data,temp_measurment_time,room_foreign_key_id)  VALUES (%s,%s,%s,%s)""",(temp,date_write,time_write,'1'))
try:
    print "Writing to database..."
    # Execute the SQL command
    cur.execute(*sql)
    # Commit your changes in the database
    db.commit()
    print "Write Complete"
 
except:
    # Rollback in case there is any error
    db.rollback()
    print db.rollback()
    print "Failed writing to database"
 
cur.close()
db.close()
