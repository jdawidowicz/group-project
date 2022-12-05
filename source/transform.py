######################################################
# Joseph Beckett
# Transform - A file to change the data to the clients specifications
# File Created 05/12/22
# File Last Edited 05/12/22
######################################################

from source.extract import read_file
import pandas as pd


def drop_sensitive():
    # Reads the CSV file
    df = read_file()

    # Delets sensitive columns
    del df['card_details']
    del df['name']

    return df