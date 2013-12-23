# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 20:32:18 2013

@author: litbang
"""

import numpy as np
import pylab
import sys

nmfile= sys.argv[1]
x11 = [672451.44,672486.8,672446.03,672610.65,672447.91] 
y11 = [9225404.24,9225469.66,9225326.29,9225300.04,9225322.13]
x22 = [672695.39,672647.97,672745.6,672574.86,672464.23]
y22 = [9225405.64,9225492.46,9225339.13,9225510.81,9225488.95]

x1 = x11[int(sys.argv[2])-1]
y1 = y11[int(sys.argv[2])-1]
x2 = x22[int(sys.argv[2])-1]
y2 = y22[int(sys.argv[2])-1]
# np.tan(np.radians(np.arctan(0.5)*180/pi))

teta_rad = np.radians(np.arctan((y2-y1)/(x2-x1))*180/np.pi)
#print teta_rad

with open(nmfile,'r') as fid:
    for line in fid:
        dt = line.strip().split()
        dr = float(dt[0])
        dx = dr * np.sin(teta_rad)
        dy = dr * np.cos(teta_rad)
        sx = x1 + dx
        sy = y1 + dy
        print sx,sy,dt[1],dt[2],dt[3]