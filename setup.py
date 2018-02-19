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
# Use setuptools in preference to distutils
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os

VERSION = '2.3'
DESCRIPTION = "A Python Package to calculate indexes related to poverty and inequality."
LONG_DESCRIPTION = "This is a package that can be used to find following parameters:Headcount Index, Poverty Index, Squared Poverty Index, Sen-Shorrocks-Thon Index, Sen Index, Watts Index, Gini Coefficient, Draw Lorenz Curve"
LICENSE = "MIT"
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Operating System :: OS Independent',
    'Intended Audience :: Education',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5']

URL="https://github.com/ronak-07/poverty"
KEYWORDS=['POVERTY','INEQUALITY','ECONOMICS']


setup(
    name = 'poverty',
    packages=['poverty'],
    version=VERSION,
    description=DESCRIPTION,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    author= 'Ronak Sisodia and Rishi Kumar (Project Coordinator)',
    author_email='ronaksisodia07@gmail.com',
    install_requires=['numpy','matplotlib'],
    url=URL,
    keywords=KEYWORDS
    )
    
