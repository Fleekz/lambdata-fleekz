"""Helper Functions"""

import pandas as pd
import numpy as np
import datetime as dt

# Function to find the amount of null values in a dataframe
def null_count(df):
    return print(df.isnull().sum().sum().astype(int))

array = [1, 3, np.nan, 7, np.nan]
array2 = [2, np.nan, 6, np.nan, 10]
df = pd.DataFrame(data=(array, array2))
# Made arrays and combined into a dataframe
# When using in python as import helper_functions as hf
# Type "hf.null_count(hf.df)" to find the null values in this dataframe



# Function to split dates into different columns
def split_dates(date_series):
  df = pd.DataFrame({'date': date_series})
  df['month'] = pd.to_datetime(df['date']).dt.month
  df['day'] = pd.to_datetime(df['date']).dt.day
  df['year'] = pd.to_datetime(df['date']).dt.year
  df.drop(columns='date', inplace=True)
  return df

# List of dates
dates = ('01/01/2000', '05/05/2005', '07/04/1776', '12/25/2020')
# Putting the list of dates into a series
date_series = pd.Series(dates)
