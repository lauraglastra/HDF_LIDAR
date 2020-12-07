# HDF_LIDAR
======
This repository has been created for processing LIDAR data from NASA's CALIPSO satellite. LIDAR data from CALIPSO is stored in HDF format.

I recommend creating a virtual environment to work with HDF_LIDAR in. Oftentimes the matplotlib toolkit 'basemap' will be difficult to install or fail to install otherwise.

To create a virtual environment, do the following:

# Python 3
conda create --name hdflidar

Requirements
------------

Make sure you have the following programs and libraries installed:

  * [Python](http://www.python.org/) >= 2.6
    including development files
  * [cython](http://cython.org/)
  * [numpy](http://www.numpy.org/)
  * [matplotlib](http://matplotlib.org/)
  * [basemap](http://matplotlib.org/basemap/)
  * [libhdf4](http://www.hdfgroup.org/products/hdf4/)
  * [libhdfeos2](http://hdfeos.org/software/library.php#HDF-EOS2)

