# -*- coding: utf-8 -*-
import sys
import re
import ttk
import Tkinter as tk
import requests
import os
import requests
import json

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


def plugin_start():
	"""
	Load Template plugin into EDMC
	"""
	this.Range = tk.StringVar(value=config.get("Range"))
	
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
	this.status = tk.Label(parent, anchor=tk.W, text="Ready")
	
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
		

		
# Detect journal events
def journal_entry(cmdr, system, station, entry):

    if entry['event'] == 'FSDJump':
		this.status['text'] = 'Finding nearest neutron star...'	
		print system
		radius = tk.StringVar(value=config.get("Range")).get()		
		url = 'https://www.edsm.net/api-v1/sphere-systems?systemName=1'+system+'&minRadius=0&radius='+radius+'&showPrimaryStar=1&filterPrimaryStar=N'		
		print url
		r = requests.get(url)
		print r.status_code
		
		#print r.json()
		
		input_dict = r.json()
		output_dict = [x for x in input_dict if x['primaryStar'] and x['primaryStar']['type'] == 'Neutron Star' ]
		
		print output_dict
					
		## what if there isnt any?
		for sysrec in output_dict:
			if float(nearest['distance']) >  sysrec['distance']:
				nearest=sysrec
		
		print nearest
		
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


