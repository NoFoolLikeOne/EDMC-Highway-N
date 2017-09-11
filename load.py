# -*- coding: utf-8 -*-
import sys
import re
import ttk
import Tkinter as tk
import requests
import os
import requests
import json
from  math import sqrt,pow,trunc
import threading
from time import sleep
from urllib import quote_plus

from config import applongname, appversion
import myNotebook as nb
from config import config



window=tk.Tk()
window.withdraw()



this = sys.modules[__name__]
this.s = None
this.prep = {}

this.frame = None
threads=[]
#this.edsm_session = None
#this.edsm_data = None



# Lets capture the plugin name we want the name - "EDMC -"
myPlugin = os.path.basename(os.path.realpath(os.path.dirname(os.path.realpath(__file__)))).split('-')[1]

print os.path.realpath(os.path.dirname(os.path.realpath(__file__)))+'/bubble.json'


	
try:		
	with open(os.path.realpath(os.path.dirname(os.path.realpath(__file__)))+'/userstars.json') as user_file: 
		this.userstars = json.load(user_file)		
except:
	print "No user stars we can create a list later"
	this.userstars = []

with open(os.path.realpath(os.path.dirname(os.path.realpath(__file__)))+'/bubble.json') as bubble_file: 
		bubble = json.load(bubble_file)	


	
def dumpUserStars(x):
	with open(os.path.realpath(os.path.dirname(os.path.realpath(__file__)))+'/userstars.json', 'w') as outfile:  
		 json.dump(x, outfile)	
	print "dumpUserStars"

	

def edsmGetSystem(system):
	url = 'https://www.edsm.net/api-v1/system?systemName='+system+'&showCoordinates=1'		
	print url
	r = requests.get(url)
	s =  r.json()
	print s
	return { "x": s["coords"]["x"], "y": s["coords"]["y"], "z": s["coords"]["z"], "name": s["name"] }
		
			

def getDistance(x1,y1,z1,x2,y2,z2):
	return round(sqrt(pow(float(x2)-float(x1),2)+pow(float(y2)-float(y1),2)+pow(float(z2)-float(z1),2)),2)

# def setDistances(x,y,z):
			
	# for i, newt in enumerate(nstars):
		# nstars[i]["distance"]=getDistance(x,y,z,newt["coords"]["x"],newt["coords"]["y"],newt["coords"]["z"])
		#print newt


def plugin_start():
	"""
	Load Template plugin into EDMC
	"""
	this.Range = tk.StringVar(value=config.get("Range"))
	this.nearest = 'No available'
	this.distance = 999999
	
	#this.userstars=userstars
	
	print os.path.realpath(os.path.dirname(os.path.realpath(__file__)))
	
	
		
	print myPlugin + "Loaded!"
	
	return myPlugin


def plugin_prefs(parent,cmdr,is_beta):  
	frame = nb.Frame(parent)
	frame.columnconfigure(1, weight=1)

	Range_label = nb.Label(frame, text="Range")
	Range_label.grid(padx=10, row=10, sticky=tk.W)

	Range_entry = nb.Entry(frame, textvariable=this.Range)
	Range_entry.grid(padx=10, row=10, column=1, sticky=tk.EW)
	
	#Need to add input validation
	
	#nb.Checkbutton(frame, text="Delete Original File", variable=this.delete_org).grid()
	
	return frame

def copy_text_to_clipboard(event):
	
	window.clipboard_clear()  # clear clipboard contents
	window.clipboard_append(this.nearest)  # append new value to clipb			
	
def plugin_app(parent):
	label = tk.Label(parent, text= myPlugin + ":")
	
	try:
		nearest = tk.StringVar(value=config.get("Nearest"))
		label_text=nearest['name']
	except:
		label_text="Out of Range"
		
	this.status = tk.Label(parent, anchor=tk.W, text=label_text)
	
	this.lastsystem = {}
	this.frame = tk.Frame(parent)
	#this.frame.columnconfigure(3, weight=1)
	this.frame.bind('<<NeutronData>>', edsm_data)
	
	# We should ideally make this conditional
	this.status.bind("<Button-1>", copy_text_to_clipboard)  

	return (label, this.status)

# Log in

# Settings dialog dismissed
def prefs_changed():
	config.set("Range", this.Range.get())
	
	this.status['text'] = "Prefs changed"
	
	
def fsdJumpEvent(system):
	print "FSDJump"
	#until getCoords(system)
	#  findNearest(system,coords)
		
def findNearest(jumpsystem,list):
	nearest	= { 'distance': 999999, 'name': "Out of Range" } 
	n=999999
	for sysrec in list:
		#print str(n) +  ">"  + str(sysrec['distance'])
		d = getDistance(jumpsystem["x"],jumpsystem["y"],jumpsystem["z"],sysrec["x"],sysrec["y"],sysrec["z"])
		if float(n) > float(d):
			try:
				n = d
				nearest=sysrec
			except:
				print exception
	return nearest["name"],n
		
def inBubble(s):
	return getDistance(0,0,0,s["x"],s["y"],s["z"]) <= 800
	#return False
		
def inColonia(s):
	#{"name":"Colonia","coords":{"x":-9530.5,"y":-910.28125,"z":19808.125}}
	return getDistance(-9530.5,-910.28125,19808.125,s["x"],s["y"],s["z"]) <= 200
		
