"""
Name: Shashank Reddy Bobbala
Student ID: 22083114
Course: 7PAM2000-0901-2023 - Applied Data Science 1
University: Msc Data Science (SW) with Placement Year
"""

#Importing the fuctions
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#creating the function to 

def barChart(dF1):
    """
    Parameters
    ----------
    dF1 : This parsed argument for the dataframe which is received from main funtion
    bwidth: defines the width of the bar
    positions: defines the position of bar graph that need to be plotted

    Returns
    -------
    This function plots bar graph represents to total number of registered covid cases to the recovered people among selected countries
    """
    plt.figure()
    
    # Set Bar values and positions
    bwidth = 0.40
    positions = np.arange(len(dF1['Country']))  # Corrected variable name and added missing parentheses

    # Plot the Bar graph for total number of cases
    plt.bar(positions - bwidth/2, dF1['Total Cases'], width=bwidth, label='Total Cases', color='blue')
    
    # Plot the bar graph over the above graph which represents total deaths among the total cases
    plt.bar(positions + bwidth/2, dF1['Total Recovered'].tolist(), width=bwidth, label='Total Recovered', color='Green')
    
    # Label the plot for X and Y axes
    plt.xlabel('Countries')
    plt.ylabel('Count')
    plt.title('Bar Graph Overlay for Total number of cases to Total number of deaths')
    plt.xticks(positions, dF1['Country'])
    plt.legend()
    
    # Display the Graph
    plt.show()
    
def pieChar(dF1):
    """
    Parameters
    ----------
    dF1 : This is parsed parmater for the dataframe which is received from the main function
    fig,axs : is used to plot the pie charts in the grid 1x2
    selected: this is variable which retrieves the values of active cases, total deaths, total recovered for various countries
    totalCases: this stores the values of total of registered cases
    
    Returns
    -------
    This function returns the pie chart which plot the pie chart which segregated under various categories of registered covid cases
    """
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))
    
    #select the values and defines its labels
    selected=dF[dF['Country'] == 'Germany'][['Active Cases', 'Total Deaths','Total Recovered']].values.tolist()
    labels=['Active Cases','Total Deaths','Total Recovered']
    totalCases = dF[dF['Country'] == 'Germany'][['Total Cases']].values.tolist()
    
    #Plot the piechart with selected values
    axs[0].pie(selected[0], explode=[0,0.3,0], labels=labels, startangle=140, pctdistance=0.85)
    axs[0].set_title('Germany')
    
    
    #select the values and defines its labels
    selected1=dF[dF['Country'] == 'China'][['Active Cases', 'Total Deaths','Total Recovered']].values.tolist()
    labels=['Active Cases','Total Deaths','Total Recovered']
    totalCases1 = dF[dF['Country'] == 'China'][['Total Cases']].values.tolist()
    
    #Plot the piechart with selected values
    axs[1].pie(selected1[0], explode=[0,0.3,0], labels=labels, startangle=140, pctdistance=0.85)
    axs[1].set_title('China')
    
    #Display the Total cases value which is sum of Active Cases + Recovered + Total Deaths
    plt.legend(['Total Cases (Germany): {}'.format(totalCases1[0]),'Total Cases (China): {}'.format(totalCases[0])])
    #Display the graph
    plt.tight_layout()
    plt.show()


#displaying Line Chart

def lineChart(dF):
    """
    Parameters
    ----------
    dF : This is parsed parmater for the dataframe which is received from the main function
    countries: It is the list of countries
    year: It is list of years
    
    Returns
    -------
    This function returns the line chart which plots the graph based on population growth over years
    
    """
    plt.figure()
    
    countries = ['India','United States','United Kingdom','China']
    year = [2022,2020,2015,2010,2000,1990]
    
    for country in countries:
        value = dF[dF['Country/Territory'] == country][['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population']].values.tolist()
        plt.plot(year,value[0],label=country)
        
    
    plt.legend()
    plt.show()
    
    
# Main Function
# Reading the CSV file using pandas
dF = pd.read_csv("covid_worldwide.csv")

# Filtering data with specified countries
Countries = ['USA','Germany', 'UK', 'China', 'Italy','India']
dF = dF[dF['Country'].isin(Countries)]

dF['Total Cases'] = dF['Total Cases'].str.replace(',', '').astype(int)
dF['Total Recovered'] = dF['Total Recovered'].str.replace(',','').astype(int)
dF['Active Cases'] = dF['Active Cases'].str.replace(',','').astype(int)
dF['Total Deaths'] = dF['Total Deaths'].str.replace(',','').astype(int)

barChart(dF)
pieChar(dF)

df=pd.read_csv("world_population.csv")
df=df[['Country/Territory','2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population']]
lineChart(df)
