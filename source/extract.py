######################################################
# Joseph Beckett
# Extract - A file to extract data from csv files
# File Created 05/12/22
# File Last Edited 05/12/22
######################################################

## Imports
import pandas as pd
import glob
import os


## Functions
# Reads CSV file
def read_files():
    #create list to hold dataframes
    list_of_df = []

    
    # Reads CSV file and returns it as a dataframe
    #The 'glob' function will look through the 'data' folder for any file enifing in '.csv'
    for csv in glob.glob("data\*.csv"):
        df = pd.read_csv(csv, names=['date', 'branch', 'name', 'product', 'total_price', 'payment_type', 'card_details'])
        list_of_df.append(df)

    
    return list_of_df