def edsm_worker(system):
	print "in edsm_worker going to sleep"
	
	print this.jumpsystem
	
	## max range is the current nearest star or 200
	
	try:
		range=this.distance 
		if range > 200:
			range = 200
	except:
			range=200
	if range == 0:
		range = 200
	
	print "in worker"
	print this.jumpsystem
	jumpSystem=quote_plus(this.jumpsystem["name"])
	
	url = 'https://www.edsm.net/api-v1/sphere-systems?systemName='+jumpSystem+'&minRadius=0&radius='+str(range)+'&showPrimaryStar=1&filterPrimaryStar=N&showCoordinates=1'
	print url
	r = requests.get(url)
	l = {}
	for elem in this.userstars:
		name=elem["name"]
		x=elem["x"]
		y=elem["y"]
		z=elem["z"]
		l[name]={ "x": x, "y": y,"z": z} 
		
	for elem in bubble:
		name=elem["name"]
		x=elem["x"]
		y=elem["y"]
		z=elem["z"]
		l[name]={ "x": x, "y": y,"z": z} 		
		
	for elem in r.json():
		print elem["name"]
		name=elem["name"]
		x=elem["coords"]["x"]
		y=elem["coords"]["y"]
		z=elem["coords"]["z"]
		l[name]={ "x": x, "y": y,"z": z} 
		
	#n = []
	del this.userstars[:]
	
	for key, value in l.iteritems():
		#n.append({ "name": key, "x": value["x"],"y": value["y"],"z": value["z"]})
		this.userstars.append({ "name": key, "x": value["x"],"y": value["y"],"z": value["z"]})
		
	print "in worker pre find"	
	print this.jumpsystem
	
	this.nearest,this.distance = findNearest(this.jumpsystem,this.userstars)
	
	
	dumpUserStars(this.userstars)
	
	this.frame.event_generate('<<NeutronData>>', when='tail')
	return
		
def edsm_data(event):
	print "Waking up"
	print this.nearest + " " + str(this.distance)
	if this.distance == 999999:
		this.status['text'] = this.nearest
	else:
		this.status['text'] = this.nearest+' ('+str(this.distance)+'ly)'				
		this.status["fg"] = "green"
	return
		
def initThread(jumpSystem):		
	thread = threading.Thread(target = edsm_worker, args = (jumpSystem,))
	##threads.append(thread)
	thread.daemon = True
	thread.start()
		
def setNearest(start,end=None):
	print "setNearest"
	print start
	if not end == None:
		print end
		this.jump = getDistance(start["x"],start["y"],start["z"],end["x"],end["y"],end["z"])
		jumpSystem=end
	else:
		print "No jump"
		this.jump = 0
		jumpSystem=start
		
	if inBubble(jumpSystem):
		print "Near Sol"
		this.nearest,this.distance = findNearest(jumpSystem,bubble)
			
	if inColonia(jumpSystem):
		print "Near Colonia"
		
	if not inBubble(jumpSystem):
		print "Not in bubble or colonia"
		#we will display something right away
		#and then send of a background query to EDSM
		print jumpSystem
		this.nearest,this.distance = findNearest(jumpSystem,this.userstars)
		
		this.jumpsystem=jumpSystem
		print this.jumpsystem
		print "init thread"
		initThread(jumpSystem)
		
	print this.nearest + " " + str(this.distance)
	if this.distance == 999999:
		this.status['text'] = this.nearest
	else:
		this.status['text'] = this.nearest+' ('+str(this.distance)+'ly)'
		
	if not inColonia(jumpSystem) and not inBubble(jumpSystem):
		this.status["fg"] = "grey"
	else: 	
		this.status["fg"] = "green"		
# Detect journal events
def journal_entry(cmdr, is_beta, system, station, entry, state):

	print entry['event']
	
	if entry['event'] == 'StartUp':
		
		#We need the coords of the current system
		#What if EDSM doesn't know? unlikely but could happen
		this.lastsystem = edsmGetSystem(system)	
		setNearest(this.lastsystem)

	
	if entry['event'] == 'Location':
		print "Location"
		print entry
		this.lastsystem = { "x": entry["StarPos"][0], "y": entry["StarPos"][1], "z": entry["StarPos"][2], "name": entry["StarSystem"] }
		setNearest(this.lastsystem)

	if entry['event'] == 'StartJump' and entry['JumpType'] == 'Hyperspace':

		#We can assume that we know the location of the current system
		# but what if we don't
		
		print "StartJump"
		#if the last system was in the bubble then we can wait
		
		try:
			##
			this.jumpsystem = edsmGetSystem(system)	
			this.foundsystem = True
			setNearest(this.lastsystem,this.jumpSystem)
			#we have jumped 
			this.lastsystem = this.jumpSystem
		except:
			print "Failed to find system"
			this.foundsystem = False
		
		
	if entry['event'] == 'FSDJump':
		#We can assume that we know the location of the current system
		# but what if we don't
	
		print "FSDJump"
		print entry
		if this.foundsystem:
			print "Already calculated nearest"
		else:
			this.jumpsystem = { "x": entry["StarPos"][0], "y": entry["StarPos"][1], "z": entry["StarPos"][2], "name": entry["StarSystem"] }
			setNearest(this.lastsystem,this.jumpsystem)
			# we have jumped
			this.lastsystem = this.jumpsystem
			
	
	

# Update some data here too
def cmdr_data(data):
	print "Commander Data"
	this.lastsystem = edsmGetSystem(data['lastSystem']['name'])
	setNearest(this.lastsystem)
	

# Defines location (system)
def setLocation(location):
	print "setLocation"
	print location
	# just clearing the screenshot location
	# this.status['text'] = "setLocation"


