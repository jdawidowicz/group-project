## Imports
import pandas as pd
import glob
import os
import io

## Functions
# Reads CSV file
def read_files(csv_object):
    #create list to hold dataframes
    #list_of_df = []

    
    df = pd.read_csv(io.BytesIO(csv_object['Body'].read()), names=['date', 'branch', 'name', 'product', 'total_price', 'payment_type', 'card_details'])
    #list_of_df.append(df)

    return df
    #return list_of_df