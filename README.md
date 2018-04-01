# Grove GSR Sensor to Database

Records galvanic skin responses from a Grove GSR sensor and stores the average values (ohms)
and timestamp to an sql server.

These recordings can be used to measure and plot the subject's stress response.

More information on the Grove GSR sensor: <http://wiki.seeedstudio.com/Grove-GSR_Sensor/>

## Prerequisites

### Hardware 
	* Arduino Uno
	* Grove Base Shield
	* Grove GSR sensor

The arduino was connected to a Raspberry Pi 3 using a serial cable.

### Python Modules
	* serial
	* pymysql

## Getting Started

Update the config.json with your sql server credentials. Setup a database with a table called 'reading', with 'ohms' and 'date' columns. 

## Running

Attach the GSR sensors to the subject's fingers, and run the following command:

	python gsr_db.py

The recorded averaged values and a timestamp will appear in the 'reading' database table.
