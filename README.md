# HDF_LIDAR
This repository has been created for processing LIDAR data from NASA's CALIPSO satellite. LIDAR data from CALIPSO is stored in HDF format.

I recommend creating a virtual environment to work with HDF_LIDAR in. Oftentimes the matplotlib toolkit 'basemap' will be difficult to install or fail to install otherwise.

To create a virtual environment, do the following:

    # Python 3
    conda create --name hdflidar

Requirements
------------

Make sure you have the following programs and libraries installed in your virtual environment:

  * [Python](http://www.python.org/) >= 3.8
    including development files
  * [Anaconda](https://www.anaconda.com/products/individual)
    install the 64-bit version for your operating system
  * [numpy](http://www.numpy.org/) conda install numpy
  * [matplotlib](http://matplotlib.org/)  conda install matplotlib
  * [cython](http://cython.org/) conda install cython
  * [basemap](http://matplotlib.org/basemap/)
    conda install -c conda-forge basemap
  * [pyhdf](https://pypi.org/project/pyhdf/)
    conda install -c conda-forge pyhdf
  * [HDF4 Library](https://portal.hdfgroup.org/display/support/Download+HDF4) >= 4.2.15 (Download from site and save to your environment)
  * [pyproj](https://pypi.org/project/pyproj/) conda install pyproj
  * [pytz](https://pypi.org/project/pytz/) conda install pytz
  * [numexpr](https://pypi.org/project/numexpr/2.6.1/) conda install numexpr
  
**Note:** For pyhdf to work, you must also install the HDF4 library listed above.  

