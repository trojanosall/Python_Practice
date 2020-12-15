# Write a Python program to locate Python site-packages.
# site-packages is the target directory of manually built python packages. 
# When you build and install python packages from source(using distutils, 
# probably by executing python setup.py install), you will find the installed modules in site-packages by default. 
# site-packages is by default part of the python search path, so modules installed there can be imported easily afterwards


import site

print(site.getsitepackages())
