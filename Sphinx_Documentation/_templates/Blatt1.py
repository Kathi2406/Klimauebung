# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import iris
import iris.quickplot as qplt
import matplotlib.pyplot as plt


filename ='C:\\Users\\Besitzer\\iris-test-data\\test_data\\NetCDF\\lambert_conformal\\test_lcc.nc'
var1 = iris.load_cube(filename)

print(var1)

var_1=var1[:,10,10]
plt.figure()
qplt.plot(var_1)

var_m=var1.collapsed('time', iris.analysis.MEAN)
print(var_m)
        
plt.figure()
qplt.contourf(var_m,20)

