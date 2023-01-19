import pandas as pd
import numpy as np
from datetime import datetime

## Deletes sensitive columns
def format_df(df):
    pd.options.mode.chained_assignment = None  # default='warn'

    if 'card_details' in df:
        del df['card_details']
    if 'name' in df:
        del df['name']
    
    return df
    
## Deletes given columns
def drop_columns(df, *columns):

    for column in columns:
        if column in df:
            del df[column]
        
    return df

def split_product_lines(df):
    # splits product lines into separate rows and removes spaces
    df = df.assign(product=df['product'].str.split(', ')).explode('product')
    return df

def product_table(df):
    df = format_df(df)
    df = split_product_lines(df)
    product_list = df['product'].tolist()
    product_list = np.unique(product_list)

    product_dict_list = []
    for item in product_list:
        product_dict = {}
        product_dict['product'] = item[:-7]
        product_dict['price'] = item[-4:]
        product_dict_list.append(product_dict)
    df = pd.DataFrame(product_dict_list)
    
    return df
