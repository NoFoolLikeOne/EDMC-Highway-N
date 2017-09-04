# -*- coding: utf-8 -*-
import sys
import re
import ttk
import Tkinter as tk
import requests
import os
import requests
import json
from  math import sqrt,pow

from config import applongname, appversion
import myNotebook as nb
from config import config

window=tk.Tk()
window.withdraw()

this = sys.modules[__name__]
this.s = None
this.prep = {}

# Lets capture the plugin name we want the name - "EDMC -"
myPlugin = os.path.basename(os.path.realpath(os.path.dirname(os.path.realpath(__file__)))).split('-')[1]

print os.path.realpath(os.path.dirname(os.path.realpath(__file__)))+'/bubble.json'

with open(os.path.realpath(os.path.dirname(os.path.realpath(__file__)))+'/bubble.json') as bubble_file: 
	nstars = json.load(bubble_file)
	

def edsmGetSystem(system):
	url = 'https://www.edsm.net/api-v1/system?systemName='+system+'&showCoordinates=1'		
	print url
	r = requests.get(url)
	return r.json()
		
			

def getDistance(x1,y1,z1,x2,y2,z2):
	return round(sqrt(pow(float(x2)-float(x1),2)+pow(float(y2)-float(y1),2)+pow(float(z2)-float(z1),2)),2)

def setDistances(x,y,z):
			
	for i, newt in enumerate(nstars):
		nstars[i]["distance"]=getDistance(x,y,z,newt["coords"]["x"],newt["coords"]["y"],newt["coords"]["z"])
		#print newt


def plugin_start():
	"""
	Load Template plugin into EDMC
	"""
	this.Range = tk.StringVar(value=config.get("Range"))
	this.nearest = tk.StringVar(value=config.get("Nearest"))
	this.nextnearest = tk.StringVar(value=config.get("NextNearest"))
	
	print os.path.realpath(os.path.dirname(os.path.realpath(__file__)))
	
	with open(os.path.realpath(os.path.dirname(os.path.realpath(__file__)))+'/nstars.json', 'w') as outfile:  
		json.dump(nstars, outfile)
		
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
	window.clipboard_append(this.status['text'])  # append new value to clipb			
	
def plugin_app(parent):
	label = tk.Label(parent, text= myPlugin + ":")
	
	try:
		nearest = tk.StringVar(value=config.get("Nearest"))
		label_text=nearest['name']
	except:
		label_text="Out of Range"
		
	this.status = tk.Label(parent, anchor=tk.W, text=label_text)
	
	# We should ideally make this conditional
	this.status.bind("<Button-1>", copy_text_to_clipboard)  

	return (label, this.status)

# Log in

# Settings dialog dismissed
def prefs_changed():
	config.set("Range", this.Range.get())
	
	this.status['text'] = "Prefs changed"
	
# def extract_distance(json):
    # try:
        # Also convert to int since update_time will be string.  When comparing
        # strings, "10" is smaller than "2".
        # return int(json['primaryStar']['distance'])
    # except KeyError:
        # return 0
		
def startJumpEvent(system):
	print "StartJump"
	# get the coordinates of the system
	currentSystem=edsmGetSystem(system)
	print "currentSystem"
	print currentSystem
	try:
		setDistances(system["x"],system["y"],system["z"])
		this.jump_distance = getDistance(this.x,this.y,this.z,system["x"],system["y"],system["z"])
		### we need to find the nearest
		print "startJump found system"	
		return True
	except:
		print "startJump not found system"	
		return False
	
def fsdJumpEvent(system):
	print "FSDJump"
	#until getCoords(system)
	#  findNearest(system,coords)
		
def getNearest():
	nearest	= { 'distance': 999999, 'name': "Out of Range" } 
	n=999999
	for sysrec in nstars:
		#print str(n) +  ">"  + str(sysrec['distance'])
		if float(n) >  float(sysrec['distance']):
			try:
				n = float(sysrec['distance'])
				nearest=sysrec
			except:
				print exception
	return nearest
		
# Detect journal events
def journal_entry(cmdr, is_beta, system, station, entry, state):

	print entry['event']
	
	if entry['event'] == 'StartUp':
		
		startSystem = edsmGetSystem(system)
		print startSystem
		setDistances(startSystem["coords"]["x"],startSystem["coords"]["y"],startSystem["coords"]["z"])
		nearest = getNearest()
		print nearest
		if nearest['distance'] == 999999:
			this.status['text'] = nearest['name']
		else:
			this.status['text'] = nearest['name']+' ('+str(nearest['distance'])+'ly)'
	
	if entry['event'] == 'Location':
		print "Location"
		setDistances(entry["StarPos"][0],entry["StarPos"][2],entry["StarPos"][2])
		this.x = entry["StarPos"][0]
		this.y = entry["StarPos"][1]
		this.z = entry["StarPos"][2]

	if entry['event'] == 'StartJump' and entry['JumpType'] == 'Hyperspace':

		this.found = startJumpEvent(system) 
		
	if entry['event'] == 'FSDJump':
	
		if not this.found:
			
		
			this.status['text'] = 'Finding nearest neutron star...'	
			print system
			radius = tk.StringVar(value=config.get("Range")).get()		
			url = 'https://www.edsm.net/api-v1/sphere-systems?systemName='+system+'&minRadius=0&radius='+radius+'&showPrimaryStar=1&filterPrimaryStar=N'		
			print url
			r = requests.get(url)
			print r.status_code
			
			#print r.json()
			
			input_dict = r.json()
			output_dict = [x for x in input_dict if x['primaryStar'] and x['primaryStar']['type'] == 'Neutron Star' ]
			
			print output_dict
			nearest	= { 'distance': 999, 'name': "Out of Range" } 
			nextnearest	= { 'distance': 999, 'name': "Out of Range" } 
			## what if there isnt any?
			for sysrec in output_dict:
				if float(nearest['distance']) >  sysrec['distance']:
					try:
						nextnearest=nearest
						nearest=sysrec
					except:
						print exception
			
			print nearest
			print nextnearest
			
			config.set("Nearest", nearest)
			config.set("NextNearest", nextnearest)
			this.status['text'] = nearest['name']+' ('+str(nearest['distance'])+'ly) '

# Update some data here too
def cmdr_data(data):
	print "Commander Data"
	print data
	# this.status['text'] = "Commander Data"

# Defines location (system)
def setLocation(location):
	print "setLocation"
	print location
	# just clearing the screenshot location
	# this.status['text'] = "setLocation"


