######################################################
# Joseph Beckett, Owen Illingworth
# Main - An ETL pipeline from cafe csvs to a database
# File Created 05/12/22
# File Last Edited 05/12/22
######################################################

## Imports
# from source.extract import read_files
# from source.transform import *
# from source.load import *
# import pandas as pd
# import os

## Functions

# Reads the CSV file and merges.
dfs = read_files()
for df in dfs:
    df = format_df(df)

    #create and load orders table
    load_orders_table(df)

    #create and load products table
    load_products_table(df)

    #create and load basket table
    load_baskets(df)