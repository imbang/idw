# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 05:20:45 2013

@author: litbang
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.mlab import griddata
from scipy.interpolate import griddata
import scipy.interpolate as interpolate
from scipy.interpolate import Rbf

def idw(xin,yin,zin,datain,xout,yout,zout,dataout):
    
def ndmesh(*args):
   args = map(np.asarray,args)
   return np.broadcast_arrays(*[x[(slice(None),)+(None,)*i] for i, x in enumerate(args)])
   

data = np.genfromtxt('res1.txt', dtype=[('x',float),('y',float),
                                           ('z',float),('rho',float),('rho1',float)],
                     comments='"', delimiter=' ')

sample_pts = 100
con_levels = 40

x = data['x']
xmin = x.min()
xmax = x.max()
x = x - xmin
xmin = x.min()
xmax = x.max()

y = data['y']
ymin = y.min()
ymax = y.max()
y = y - ymin
ymin = y.min()
ymax = y.max()

z = data['z']
zmin = z.min()
zmax = z.max()
z = z - zmin
zmin = z.min()
zmax = z.max()

da = data['rho']

X_irregular, Y_irregular, Z_irregular = (
    x[:, None, None], y[None, :, None], z[None, None, :])
    
xi = np.linspace(xmin,xmax,sample_pts)
yi = np.linspace(ymin,ymax,sample_pts)
zi = np.linspace(zmin,zmax,sample_pts)
xii,yii,zii = ndmesh(xi,yi,zi)

X_uniform, Y_uniform, Z_uniform = (
    xi[:, None, None], yi[None, :, None], zi[None, None, :])
    
X_irregular, Y_irregular, Z_irregular = np.broadcast_arrays(
    X_irregular, Y_irregular, Z_irregular)

#rbf = Rbf(x,y,z,da,epsilon=2)
#daa = rbf(xii,yii,zii)

#D_interpolated = interpolate.griddata(
#    (X_irregular.ravel(), Y_irregular.ravel(), Z_irregular.ravel()),
#    da.ravel(),
#    (X_uniform, Y_uniform, Z_uniform),
#    method='linear')
    
#print(D_interpolated.shape)
    
#di = griddata(x,(y,z),da,xi[0],(yi,zi))

#print di
#plt.contourf(xi,yi,zi,con_levels,linewidths=1)
#plt.scatter(x,y,c=z,s=20)
#plt.xlim(xmin,xmax)
#plt.ylim(ymin,ymax)
##plt.gca().invert_yaxis()
#plt.show()
sys.exit(1)
