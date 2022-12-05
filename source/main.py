######################################################
# Joseph Beckett
# Main - An ETL pipeline from cafe csvs to a database
# File Created 05/12/22
# File Last Edited 05/12/22
######################################################

## Imports
from extract import read_file
import os

## Functions
# Clears terminal
def clear():
    os.system('cls')

print(read_file())