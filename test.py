#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:05:12 2020

@author: lauraglastra

This code is not in full working order. It is a modified version of what 
the HDF-EOS Tools and Information Center has available for plotting
AIRS data. 

https://hdfeos.org/software/pyhdf.php 
https://hdfeos.org/examples/code/pyhdf/AIRS.py
"""

import numpy as np
from pyhdf.SD import SD, SDC
from matplotlib import pyplot as plt
import pprint 
from matplotlib import gridspec
from mpl_toolkits.basemap import Basemap


# Open file.
#FILE_NAME = 'CAL_LID_L2_05kmAPro_Exp-Prov-V3-41.2020-10-01T03-00-00Z.hdf'
FILE_NAME = "CAL_LID_L2_05kmAPro_Exp-Prov-V3-41.2020-10-01T01-30-00Z.hdf"
hdf = SD(FILE_NAME, SDC.READ)

# List available SDS datasets.
print(hdf.datasets())
#pprint prints large libraries with complex structure in a better format than
#just the print command
pprint.pprint(hdf.datasets()) 


# Read dataset. Define DATAFIELD_NAME as only one of the following below.
# To change what you're plotting, uncomment one of the following. 
# DATAFIELD_NAME='Total_Backscatter_Coefficient_532'
# DATAFIELD_NAME='Column_Feature_Fraction'
# DATAFIELD_NAME='Temperature'
# DATAFIELD_NAME='Pressure'
DATAFIELD_NAME='Backscatter_Coefficient_Uncertainty_1064'
data2D = hdf.select(DATAFIELD_NAME)
data = data2D[:,:] 

# Read geolocation dataset.
lat = hdf.select('Latitude')
latitude = lat[:,:]
lon = hdf.select('Longitude')
longitude = lon[:,:]

m = Basemap(projection='cyl', resolution='l',
            llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90, 91, 45))

m.drawmeridians(np.arange(-180, 180, 45), labels=[True,False,False,True])
m.scatter(longitude, latitude, cmap=plt.cm.jet,edgecolors=None, linewidth=0)
x, y = m(longitude, latitude)
# m.pcolormesh(x, y, data)
# m.pcolormesh(longitude, latitude, data,  shading='gouraud')


plt.title('{0}\n {1}'.format(FILE_NAME, DATAFIELD_NAME))
cb = m.colorbar()
cb.set_label('Unit:%')

plt.imshow(data)

plt.show()