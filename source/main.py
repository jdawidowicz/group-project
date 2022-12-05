######################################################
# Joseph Beckett
# Main - An ETL pipeline from cafe csvs to a database
# File Created 05/12/22
# File Last Edited 05/12/22
######################################################

## Imports
from extract import read_file
from transform import drop_sensitive
import os

## Functions
# Clears terminal
def clear():
    os.system('cls')

clear()

# Reads the CSV file
print(read_file())

# Deletes the columns of sensitive information
print(drop_sensitive())
