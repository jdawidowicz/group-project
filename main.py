######################################################
# Joseph Beckett, Owen Illingworth
# Main - An ETL pipeline from cafe csvs to a database
# File Created 05/12/22
# File Last Edited 05/12/22
######################################################

## Imports
from source.extract import read_files
from source.transform import drop_columns
from source.transform import drop_sensitive
from source.transform import product_table
from source.load import load_to_database
import pandas as pd
import os

## Functions
# Clears terminal
def clear():
    os.system('cls')

## Main Code
clear()

# Reads the CSV file
dfs = read_files()
df = pd.concat(dfs)
products_df = pd.concat(dfs)
orders_df = pd.concat(dfs)


#create and load orders table
orders_df = drop_sensitive(orders_df)
orders_df = drop_columns(orders_df, 'product')

load_to_database(orders_df, 'order_id', 'orders')

#create and load products table
products_df = product_table(products_df)

load_to_database(products_df, 'products_id', 'products')
