import pandas as pd
from pandas import DataFrame, Series
from pandas.core.groupby import DataFrameGroupBy

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import seaborn as sns

import numpy as np

import plotly.express as px

"""
HERE'S THE LINK TO THE DATA:
https://data.worldbank.org/country/turkiye 

There should be a download tab for csv there.

Also before you run, make sure you include 'pip install seaborn, plotly, pandas'
at the top of the module so that the imports work properly
"""


# display all rows and columns for a dataframe temporarily
def print_in_full(*args: any) -> None: 
    with pd.option_context(
        "display.max_rows", 
        None, 
        "display.max_columns", 
        None,
        "display.max_colwidth",
        120
    ):
        print(*args)
        
# gives options as to what we can pass for pd.option_context()
# pd.describe_option()

# skip the first 4 rows of the csv since they aren't actual columns of data
# they're just titles and metadata; do this to prevent tokenizing error from pandas
# look at the actual turkey_stats.csv file for more info

# replace the file path with your file path
info: DataFrame = pd.read_csv(
    "./misc/turkey_stats.csv", 
    skiprows=4
).fillna(0) # also fill all the NaN values with a value

# parse the csv file and remove extraneous stuff from it (like the first view columns
# which are redundant and just adds more clutter)
turkey_data: DataFrame = info[(info["Country Name"] == "Turkiye")]
# inPlace=True allows us to mutate the current DataFrame instance directly
# instead of returning a modified copy
columns_to_drop: list[str] = ["Country Name", "Country Code", "Indicator Code"]
turkey_data.drop(
    columns=columns_to_drop, 
    inplace=True
)

# feel free to uncomment this to see all available columns;
# change to whatever values you want
# print_in_full(turkey_data["Indicator Name"])

# the 3 variables below are lists containing select indicator names I want to look
# at and the years I want to observe these values

# ignore the commented out strings
indicators_to_sortby: list[str] = [
    # "Official exchange rate (LCU per US$, period average)",
    "Imports of goods, services and primary income (BoP, current US$)",
    "Exports of goods and services (current US$",
    "GDP (current US$)",
    "Reserves and related items (BoP, current US$)",
    "Gross fixed capital formation (current US$)"
    # "Reserves and related items (BoP, current US$)"
]
target_years: list[str] = [
    "2020",
    "2021",
    "2022",
    "2023",
    "2024",
    "2025"
]
# this essentially means it includes the column "Indicator Name" + all the year
# columns that we want (the * operator unpacks a list)
target_columns: list[str] = [
    "Indicator Name",
    *target_years
]
    
# get our filtered data frame..
turkey_2020_to_2025: DataFrame = (
    # get only these rows with the select indicators
    turkey_data[
        (turkey_data["Indicator Name"].isin(indicators_to_sortby))
    ]
    # this roughly translates to 'select all rows (denoted by :) for the given 
    # list of columns'
    .loc[:, target_columns]
    # converts the dataframe into a long format
    # in short it'll keep Indicator Name as a column
    # and all the year columns will pivot to a row elements (e.g. value_vars)
    # and all the year columns will now be headed under a new column (e.g. with var_name)
    # and also create a separate column to hold cell values 
    .melt(
        id_vars=["Indicator Name"],
        value_vars=target_years,
        var_name="Year",
        value_name="Value"
    )
)

# create our plot here, the first 2 parameters correspond to how many rows
# and columns of subplots you want respectively; figsize is how width and tall
# you want to overall viewport to be
fig, ax = plt.subplots(1, 2, figsize=(16, 10))
# use this for long format dataframes
# sns.catplot(
    # data=turkey_2020_to_2025,
    # x="Value",
    # y="Indicator Name",
    # col="Year",
    # kind="bar",
    # height=5,
    # aspect=0.6,
# )
# line plot or the other plots works fine too
sns.lineplot(
    data=turkey_2020_to_2025,
    x="Year",
    y="Value",
    hue="Indicator Name",
    ax=ax[0]
)
sns.barplot(
    data=turkey_2020_to_2025,
    x="Year",
    y="Value",
    hue="Indicator Name",
    ax=ax[1]
)
plt.show()

plotly_fig: Figure = px.scatter(
    # there is a weird formatting error that prevents plotly from loading 
    # the dataset originally (probably some corrupted or malformed transformation)
    # just run reset_index(drop=True) in this case
    # this essentially removes the old row index and replaces it again (like a 
    # reinitialization)
    turkey_2020_to_2025.reset_index(drop=True),
    x="Year",
    y="Value",
    color="Indicator Name",
    title="World Bank Turkey Overview 2020-2025"
)
# remove decimal points for the year axis
plotly_fig.update_layout(
    xaxis={
        "dtick": 1, # make the tick rate increment by 1 (this is the solution)
        "tickformat": "0.0f" # remove decimals
    }
)
plotly_fig.show()