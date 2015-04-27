import json
import logging
import requests

# logging.getLogger("wit").setLevel(logging.WARNING)
# wit_logger = logging.getLogger('wit')
# wit_logger.setLevel(logging.CRITICAL)


class intent(object):
	def __init__(self,buildingObject):
		self.buildingObject = buildingObject

	def device(self,dictEntity,currentLocation):	#Add sanity check. Like if the room from Wit is not available or wrong
		devicetype = ''
		on_off = ''
		room = ''
		everything = ''
		ordinal = ''

		try: devicetype = dictEntity["devicetype"][0]["value"]
		except KeyError:
			pass
#			devicetype = 'Light'					#Default devicetype is Light

		try: on_off = dictEntity["on_off"][0]["value"]
		except KeyError:
			print "Device Intent without on_off Entity"	#Add a custom exception to catch at the highest level

		try: room = dictEntity["room"][0]["value"]
		except KeyError:
			room = currentLocation

		try: everything = dictEntity["everything"][0]["value"]
		except KeyError:
			pass

		try: ordinal = dictEntity["ordinal"][0]["value"]
		except KeyError:
			ordinal = 1

		if room not in self.buildingObject.getRoomList():
				raise KeyError('Room not found')

		if everything == 'all':
			currentRoom = self.buildingObject.getRoom(room)
			if devicetype == '':
				for iDevicetype in currentRoom.getDeviceList().keys():
					for eachDevice in currentRoom.getDeviceList()[iDevicetype]:
						currentRoom.getDevice(iDevicetype, eachDevice).switch(on_off)
			else:
				for eachDevice in currentRoom.getDeviceList()[devicetype]:
					#print devicetype + " " + eachDevice
					currentRoom.getDevice(devicetype, eachDevice).switch(on_off)
					#eachDevice.switch(on_off)
			return

		elif (devicetype != '') and (on_off != ''):
			device = devicetype.lower() + str(ordinal)

			# print 'Room: ' + room + " device type " + devicetype + " on_off " + on_off 
			try:
				roomObj = self.buildingObject.getRoom(room)
				roomObj.getDevice(devicetype,device).switch(on_off)
			except Exception, e:
				print e
				raise
			return

		else: 
			print "Unknown Device Intent State : Everything: " + everything
			print "\r\n devicetype : " + devicetype
			print "\r\n room : " + room
			print "\r\n ordinal : " + ordinal
			print "\r\n on_off : " + on_off + "\r\rn" 



	def jukebox(self,dictEntity):
		pass

	def set_current_location(self,dictEntity):
		pass


class Witai(object):
	def __init__(self,accessToken):
		self.accessToken = accessToken
#		wit.init()

	def textQuery(self,queryText):
		payload = {'q': queryText, 'v':'20141022'}
		header = {'Authorization': 'Bearer ' + self.accessToken}
		response = requests.get("https://api.wit.ai/message",params=payload,headers=header)
		print "\r\n" + response.text + '\r\n\r\n'
		return response.json()


