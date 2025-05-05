
# coding: utf-8

# In[1]:


# import all libraries needed
import numpy as np
import pandas as pd
import missingno as msno
import janitor
from scipy import stats
from sklearn.preprocessing import minmax_scale
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import fuzzywuzzy
from fuzzywuzzy import process
import chardet


def load_data(df):

    # import the data
    df = pd.read_csv(data_file,delimiter=',')
    # store the data in a new variable for later use
    self.df_with_predictions = df.copy()
    # set seed for reproducibility
    np.random.seed(0)

def check_missing_values(df):

    # get the number of missing data points per column
    missing_values_count = df.isnull().sum()
    # look at the missing points
    missing_values_count[0:10]
    # get the total number of missing values
    total_cells = np.product(df.shape)
    total_missing = missing_values_count.sum()
    # percent of data that is missing
    percent_missing = (total_missing/total_cells)*100

    print("Missing values per column:")
    print(missing_values_count[0:10])
    print(f"\nTotal missing: {total_missing}")
    print(f"Percent of total:{percent_missing}")

    return missing_values_count

def drop_missing_values_by_row(df):

    # remove all the rows that contain a missing value
    df.dropna()
    return df.dropna()

def drop_missing_values_by_column(df):


    # remove all columns with at least one missing value
    columns_with_na_dropped = df.dropna(axis=1)

    # check how much data did we lose
    print(f"Number of original columns: {df.shape[1]}\n")
    print(f"Number of existing columns: {columns_with_na_dropped.shape[1]}")

    return columns_with_na_dropped.head()

def backfill_missing_values(df):

    #replace all NA's the value that comes directly after it in the same column
    df = df.fillna(method = 'bfill',axis=0).fillna(0)

    return df

def avgfill_missing_values(df,column):

    # fill the data with average value in that column
    df['column'] = df['column'].fillna(df['column'].mean(), axis = 0, inplace = True)

    return df

def min_max_scaling(df,column):

    # scale the data between 0 and 1
    scaled_data = minmax_scale(df['column'])
    # plot both together to compare
    fig,ax = plt.subplots(1, 2, figsize=(10,4))
    sns.histplot(df, ax=ax[0],kde=True)
    ax[0].set_title("Original Data")
    sns.histplot(scaled_data, ax=ax[1],kde=True)
    ax[1].set_title("Scaled Data")

    return scaled_data

def normalization(df,column):

    #get only positive columns
    positive_column =  df['column'][df['column'] > 0]

    # normalize the column using boxcox
    normalized_column = stats.boxcox(positive_column)[0]

    # plot both together to compare
    fig, ax=plt.subplots(1, 2, figsize=(10,4))
    sns.histplot(positive_column, ax=ax[0],kde=True)
    ax[0].set_title("Original Data")
    sns.histplot(normalized_column, ax=ax[1],kde=True)
    ax[1].set_title("Normalized data")

    return normalized_column













    
