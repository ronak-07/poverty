
POVERTY
===========

A Python Package to calculate various parameters related to poverty and inequality.

Who is this for?
----------------
For anybody who want to calculate indexes related to poverty and inequality using a python package.

GENERAL USAGE
-------------

### Installation From PyPI package

    pip install poverty

IMPLEMENTED FEATURES
---------------
- [x] Headcount Index
- [x] Poverty Index
- [x] Squared Poverty Index
- [x] Sen Index
- [x] Sen-Shorrocks-Thon Index
- [x] Watts Index
- [x] Gini Coefficient
- [x] Lorenz Curve

		import poverty as pt

		#Base line for poverty
		>>>poverty_line=125

		#List containing expenditure
		>>>expenditure=[100,110,150,160]

		#To calculate Headcount Index
		>>>pt.calc_head(expenditure,poverty_line)

		#To calculate Poverty Index
		>>>pt.pov_index(expenditure,poverty_line)

		#To calculate Squared Poverty Index
		>>>pt.squared_pov_index(expenditure,poverty_line)

		#To calculate Sen Index
		>>>pt.sen_index(expenditure,poverty_line)

		#To calculate Sen-Shorrocks-Thon index
		>>>pt.sst_index(expenditure,poverty_line)

		#To calculate Watts Index
		>>>pt.watts_index(expenditure,poverty_line)

		#To calculate Gini Coefficient
		>>>pt.gini(expenditure)

		#To draw Lorenz Curve
		>>>pt.draw_lorenz(expenditure)

![alt text](https://github.com/ronak-07/poverty/blob/master/Vietnam.PNG)

PERSONAL NOTE
-------------
Feel free to browse the project and give feedback (comments, issues, pull requests).
