"""
   "Introduction to Poverty Analysis" by World Bank have been used as a reference for the formula.
    Package developed by: Ronak Sisodia
    
    Measures of Poverty:
        1. Headcount Index
        2. Poverty Index
        3. Squared Poverty Index
        4. Sen Index
        5. Sen-Shorrocks-Thon Index
        6. Watts Index
        
    Measures Of Inequality:
        1. Gini Coefficient
		
	To Visualise the Inequality graphically
        1. Lorenz Curve 
"""
from codecs import open  # To use a consistent encoding
from os import path


# Use setuptools in preference to distutils
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup    

here = path.dirname(path.abspath(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst')) as f:
    long_desc = f.read()


VERSION = '7.2'
DESCRIPTION = "A Python Package to calculate indexes related to poverty and inequality."
LICENSE = "MIT"
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Operating System :: OS Independent',
    'Intended Audience :: Education',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6']

URL="https://github.com/ronak-07/poverty"
KEYWORDS=['Poverty','Inequality','Economics','Gini Coefficient','Lorenz Curve']


setup(
    name = 'poverty',
    packages=['poverty'],
    version=VERSION,
    description=DESCRIPTION,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    author= 'Ronak Sisodia',
    author_email='ronaksisodia07@gmail.com',
    install_requires=['numpy','matplotlib'],
    url=URL,
    keywords=KEYWORDS,
    long_description=long_desc 
    )
