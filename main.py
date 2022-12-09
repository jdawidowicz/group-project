######################################################
# Joseph Beckett, Owen Illingworth
# Main - An ETL pipeline from cafe csvs to a database
# File Created 05/12/22
# File Last Edited 05/12/22
######################################################

## Imports
from source.extract import read_files
from source.transform import *
from source.load import *
import pandas as pd
import os

## Functions
# Clears terminal
def clear():
    os.system('cls')

## Main Code
clear()

# Reads the CSV file and merges.
dfs = read_files()
for df in dfs:
    df = format_df(df)

    products_df = df
    orders_df = df
    baskets_df = df


    #create and load orders table
    orders_df = drop_columns(orders_df, 'product')
    load_to_database(orders_df, 'order_id', 'orders')

    #create and load products table
    products_df = product_table(products_df)
    load_to_database(products_df, 'product_id', 'products')

    #create and load basket table
    baskets_df = create_basket_base(baskets_df)
    load_to_database(baskets_df, 'order_id', 'basket')
    load_baskets()