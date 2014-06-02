import xml.etree.ElementTree as ET
import time
import requests
from datetime import datetime
import calendar
import sys

# tree = ET.parse('Dexcom.xml')

# root = tree.getroot()

# for reading in root.find('GlucoseReadings'):
# 	print 'got another reading'
# 	print reading.get('DisplayTime'), reading.get('Value')
# 	time.sleep(5)
# 	payload = {'value': float(reading.get('Value'))}
# 	requests.post("http://wotkit.sensetecnic.com/api/sensors/mike.blood-sensor/data", auth=('b781be7908b3787b', 'f5bde2beb22a0653'), data=payload)

def sendData(readings):
	'''assumes this is a list of readings with a DisplayTime and Value
	attribute'''
	for reading in readings:
		timestamp_str = reading.get('DisplayTime')
		dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
		timestamp=calendar.timegm(dt.utctimetuple())
		value = float(reading.get('Value'))
		payload = {'timestamp':timestamp*1000, 'value': float(reading.get('Value'))}
		print payload
		# send the data to the wotkit
		r = requests.post("http://wotkit.sensetecnic.com/api/sensors/mike.blood-sensor/data", auth=('b781be7908b3787b', 'f5bde2beb22a0653'), data=payload)
		print r.status_code
		
if __name__ == "__main__":
	filename = sys.argv[1]
	tree = ET.parse(filename)
	root = tree.getroot()
	sendData(root.find('GlucoseReadings'))




