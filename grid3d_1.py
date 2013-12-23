# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 09:52:05 2013

@author: bayu imbang laksono
"""

#import sys
import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.mlab import griddata
#from scipy.interpolate import griddata
#import scipy.interpolate as interpolate
#from scipy.interpolate import Rbf

def weightall(xin,yin,zin,xref,yref,zref):
    lendata = len(xin)
    wa = 0
    for w in range(0,lendata):
        tmp = np.power((xin[w]-xref),2) + \
                np.power((yin[w]-yref),2) + \
                np.power((zin[w]-zref),2)
        wei1 = 1/ np.power(np.sqrt(tmp),3)
        wa += wei1
    return wa
        
def idw(xin,yin,zin,datain,xout,yout,zout):
    lendata = len(xin)
    i=j=k=0
    dataout = np.zeros((len(xout),len(yout),len(zout)))
    dataout.shape
    for i in range(0,len(xout)):
        for j in range(0,len(yout)):
            for k in range(0,len(zout)):
                ux = 0
                for N in range(0,lendata):
                    uu = 0
                    ui = datain[N]
                    tmp = np.power((xin[N]-xout[i]),2) + \
                            np.power((yin[N]-yout[j]),2) + \
                            np.power((zin[N]-zout[k]),2)
                    wix = 1/np.power(np.sqrt(tmp),3)
                    wixui = wix * ui
                    wjx = weightall(xin,yin,zin,xout[i],yout[j],zout[k])
                    uu = wixui / wjx
                    ux += uu
                dataout[i,j,k] = ux
                print i,j,k,".",
                #k += 1
            #j +=1
        #i += 1
    return dataout
                    
                    
#def ndmesh(*args):
#   args = map(np.asarray,args)
#   return np.broadcast_arrays(*[x[(slice(None),)+(None,)*i] for i, x in #enumerate(args)])
   

data = np.genfromtxt('res1.txt', dtype=[('x',float),('y',float),
                                           ('z',float),('rho',float),('rho1',float)],
                     comments='"', delimiter=' ')

sample_pts = 100
con_levels = 40

x = data['x']
xmin = x.min()
xmax = x.max()
#x = x - xmin
#xmin = x.min()
#xmax = x.max()

y = data['y']
ymin = y.min()
ymax = y.max()
#y = y - ymin
#ymin = y.min()
#ymax = y.max()

z = data['z']
zmin = z.min()
zmax = z.max()
#z = z - zmin
#zmin = z.min()
#zmax = z.max()

da = data['rho']

# DEFINISIKAN RUANG GRID
xgrd_max = xmax + 50
xgrd_min = xmin - 50
ygrd_max = ymax + 50
ygrd_min = ymin - 50
zgrd_max = zmax + 10
zgrd_min = zmin - 10

xgrd = np.arange(xgrd_min,xgrd_max,10)
ygrd = np.arange(ygrd_min,ygrd_max,10)
zgrd = np.arange(zgrd_min,zgrd_max,10)
print len(xgrd),len(ygrd),len(zgrd)
D = idw(x,y,z,da,xgrd,ygrd,zgrd)

#X_irregular, Y_irregular, Z_irregular = (
#    x[:, None, None], y[None, :, None], z[None, None, :])
#    
#xi = np.linspace(xmin,xmax,sample_pts)
#yi = np.linspace(ymin,ymax,sample_pts)
#zi = np.linspace(zmin,zmax,sample_pts)
#xii,yii,zii = ndmesh(xi,yi,zi)
#
#X_uniform, Y_uniform, Z_uniform = (
#    xi[:, None, None], yi[None, :, None], zi[None, None, :])
#    
#X_irregular, Y_irregular, Z_irregular = np.broadcast_arrays(
#    X_irregular, Y_irregular, Z_irregular)

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
#sys.exit(1)
