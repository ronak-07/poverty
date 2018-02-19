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
import matplotlib.pyplot as plt
import numpy as np
import math

def calc_head(expenditure,poverty_line):
    '''
        This function also counts the headcount ratio. 
        The first argument takes a list of income or expenditure of individuals or countries.
        The second argument is an integer value that is poverty line.
    '''
    count=0
    if len(expenditure)==0:
        print("Check data.")
        return
    
    for person in expenditure:
        if person<poverty_line:
            count+=1

    return(count/len(expenditure))
    
def headcount(count_poor_people, total_population):
    '''
        An index that simply measures the proportion of the population that is counted as poor.
    '''
    return (count_poor_people/total_population)

def oecd(adult, children):
    '''
        This is a scale used to calculate numbers of adult equivalents.
        The coefficents have been used in reference of Poverty Manual by World Bank.
    '''
    return(1 + 0.7*(adult-1) + 0.5*children)

def pov_index(expenditure, poverty_line, *args):
    '''
        Poverty gap index: adds up the extent to which individuals on average fall below the poverty line.
        It is expressed as a percentage of the poverty line.
        
        First argument is a list having numerical values of individual's or country's expenditure
        Second argument refers to the minimum income for not being considered as poor.
        
        If just two arguments are passed in pov_index it will calculate the pov_index considering the entire list.
        If *args=0 => entire list will be considered
        If *args=1 => Just the poor population will be considered
    '''
    index=0
    count=0
    for country in expenditure:
        if country<poverty_line:
           index+=(poverty_line-country)/poverty_line
           count+=1

    if len(expenditure)!=0 and(len(args)==0 or args[0]==0 ):
        return(index/len(expenditure))
    elif len(expenditure)!=0 and(args[0]==1) and count!=0:
        return(index/count)
    else:
        print("Check Parameters.")
        return

def squared_pov_index(expenditure, poverty_line):
    '''
        This is a weighted sum of poverty gaps, where the weights are the proportionate poverty gaps. 
        Hence, by squaring the poverty gap index, the measure implicitly puts more weight on observations that fall well below the poverty line.
        
        First argument is a list having numerical values of individual's or country's expenditure
        Second argument refers to the minimum income for not being considered as poor.
    '''
    index=0
    for country in expenditure:
        if country<poverty_line:
           index+=(((poverty_line-country)/poverty_line)*((poverty_line-country)/poverty_line))

    if len(expenditure)!=0:
        return(index/len(expenditure))
    else:
        print("Check Expenditure data.")
        return
    
def sen_index(expenditure,poverty_line):
    '''
        Sen (1976) has proposed an index that sought to combine the effects of 
        -the number of poor
        -the depth of their poverty 
        -the distribution of poverty within the group.
        
        First argument is a list having numerical values of individual's or country's expenditure
        Second argument refers to the minimum income for not being considered as poor.
        
        It calculates the gini-coefficient using the first argument
    '''
    gini_coeff= gini(expenditure)
    p0= calc_head(expenditure,poverty_line)
    p1= pov_index(expenditure,poverty_line)
    return(p0*gini_coeff + p1*(1-gini_coeff))


def sst_index(expenditure,poverty_line):
    '''
        The Sen-Shorrocks-Thon index: Modified version of the Sen Index.
        the product of the headcount index, the poverty gap index (applied to the poor only), and a term with the Gini coefficient of the poverty gap ratios (i.e. of the Gn’s) for the whole population.

        First argument is a list having numerical values of individual's or country's expenditure
        Second argument refers to the minimum income for not being considered as poor.
        
        It calculates the gini-coefficient using the first argument
    '''
    gini_coeff= gini(expenditure)
    p0= calc_head(expenditure,poverty_line)
    p1= pov_index(expenditure,poverty_line,1)
    return(p0*p1*(1+gini_coeff))

def watts_index(expenditure,poverty_line):
    '''
        The first distribution-sensitive poverty measure was proposed in 1968 by Watts.
        The Watts index is attractive in that it satisfies all the theoretical properties that one would want in a poverty index, and is increasingly used by researchers in generating such measures as the poverty incidence curve
    '''
    index=0
    for individual in expenditure:
        if individual<poverty_line:
            index+= math.log(poverty_line/individual)
    if len(expenditure)!=0:
        return(index/len(expenditure))
    else:
        print("Check Data.")
        return

def gini(x):
    '''
        The most widely used single measure of inequality is the Gini coefficient. 
        It is based on the Lorenz curve, a cumulative frequency curve that compares the distribution of a specific variable (e.g. income) with the uniform distribution that represents equality.
    
        x represents a list or numpy array represnting the income or expenditure of indivdiuals or country.
    '''
    n = len(x)
    try:
        x_sum = x.sum()
    except AttributeError:
        x = np.asarray(x)
        x_sum = x.sum()
    n_x_sum = n * x_sum
    r_x = (2. * np.arange(1, len(x)+1) * x[np.argsort(x)]).sum()
    return (r_x - n_x_sum - x_sum) / n_x_sum

def draw_lorenz(expenditure):
    '''
        A graph on which the cumulative percentage of a variable is plotted against the cumulative percentage of the corresponding population (ranked in increasing size of share). 
        The extent to which the curve sags below a straight diagonal line indicates the degree of inequality of distribution.
    
        The first argument takes a list of income or expenditure of individuals or countries.
    '''
    if len(expenditure)==0:
        print("Data Error")
        
    y=np.asarray(expenditure)
    cum_expend= 100*(np.cumsum(np.sort(y))/y.sum())
    cum_expend=np.insert(cum_expend,0,0)
    x_axis= list(range(0,len(y)+1))
    cum_population=np.asarray(x_axis)
    cum_population=100*cum_population/len(y)
    plt.axis([0,100,0,100])
    st_line=np.arange(0,101,1)
    plt.plot(cum_population,cum_expend,st_line)
    plt.xlabel('Cumulative % of Population')
    plt.ylabel('Cumulative % of Expenditure')
    plt.title('Lorenz Curve')
    plt.grid(True)
    plt.show()
