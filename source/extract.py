######################################################
# Joseph Beckett
# Extract - A file to extract data from csv files
# File Created 05/12/22
# File Last Edited 05/12/22
######################################################

import pandas as pd

import os
os.system('cls')

def read_file():
    global df
    df = pd.read_csv('data\chesterfield_25-08-2021_09-00-00.csv')
    return df
