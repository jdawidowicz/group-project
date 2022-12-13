######################################################
# Joseph Beckett
# Transform - A file to change the data to the clients specifications
# File Created 05/12/22
# File Last Edited 05/12/22
######################################################

import pandas as pd
import numpy as np
from datetime import datetime
pd.options.mode.chained_assignment = None  # default='warn'


def format_df(df):
    # date to seconds
    # pd.options.mode.chained_assignment = None  # default='warn'
    # col = 'date'
    # for i in range(len(df[col])):
    #     current = df[col].iloc[i]
    #     dt = datetime.strptime(current, '%d/%m/%Y %H:%M')
    #     df[col].iloc[i] = int(dt.timestamp())

    # Deletes sensitive columns
    if 'card_details' in df:
        del df['card_details']
    if 'name' in df:
        del df['name']
    
    return df

def drop_columns(df, *columns):
    # Deletes sensitive columns
    for column in columns:
        if column in df:
            del df[column]     
    return df

def split_product_lines(df):
    # splits product lines into separate rows and removes spaces
    df = df.assign(product=df['product'].str.split(', ')).explode('product')
    return df

def product_table(df):
    # spaces not removed even though it works in the source function. Had to repeat the code
    # needs work but the output is correct
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



def create_order_basket(df):
    df = format_df(df)
    drop_columns(df, 'date', 'branch', 'total_price', 'payment_type', 'name')
    return df



