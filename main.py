######################################################
# Joseph Beckett, Owen Illingworth
# Main - An ETL pipeline from cafe csvs to a database
# File Created 05/12/22
# File Last Edited 05/12/22
######################################################

## Imports
from sql_utils import setup_db_connection, create_db_tables, create_engine_for_load_step
from source.extract import read_files
from source.transform import drop_sensitive
import os

## Functions
# Clears terminal
def clear():
    os.system('cls')

## Main Code
clear()

# Reads the CSV file
dfs = read_files()

# Deletes the columns of sensitive information
for df in dfs:
    print(drop_sensitive(df))

## Load
engine = create_engine_for_load_step() # this will be useful for pandas df.to_sql method
connection, cursor = setup_db_connection()
create_db_tables(connection, cursor) # set up the sql tables that we will be loading to

for df in dfs:
    df.to_sql('test', engine, index=False, if_exists='replace')

