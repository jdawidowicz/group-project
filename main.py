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
from source.transform import create_basket_base
from source.load import load_to_database
from source.load import load_baskets
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
df = pd.concat(dfs, ignore_index=True)
products_df = pd.concat(dfs, ignore_index=True)
orders_df = pd.concat(dfs, ignore_index=True)
baskets_df = pd.concat(dfs, ignore_index=True)

#create and load orders table
orders_df = drop_sensitive(orders_df)
orders_df = drop_columns(orders_df, 'product')

load_to_database(orders_df, 'order_id', 'orders')

#create and load products table
products_df = product_table(products_df)

load_to_database(products_df, 'product_id', 'products')

baskets_df = create_basket_base(baskets_df)

load_to_database(baskets_df, 'order_id', 'basket')

load_baskets()