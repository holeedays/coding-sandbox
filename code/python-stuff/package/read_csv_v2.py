"""
This is just more of a test to experiment with the turkey data I pulled,
ignore this page lol
"""

import pandas as pd
from pandas import DataFrame, Series
from pandas.core.groupby import DataFrameGroupBy

import seaborn as sns

from .csv_utils import print_in_full

path: str = "C:/Users/weigh/Downloads/turkey_stats.csv";


raw_df: DataFrame = pd.read_csv(
    path,
    skiprows=4
)

# print_in_full(raw_df["Indicator Name"])


target_indicators: tuple[str] = (
    "Net bilateral aid flows from DAC donors, United States (current US$)",
    "Net bilateral aid flows from DAC donors, Slovak Republic (current US$)",
    "Net bilateral aid flows from DAC donors, Norway (current US$)",
    "Net bilateral aid flows from DAC donors, Korea, Rep. (current US$)",
    "Net bilateral aid flows from DAC donors, Ireland (current US$)"
)
target_years: tuple[str] = (for str(i) in range(1990, 2025, 1))

(
    raw_df[
        (raw_df["Indicator Name"].isin(target_indicators)) 
    ].loc[:, ]
)


