from witai import *
from classes import *
from credentials import *	#import Wit.ai's accesstoken from credentials.py

import logging		#To capture the urllib3 ssl warning
logging.captureWarnings(True)

wit = Witai(accessToken)

home = Building('home',['Fan','Light'])
DataLoader('data.json',home)
#time.sleep(3)

while True:
	query = raw_input("\r\nEnter the query: >>  ")
	response = wit.textQuery(query)
	# print response
	dictEntity = response['outcomes'][0]['entities']
	intentobj = intent(home)
	try:
		intentobj.device(dictEntity,'kitchen')
	except KeyError:
		print "Error: Not found"

	del intentobj
