# Surf Shop Analysis

# Overview

We are looking to open a surf and ice cream shop in Oahu, Hawaii. We are finding the temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

## Process:
Please find analysis [here](https://github.com/corispade/Surfs_Up/blob/main/SurfsUp_Challenge.ipynb) to reference for the below deliverables.

### Deliverable 1 - Determine the Summary Statistics for June
* A query is written to retrieve all the June temperatures from the Date column in the Measurement table from the hawaii.sqlite database
* The June temperatures are added to a list
* Create a DataFrame from the list of June temperatures
* Generate summary statistics chart for the June temperatures

### Deliverable 2 - Determine the Summary Statistics for December
* A query is written to retrieve all the December temperatures from the Date column in the Measurement table from the hawaii.sqlite database
* The December temperatures are added to a list
* Create a DataFrame from the list of December temperatures
* Generate summary statistics chart for the December temperatures

## Resources:
Data Source: hawaii.sqlite

Software: Python 3.7.6, Conda 4.10.1

Environment: Jupyter Notebook

Dependencies: Pandas, Numpy, SQLAlchemy

# Results:

There is a bulleted list that addresses the three key differences in weather between June and December

June and December Summary Statistics: 
![june](https://github.com/corispade/Surfs_Up/blob/main/Resources/june_temps.png) ![december](https://github.com/corispade/Surfs_Up/blob/main/Resources/december_temps.png)


Please note the below differences from the above charts:
* 
* 
* 

# Summary:

There is a high-level summary of the results and there are two additional queries to perform to gather more weather data for June and December.

1. View precipitation data. Show graphs.

2. Look at station data for station closest to Oahu location to determine best area in Oahu to plant the shop.