# Surf Shop Analysis

# Overview

We are looking to open a surf and ice cream shop in Oahu, Hawaii. We are finding the temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

## Process:
Please reference the analysis [here](https://github.com/corispade/Surfs_Up/blob/main/SurfsUp_Challenge.ipynb) for the below deliverables.

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

June and December Summary Statistics: 

![june](https://github.com/corispade/Surfs_Up/blob/main/Resources/june_temps.png) ![december](https://github.com/corispade/Surfs_Up/blob/main/Resources/december_temps.png)


Based on the Summary Statistics charts for the months of June and December, please note the below temperature differences:
* The average temperature is only about 4 degrees higher in June than in December
* The maximum temperature is only 2 degrees higher in June than in December
* The minimum temperature is 8 degrees higher in June than in December

# Summary:

Based on the above summary statistics charts, the temperature remains very steady year-round. This is good news for our business plan, but we should not be using temperature data as our only measurement for the success of this surf and ice cream shop. There are many other factors that determine the success of our shop. For example, the shop location will be determined based on weather data, beach popularity, and cost of real estate. 

1. Weather Data: We need to look further into the data regarding the chance of precipitation and the chance of storms. When is the storm season and how will it affect our sales? We need to analyze this data so that we can offset the losses during the storm season with the gains during the busy season.

2. Beach Popularity: We need to find data on which beaches are the most popular and analyze where is the best location to place our store based on beach popularity. 

3. Cost of Real Estate: The cost of real estate in Hawaii is high. How do we determine the best location so that we are not losing money on overhead? We need to do further queries to analyze the cost of rent to pick the best location. 