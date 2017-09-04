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
	

xstars=[{'primaryStar': {'type': 'Neutron Star',  'name': "PSR J0633+1746",  'isScoopable': False},  'coords': {'x': -212.15625,  'y': 60.59375,  'z': -784.5625},  'name': "PSR J0633+1746"},
{'primaryStar': {'type': 'Neutron Star',  'name': "PSR J0953+0755",  'isScoopable': False},  'coords': {'x': 463.625,  'y': 587.78125,  'z':  -404.34375},  'name': "PSR J0953+0755"},
{'primaryStar': {'type': 'Neutron Star',  'name': "PSR J0659+1414",  'isScoopable': False},  'coords': {'x': 325.28125,  'y': 131.09375,  'z': -842.75},  'name': "PSR J0659+1414"},
{'primaryStar': {'type': 'Neutron Star',  'name': "PSR J0030+0451",  'isScoopable': False},  'coords': {'x': -449.625,  'y': -770.8125,  'z': -192.1875},  'name': "PSR J0030+0451"},
{'primaryStar': {'type': 'Neutron Star',  'name': "PSR J1136+1551",  'isScoopable': False},  'coords': {'x': 357.46875,  'y': 1066.59375,  'z': -190.90625},  'name': "PSR J1136+1551"},
{'primaryStar': {'type': 'Neutron Star',  'name': "Jackson's Lighthouse",  'isScoopable': False},  'coords': {'y': -27,  'x': 157,  'z': -70},  'name': "Jackson's Lighthouse"},
{'primaryStar': {'type': 'Neutron Star',  'name': 'PSR J2144-3933',  'isScoopable': False},  'coords': {'y': 183.3125,  'x': 22.28125,  'z': 64.65625},  'name': 'Lalande 25224'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'PSR J1752-2806',  'isScoopable': False},  'coords': {'y': -6.84375,  'x': -10.96875,  'z': 407.28125},  'name': 'PSR J1752-2806'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'PSR J0437-4715',  'isScoopable': False},  'coords': {'y': 482.15625,  'x': -137.96875,  'z': -84.40625},  'name': 'PSR J0437-4715'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'PSR J2144-3933',  'isScoopable': False},  'coords': {'y': -396.4375,  'x': -16.53125,  'z': 338.5625},  'name': 'PSR J2144-3933'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'PSR J1856-3754 A',  'isScoopable': False},  'coords': {'y': -154.375,  'x': 12.09375,  'z': 498.09375},  'name': 'PSR J1856-3754'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'PSR J1856-3754 A',  'isScoopable': False},  'coords': {'y': -154.375,  'x': 12.09375,  'z': 498.09375},  'name': 'PSR J1856-3754'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefe EN-Q d6-38 A',  'isScoopable': False},  'coords': {'y': -61.40625,  'x': 426.28125,  'z': -427.3125},  'name': 'Synuefe EN-Q d6-38'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Nova Aquila No 3',  'isScoopable': False},  'coords': {'y': 3.3125,  'x': -363.03125,  'z': 548.28125},  'name': 'Nova Aquila No 3'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Swoilz OO-X d2-10',  'isScoopable': False},  'coords': {'y': -39.4375,  'x': 467.96875,  'z': 468.28125},  'name': 'Swoilz OO-X d2-10'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'PSR J0108-1431',  'isScoopable': False},  'coords': {'y': -666.5625,  'x': -98.4375,  'z': -121.25},  'name': 'PSR J0108-1431'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wregoe MC-M d7-20 A',  'isScoopable': False},  'coords': {'y': 55.5625,  'x': 585.90625,  'z': -360.09375},  'name': 'Wregoe MC-M d7-20'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector NN-S d4-16 A',  'isScoopable': False},  'coords': {'y': 152.4375,  'x': -457.15625,  'z': 503.125},  'name': "Joseph's Lighthouse"},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wregoe MC-M d7-13',  'isScoopable': False},  'coords': {'y': 71.0625,  'x': 588.5625,  'z': -373.4375},  'name': 'Wregoe MC-M d7-13'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq UD-T d3-44',  'isScoopable': False},  'coords': {'y': 56.9375,  'x': 430.28125,  'z': 555.9375},  'name': 'Praea Euq UD-T d3-44'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq UD-T d3-74',  'isScoopable': False},  'coords': {'y': 88.5,  'x': 450.90625,  'z': 537.625},  'name': 'Praea Euq UD-T d3-74'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector ZZ-P d5-52 A',  'isScoopable': False},  'coords': {'y': -160.3125,  'x': -416.96875,  'z': 559.25},  'name': 'Col 359 Sector ZZ-P d5-52'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector ZZ-P d5-59 A',  'isScoopable': False},  'coords': {'y': -182.59375,  'x': -427.71875,  'z': 564.15625},  'name': 'Col 359 Sector ZZ-P d5-59'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector ZZ-P d5-13',  'isScoopable': False},  'coords': {'y': -136.4375,  'x': -425.90625,  'z': 596.71875},  'name': 'Col 359 Sector ZZ-P d5-13'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wregoe BV-P d5-4',  'isScoopable': False},  'coords': {'y': 176,  'x': 500.71875,  'z': -524.53125},  'name': 'Wregoe BV-P d5-4'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'HIP 39751 A',  'isScoopable': False},  'coords': {'y': 71.40625,  'x': 659.65625,  'z': -345.5},  'name': 'HIP 39751'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector UT-R d4-41 A',  'isScoopable': False},  'coords': {'y': -115.375,  'x': -530.1875,  'z': 516.5625},  'name': 'Col 359 Sector UT-R d4-41'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'PSR J1045-4509 A',  'isScoopable': False},  'coords': {'y': 159.125,  'x': 719.59375,  'z': 137.9375},  'name': 'PSR J1045-4509'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wregoe NC-M d7-82',  'isScoopable': False},  'coords': {'y': 66.84375,  'x': 665.84375,  'z': -352.03125},  'name': 'Wregoe NC-M d7-82'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefe YV-T d4-30 A',  'isScoopable': False},  'coords': {'y': -114.90625,  'x': 434.71875,  'z': -629.40625},  'name': 'Synuefe YV-T d4-30'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefai EH-S d5-34 A',  'isScoopable': False},  'coords': {'y': -95.71875,  'x': -505.4375,  'z': -577.96875},  'name': 'Synuefai EH-S d5-34'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefai KT-O d7-10 A',  'isScoopable': False},  'coords': {'y': -94.4375,  'x': -678.96875,  'z': -364.40625},  'name': 'Synuefai KT-O d7-10'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefe DC-S d5-11 A',  'isScoopable': False},  'coords': {'y': -136.34375,  'x': 523.75,  'z': -562.15625},  'name': 'Synuefe DC-S d5-11'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq NH-V d2-33',  'isScoopable': False},  'coords': {'y': 251.34375,  'x': 537.09375,  'z': 514.125},  'name': 'Praea Euq NH-V d2-33'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefai MO-O d7-27',  'isScoopable': False},  'coords': {'y': -142.8125,  'x': -682.3125,  'z': -361.09375},  'name': 'Synuefai MO-O d7-27'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Swoilz QO-X d2-93 A',  'isScoopable': False},  'coords': {'y': -71.375,  'x': 622.34375,  'z': 480.15625},  'name': 'Swoilz QO-X d2-93'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Swoilz QO-X d2-51',  'isScoopable': False},  'coords': {'y': -81.15625,  'x': 606.84375,  'z': 499.46875},  'name': 'Swoilz QO-X d2-51'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefai KT-O d7-46 A',  'isScoopable': False},  'coords': {'y': -97.0625,  'x': -670.125,  'z': -418.9375},  'name': 'Synuefai KT-O d7-46'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefe KD-Q d6-27 A',  'isScoopable': False},  'coords': {'y': -257.65625,  'x': 585.25,  'z': -485.5625},  'name': 'Synuefe KD-Q d6-27'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector DG-O d6-17 A',  'isScoopable': False},  'coords': {'y': -171.84375,  'x': -430.65625,  'z': 658.4375},  'name': 'Col 359 Sector DG-O d6-17'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefai FC-S d5-29 A',  'isScoopable': False},  'coords': {'y': -112.21875,  'x': -579.90625,  'z': -552.9375},  'name': 'Synuefai FC-S d5-29'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefe FX-R d5-22 A',  'isScoopable': False},  'coords': {'y': -233.34375,  'x': 574,  'z': -521.375},  'name': 'Synuefe FX-R d5-22'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector CG-O d6-71 A',  'isScoopable': False},  'coords': {'y': -128.25,  'x': -492.09375,  'z': 639.46875},  'name': 'Col 359 Sector CG-O d6-71'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'HIP 31829 A',  'isScoopable': False},  'coords': {'y': 117.09375,  'x': 165.59375,  'z': -798.28125},  'name': 'HIP 31829'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefe VP-N d7-12',  'isScoopable': False},  'coords': {'y': -534.34375,  'x': 526.34375,  'z': -345.28125},  'name': 'Synuefe VP-N d7-12'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wregoe LR-N d6-67 A',  'isScoopable': False},  'coords': {'y': -11.1875,  'x': 690.90625,  'z': -457.65625},  'name': 'Wregoe LR-N d6-67'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wregoe EQ-P d5-16 A',  'isScoopable': False},  'coords': {'y': 78.15625,  'x': 653.71875,  'z': -508},  'name': 'Wregoe EQ-P d5-16'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wregoe QX-L d7-76 A',  'isScoopable': False},  'coords': {'y': 8.8125,  'x': 752.03125,  'z': -364.53125},  'name': 'Wregoe QX-L d7-76'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Swoiwns HW-U d3-17',  'isScoopable': False},  'coords': {'y': -498.1875,  'x': -430.5,  'z': 544.5625},  'name': 'Swoiwns HW-U d3-17'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefai CH-S d5-8 A',  'isScoopable': False},  'coords': {'y': -73.75,  'x': -638.9375,  'z': -569.90625},  'name': 'Synuefai CH-S d5-8'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq CQ-P d5-80',  'isScoopable': False},  'coords': {'y': 128.53125,  'x': 486.78125,  'z': 705.21875},  'name': 'Praea Euq CQ-P d5-80'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Stock 1 Sector LH-V d2-100 A',  'isScoopable': False},  'coords': {'y': 44.25,  'x': -723.0625,  'z': 479.21875},  'name': 'Stock 1 Sector LH-V d2-100'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq TY-R d4-25 A',  'isScoopable': False},  'coords': {'y': 319.5,  'x': 516.40625,  'z': 621.0625},  'name': 'Praea Euq TY-R d4-25'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector BG-O d6-87 A',  'isScoopable': False},  'coords': {'y': -125.4375,  'x': -560.46875,  'z': 652.53125},  'name': 'Col 359 Sector BG-O d6-87'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector ZK-O d6-3',  'isScoopable': False},  'coords': {'y': -80.28125,  'x': -553.8125,  'z': 667.03125},  'name': 'Col 359 Sector ZK-O d6-3'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector NN-T e3-3',  'isScoopable': False},  'coords': {'y': -16.8125,  'x': -399.375,  'z': 774.125},  'name': 'Col 359 Sector NN-T e3-3'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'U Antliae',  'isScoopable': False},  'coords': {'y': 243.0625,  'x': 834.125,  'z': 98.65625},  'name': 'U Antliae'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector CG-O d6-7',  'isScoopable': False},  'coords': {'y': -182.375,  'x': -534.875,  'z': 667.28125},  'name': 'Col 359 Sector CG-O d6-7'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wredguia BQ-O d6-7 A',  'isScoopable': False},  'coords': {'y': 421.21875,  'x': -593.65625,  'z': -491.59375},  'name': 'Wredguia BQ-O d6-7'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefai IT-O d7-3 A',  'isScoopable': False},  'coords': {'y': -32.75,  'x': -795.4375,  'z': -389.28125},  'name': 'Synuefai IT-O d7-3'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq DQ-P d5-20 A',  'isScoopable': False},  'coords': {'y': 103.5,  'x': 505.96875,  'z': 735.65625},  'name': 'Praea Euq DQ-P d5-20'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wredguia XJ-Q d5-11',  'isScoopable': False},  'coords': {'y': 406.0625,  'x': -601.3125,  'z': -533.09375},  'name': 'Wredguia XJ-Q d5-11'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Swoilz AH-S d5-52 A',  'isScoopable': False},  'coords': {'y': -79.9375,  'x': 461,  'z': 773.53125},  'name': 'Swoilz AH-S d5-52'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Stock 1 Sector PN-T d3-12',  'isScoopable': False},  'coords': {'y': -7.9375,  'x': -723.21875,  'z': 543.78125},  'name': 'Stock 1 Sector PN-T d3-12'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq UX-U d2-72',  'isScoopable': False},  'coords': {'y': 130.46875,  'x': 764.125,  'z': 473.78125},  'name': 'Praea Euq UX-U d2-72'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefe UZ-N d7-1',  'isScoopable': False},  'coords': {'y': -377.40625,  'x': 748.03125,  'z': -356.4375},  'name': 'Synuefe UZ-N d7-1'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Vela Pulsar A',  'isScoopable': False},  'coords': {'y': -44.40625,  'x': 905.9375,  'z': -102.40625},  'name': 'Vela Pulsar'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wregoe BK-R d4-10 A',  'isScoopable': False},  'coords': {'y': 70.25,  'x': 696.6875,  'z': -588.96875},  'name': 'Wregoe BK-R d4-10'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Stock 1 Sector PN-T d3-61',  'isScoopable': False},  'coords': {'y': 25.59375,  'x': -736.3125,  'z': 549.78125},  'name': 'Stock 1 Sector PN-T d3-61'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefe YA-U d4-42',  'isScoopable': False},  'coords': {'y': -76.46875,  'x': 640.90625,  'z': -660.5625},  'name': 'Synuefe YA-U d4-42'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Stock 1 Sector LH-V d2-43 A',  'isScoopable': False},  'coords': {'y': 11.8125,  'x': -771.78125,  'z': 511.25},  'name': 'Stock 1 Sector LH-V d2-43'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'HIP 23520 A',  'isScoopable': False},  'coords': {'y': 97.59375,  'x': -347.5625,  'z': -853.40625},  'name': 'HIP 23520'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'HIP 23520 A',  'isScoopable': False},  'coords': {'y': 97.59375,  'x': -347.5625,  'z': -853.40625},  'name': 'HIP 23520'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Aquila Dark Region CQ-Y d77 A',  'isScoopable': False},  'coords': {'y': 6,  'x': -673.9375,  'z': 637.34375},  'name': 'Aquila Dark Region CQ-Y d77'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector HH-M d7-36',  'isScoopable': False},  'coords': {'y': -217.65625,  'x': -547.4375,  'z': 719.40625},  'name': 'Col 359 Sector HH-M d7-36'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Stock 1 Sector PN-T d3-101',  'isScoopable': False},  'coords': {'y': 19.875,  'x': -741.125,  'z': 566.15625},  'name': 'Stock 1 Sector PN-T d3-101'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq YO-R d4-43 A',  'isScoopable': False},  'coords': {'y': 136.0625,  'x': 638.6875,  'z': 668.5},  'name': 'Praea Euq YO-R d4-43'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq EQ-P d5-90',  'isScoopable': False},  'coords': {'y': 63.375,  'x': 627.8125,  'z': 708.78125},  'name': 'Praea Euq EQ-P d5-90'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wregoe NR-N d6-121',  'isScoopable': False},  'coords': {'y': -17.84375,  'x': 851.375,  'z': -426.0625},  'name': 'Wregoe NR-N d6-121'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wregoe NR-N d6-52',  'isScoopable': False},  'coords': {'y': 19.5625,  'x': 822.03125,  'z': -504},  'name': 'Wregoe NR-N d6-52'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Fine Ring Sector EL-Y d35 A',  'isScoopable': False},  'coords': {'y': 10.3125,  'x': 499.25,  'z': 826.15625},  'name': 'Fine Ring Sector EL-Y d35'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq UY-R d4-14 A',  'isScoopable': False},  'coords': {'y': 367.3125,  'x': 603.8125,  'z': 660.03125},  'name': 'Praea Euq UY-R d4-14'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Stock 2 Sector KM-W d1-41 A',  'isScoopable': False},  'coords': {'y': -135.84375,  'x': -701.34375,  'z': -653},  'name': 'Stock 2 Sector KM-W d1-41'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 135 Sector EB-X d1-10',  'isScoopable': False},  'coords': {'y': -108.84375,  'x': 895.5,  'z': -361.15625},  'name': 'Col 135 Sector EB-X d1-10'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefe JS-R d5-9',  'isScoopable': False},  'coords': {'y': -315.75,  'x': 732.1875,  'z': -559.09375},  'name': 'Synuefe JS-R d5-9'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector YA-N d7-39 A',  'isScoopable': False},  'coords': {'y': 107.78125,  'x': -654.46875,  'z': 719.75},  'name': 'Col 359 Sector YA-N d7-39'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Aquila Dark Region CQ-Y d54',  'isScoopable': False},  'coords': {'y': 20.75,  'x': -693.40625,  'z': 693},  'name': 'Aquila Dark Region CQ-Y d54'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefe PY-Q d5-15',  'isScoopable': False},  'coords': {'y': -616.4375,  'x': 553.84375,  'z': -524.21875},  'name': 'Synuefe PY-Q d5-15'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Aquila Dark Region GW-W d1-14',  'isScoopable': False},  'coords': {'y': -19.3125,  'x': -665.28125,  'z': 730.8125},  'name': 'Aquila Dark Region GW-W d1-14'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wredguia SN-T d3-6 A',  'isScoopable': False},  'coords': {'y': 233.375,  'x': -651.15625,  'z': -706.8125},  'name': 'Wredguia SN-T d3-6'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wregoe JR-M d7-6 A',  'isScoopable': False},  'coords': {'y': 365.71875,  'x': 844.96875,  'z': -366.03125},  'name': 'Wregoe JR-M d7-6'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Swoilz AB-U d4-18 A',  'isScoopable': False},  'coords': {'y': -40.03125,  'x': 752.03125,  'z': 662.9375},  'name': 'Swoilz AB-U d4-18'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Swoiwns PS-S d4-13',  'isScoopable': False},  'coords': {'y': -597.1875,  'x': -443.96875,  'z': 675.125},  'name': 'Swoiwns PS-S d4-13'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'B133 Sector DB-X d1-30 A',  'isScoopable': False},  'coords': {'y': -15.71875,  'x': -490.78125,  'z': 881.40625},  'name': 'B133 Sector DB-X d1-30'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'HIP 98674 A',  'isScoopable': False},  'coords': {'y': -6.3125,  'x': -938.0625,  'z': 373.75},  'name': 'HIP 98674'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'HIP 98674 A',  'isScoopable': False},  'coords': {'y': -6.3125,  'x': -938.0625,  'z': 373.75},  'name': 'HIP 98674'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'HIP 98674 A',  'isScoopable': False},  'coords': {'y': -6.3125,  'x': -938.0625,  'z': 373.75},  'name': 'HIP 98674'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefe KS-R d5-2',  'isScoopable': False},  'coords': {'y': -338.4375,  'x': 754.40625,  'z': -581.3125},  'name': 'Synuefe KS-R d5-2'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector TO-I d9-36',  'isScoopable': False},  'coords': {'y': -289.9375,  'x': -455.75,  'z': 859.875},  'name': 'Col 359 Sector TO-I d9-36'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq IH-M d7-33',  'isScoopable': False},  'coords': {'y': 165.3125,  'x': 487.28125,  'z': 876.96875},  'name': 'Praea Euq IH-M d7-33'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq AA-Q d5-9 A',  'isScoopable': False},  'coords': {'y': 229.375,  'x': 636.9375,  'z': 761.28125},  'name': 'Praea Euq AA-Q d5-9'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefai VE-X d2-10 A',  'isScoopable': False},  'coords': {'y': -236,  'x': -601.28125,  'z': -789.0625},  'name': 'Synuefai VE-X d2-10'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefe PY-P d6-9 A',  'isScoopable': False},  'coords': {'y': -301.4375,  'x': 847.03125,  'z': -490.875},  'name': 'Synuefe PY-P d6-9'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector LN-K d8-0',  'isScoopable': False},  'coords': {'y': -255.4375,  'x': -613.5,  'z': 783.6875},  'name': 'Col 359 Sector LN-K d8-0'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Swoilz GX-R d5-67 A',  'isScoopable': False},  'coords': {'y': -241.8125,  'x': 649.875,  'z': 761.21875},  'name': 'Swoilz GX-R d5-67'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq HL-P d5-44 A',  'isScoopable': False},  'coords': {'y': 12.28125,  'x': 730.0625,  'z': 738.375},  'name': 'Praea Euq HL-P d5-44'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'HIP 100582',  'isScoopable': False},  'coords': {'y': 191.25,  'x': -1020.46875,  'z': -32.75},  'name': 'HIP 100582'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Swoiwns SE-X d2-50',  'isScoopable': False},  'coords': {'y': -252.375,  'x': -862.9375,  'z': 522.71875},  'name': 'Swoiwns SE-X d2-50'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'PSR J0630-2834',  'isScoopable': False},  'coords': {'y': -300.8125,  'x': 837.28125,  'z': -544.75},  'name': 'PSR J0630-2834'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 173 Sector XF-W d2-27',  'isScoopable': False},  'coords': {'y': -51.3125,  'x': 950,  'z': -432.1875},  'name': 'Col 173 Sector XF-W d2-27'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector HN-J d9-50',  'isScoopable': False},  'coords': {'y': 68.125,  'x': -592.1875,  'z': 860.65625},  'name': 'Col 359 Sector HN-J d9-50'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector VZ-G d10-45',  'isScoopable': False},  'coords': {'y': -232.5625,  'x': -407.09375,  'z': 942.4375},  'name': 'Col 359 Sector VZ-G d10-45'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector IC-M d7-13 A',  'isScoopable': False},  'coords': {'y': -274.84375,  'x': -659.6875,  'z': 774.15625},  'name': 'Col 359 Sector IC-M d7-13'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq ZD-T d3-54',  'isScoopable': False},  'coords': {'y': 82.125,  'x': 865.75,  'z': 604.09375},  'name': 'Praea Euq ZD-T d3-54'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq AE-T d3-86',  'isScoopable': False},  'coords': {'y': 75.71875,  'x': 896.71875,  'z': 563.40625},  'name': 'Praea Euq AE-T d3-86'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wredguia BQ-P d5-36 A',  'isScoopable': False},  'coords': {'y': 129.03125,  'x': -894.78125,  'z': -564.96875},  'name': 'Wredguia BQ-P d5-36'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq OX-L d7-22 A',  'isScoopable': False},  'coords': {'y': -10.6875,  'x': 648.78125,  'z': 856.4375},  'name': 'Praea Euq OX-L d7-22'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq KH-M d7-44',  'isScoopable': False},  'coords': {'y': 143.84375,  'x': 598.4375,  'z': 885.125},  'name': 'Praea Euq KH-M d7-44'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wregoe GV-P d5-49 A',  'isScoopable': False},  'coords': {'y': 175.5625,  'x': 908.15625,  'z': -560.03125},  'name': 'Wregoe GV-P d5-49'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wredguia ZE-R d4-24',  'isScoopable': False},  'coords': {'y': -12.28125,  'x': -900.4375,  'z': -598.71875},  'name': 'Wredguia ZE-R d4-24'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Dumbbell Sector DL-Y d33 A',  'isScoopable': False},  'coords': {'y': -59.59375,  'x': -967.375,  'z': 485.03125},  'name': 'Dumbbell Sector DL-Y d33'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 135 Sector AV-Y d38',  'isScoopable': False},  'coords': {'y': -120.875,  'x': 966.78125,  'z': -475.90625},  'name': 'Col 135 Sector AV-Y d38'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector QT-I d9-37 A',  'isScoopable': False},  'coords': {'y': -236.03125,  'x': -544.96875,  'z': 910.6875},  'name': 'Col 359 Sector QT-I d9-37'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Praea Euq AE-T d3-65',  'isScoopable': False},  'coords': {'y': 60.59375,  'x': 916.40625,  'z': 582.75},  'name': 'Praea Euq AE-T d3-65'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wredguia GH-M d7-4 A',  'isScoopable': False},  'coords': {'y': 139.90625,  'x': -994.5625,  'z': -419.375},  'name': 'Wredguia GH-M d7-4'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Synuefai QY-Y d1-1 A',  'isScoopable': False},  'coords': {'y': -212.28125,  'x': -665.4375,  'z': -838.5625},  'name': 'Synuefai QY-Y d1-1'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Fine Ring Sector KC-V d2-43',  'isScoopable': False},  'coords': {'y': 70.46875,  'x': 542.78125,  'z': 945.6875},  'name': 'Fine Ring Sector KC-V d2-43'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector ZL-L d8-16',  'isScoopable': False},  'coords': {'y': 167.5625,  'x': -726.28125,  'z': 808.03125},  'name': 'Col 359 Sector ZL-L d8-16'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wregoe EV-Y d4',  'isScoopable': False},  'coords': {'y': 229.9375,  'x': 441.84375,  'z': -982},  'name': 'Wregoe EV-Y d4'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wredguia GQ-X d1-7',  'isScoopable': False},  'coords': {'y': 525.21875,  'x': -473.9375,  'z': -846},  'name': 'Wredguia GQ-X d1-7'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Stock 1 Sector IH-V d2-128',  'isScoopable': False},  'coords': {'y': 44.625,  'x': -989.53125,  'z': 487.59375},  'name': 'Stock 1 Sector IH-V d2-128'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Wredguia CL-P d5-23',  'isScoopable': False},  'coords': {'y': 9.03125,  'x': -963.96875,  'z': -543.375},  'name': 'Wredguia CL-P d5-23'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Swoilz HW-U d3-14',  'isScoopable': False},  'coords': {'y': -500,  'x': 820.875,  'z': 548.46875},  'name': 'Swoilz HW-U d3-14'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector LI-K d8-34 A',  'isScoopable': False},  'coords': {'y': -267.65625,  'x': -721.53125,  'z': 796.9375},  'name': 'Col 359 Sector LI-K d8-34'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Swoilz LT-O d7-35',  'isScoopable': False},  'coords': {'y': -36.71875,  'x': 678.0625,  'z': 881.34375},  'name': 'Swoilz LT-O d7-35'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector XK-F d11-32',  'isScoopable': False},  'coords': {'y': -158.59375,  'x': -447.625,  'z': 1016.78125},  'name': 'Col 359 Sector XK-F d11-32'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector RZ-F d11-21 A',  'isScoopable': False},  'coords': {'y': 75.40625,  'x': -433.3125,  'z': 1038.625},  'name': 'Col 359 Sector RZ-F d11-21'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Swoilz LH-U d3-5 A',  'isScoopable': False},  'coords': {'y': -713.6875,  'x': 656,  'z': 583.78125},  'name': 'Swoilz LH-U d3-5'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Pru Euq FW-V d2-14',  'isScoopable': False},  'coords': {'y': 475.8125,  'x': -929.65625,  'z': 488.0625},  'name': 'Pru Euq FW-V d2-14'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Col 359 Sector TU-F d11-89 A',  'isScoopable': False},  'coords': {'y': 27.40625,  'x': -405.625,  'z': 1083.5625},  'name': 'Col 359 Sector TU-F d11-89'},
{'primaryStar': {'type': 'Neutron Star',  'name': 'Stock 1 Sector KS-T d3-84 A',  'isScoopable': False},  'coords': {'y': 72.5,  'x': -1009.59375,  'z': 568},  'name': 'Stock 1 Sector KS-T d3-84'}]

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
	print StartJump
	# get the coordinates of the system
	currentSystem=edsmGetSystem(system)
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
	print StartJump
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
		this.status['text'] = nearest['name']+' ('+str(nearest['distance'])+'ly) '
	
	if entry['event'] == 'Location':
		print setDistances
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


