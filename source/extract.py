######################################################
# Joseph Beckett
# Extract - A file to extract data from csv files
# File Created 05/12/22
# File Last Edited 05/12/22
######################################################

## Imports
from main import clear
import pandas as pd

clear()

## Functions
# Reads CSV file
def read_file():
    global df
    
    # Reads CSV file and returns it as a dataframe
    df = pd.read_csv('data\chesterfield_25-08-2021_09-00-00.csv')

    return df
