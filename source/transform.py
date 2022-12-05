######################################################
# Joseph Beckett
# Transform - A file to change the data to the clients specifications
# File Created 05/12/22
# File Last Edited 05/12/22
######################################################

from extract import read_file
import pandas as pd


def drop_sensitive():
    read_file()

    to_drop = [
        'Edition Statement',
        'Corporate Author',
        'Corporate Contributors',
        'Former owner',
        'Engraver',
        'Contributors',
        'Issuance type',
        'Shelfmarks',
        'Flickr URL'
    ]

    df.drop(to_drop, inplace = True, axis = 1)