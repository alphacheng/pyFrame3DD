# setup.py
# only if building in place: ``python setup.py build_ext --inplace``

from setuptools import setup
from distutils.core import setup, Extension
# from numpy.distutils.core import setup, Extension
# import numpy


setup(
    name='pyFrame3DD',
    version='1.0.0',
    description='Python bindings to Frame3DD',
    author='S. Andrew Ning',
    author_email='andrew.ning@nrel.gov',
    # packages=['commonse'],
    package_dir={'': 'src'},
    py_modules=['frame3dd'],
    license='Apache License, Version 2.0',
    ext_modules=[Extension('_pyframe3dd', ['src/py_main.c', 'src/py_io.c',
                 'src/frame3dd.c', 'src/HPGmatrix.c', 'src/coordtrans.c',
                 'src/eig.c', 'src/HPGutil.c', 'src/NRutil.c'],
                 # include_dirs=[numpy.get_include()],
                 libraries=['m'])]
)