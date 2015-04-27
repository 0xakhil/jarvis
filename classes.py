
import os
import fnmatch
import json
#from pygame import mixer

class Device(object):
    def __init__(self,name,location):
    	self.location = location
    	self.name = name

    def switchOn(self):
        print self.name + " in " + self.location + " is switched ON"
    def switchOff(self):
        print self.name + " in " + self.location + " is switched OFF"

    def switch(self,state):
    	if state == 'on':
    		self.switchOn()
    	elif state == 'off':
    		self.switchOff()
    	else: print "Error: Unknow device switch state"


class Fan(Device):
	def __init__(self,name,location):
		Device.__init__(self,name,location)


class Light(Device):
	def __init__(self,name,location):
		Device.__init__(self,name,location)


class Room(object):
	def __init__(self,name, deviceTypes = []):
		self.deviceList = {}
		for i in deviceTypes:
			self.deviceList[i] = {}
		
	def addDevice(self,type,name,location):		#Add Error checking if the device name is already there.
		try:
			self.deviceList[type][name] = globals()[type](name,location)
		except Exception, e:
			print e 
			print "Error in addDevice"
			raise

	def removeDevice(self,type,name):
		# try:
			self.deviceList[type].pop(name)
		# except Exception, e:
			# print e

	def getDevice(self,type,name):
		# try:
			return self.deviceList[type][name]
		# except Exception, e:
			# print e 

	def getDeviceList(self):
		return self.deviceList


class Building(object):
	def __init__(self,name,deviceTypes):		#Look for a better way to pass deviceType 
		self.name = name
		self.roomList = {}
		self.deviceTypes = deviceTypes

	def addRoom(self,name):
		try:
			self.roomList[name] = Room(name,self.deviceTypes)
		except Exception, e:
			print e + " : Error in addRoom"

	def removeRoom(self,name):
		try:
			self.roomList.pop[name]
		except Exception, e:
			print e

	def getRoom(self,name):
		try:
			return self.roomList[name]
		except Exception, e:
			print e

	def getRoomList(self):
		return self.roomList
		

class Charactor(object):
	def __init__(self,name,gender):
		self.data = {"name":name,"gender":gender}

	def addData(self,fieldName,value):
		self.data[fieldName] = value

	def removeData(self,fieldName):
		self.data.pop(fieldName)

	def getData(self,fieldName):
		return self.data[fieldName]

	def setData(self,fieldName,value):
		self.data[fieldName] = value


class Music(object):
	def __init__(self,musicDirectory):
		self.songList = {}
		for root, dirnames, filenames in os.walk(musicDirectory):
  			for filename in fnmatch.filter(filenames, '*.mp3'):
  				prettyFilename = filename[:-4]
  				prettyFilename = prettyFilename.lower()
   				self.songList[prettyFilename] = os.path.abspath(filename)

   	def play(self, songName):
   		if songName in self.songList.getkeys():
   			pass


class DataLoader(object):
	def __init__(self,filename,BuildingObject):
		fileptr = open(filename,"r")
		dictdata = json.loads(fileptr.read())
		for room in dictdata['rooms']:
			# print "roomname: " + room['name'] + "\r\n"
			if room['name'] not in BuildingObject.getRoomList().keys():
				BuildingObject.addRoom(room['name'])
			for devicetype in room['devicetypes']:
				# print "devicetype : " + devicetype['type'] + '\r\n'
				for device in devicetype['devices']:
					# print "devicename : " + device['name'] + " ,Device Location : " + device['location'] + "\r\n\r\n"
					BuildingObject.getRoom(room['name']).addDevice(devicetype['type'],device['name'],device['location'])
		fileptr.close()



# class witparser(object):
# 	def __init__




#if __init__ == __main__:












