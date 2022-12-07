######################################################
# Joseph Beckett
# Transform - A file to change the data to the clients specifications
# File Created 05/12/22
# File Last Edited 05/12/22
######################################################

import pandas as pd
import numpy as np


def drop_sensitive(df):
    # Reads the CSV file
    # Delets sensitive columns
    del df['card_details']
    del df['name']
    return df

def drop_columns(df, *columns):
    # Reads the CSV file
    # Delets sensitive columns

    for column in columns:
        del df[column]
        
    return df
    
def split_product_lines(df):
    # splits product lines into separate rows and removes spaces

    df = drop_sensitive(df)
    df = df.assign(product=df['product'].str.split(', ')).explode('product')

    return df

def product_table(df):
    # spaces not removed even though it works in the source function. Had to repeat the code
    # needs work but the output is correct

    product_df = split_product_lines(df)
    product_list = []
    product_list = product_df['product'].tolist()
    product_list = np.unique(product_list)
    product_dict_list = []
    for item in product_list:
        product_dict = {}
        product_dict['product'] = item[:-7]
        product_dict['price'] = item[-4:]
        product_dict_list.append(product_dict)
    product_df = pd.DataFrame(product_dict_list)

    return product_df

