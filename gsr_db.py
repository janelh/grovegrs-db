import serial
import time
import pymysql
import datetime
import json

# Open json config file
with open('config.json', 'r') as f:
    config = json.load(f)

# SQL server settings
host = config['db']['host']
user = config['db']['user']
password = config['db']['password']
dbName = config['db']['dbName']
 
# Initialize serial port
ser = serial.Serial('/dev/ttyACM0')
ser.flushInput()

# Connect to database
connection = pymysql.connect(host=host, user=user, password=password, db=dbName, autocommit=True)

while True:
    try:
        # Get serial input
        ser_bytes = ser.readline()
        try:
            # Decode serial input
            gsr_value = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            # Get average of 10 input values
            gsr_sum = 0
            loop_count = 0
            while (loop_count < 10):
                gsr_sum += gsr_value
                loop_count = loop_count + 1
                # Wait for 5 milliseconds
                time.sleep(.005)
            gsr_average = gsr_sum/10;
            # Setup sql query
            sql = "INSERT INTO `reading` (`ohms`, `date`) VALUES (%s, NOW())"
            # Save gsr average and time to db
            with connection.cursor() as cursor:   
                cursor.execute(sql, (gsr_average))
        except:
            continue
    except:
        cursor.close()
        connection.close()
        print("Keyboard Interrupt")
        break


