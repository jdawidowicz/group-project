from sql_utils import setup_db_connection, create_db_tables, create_engine_for_load_step
import csv
import pandas as pd

df = pd.read_csv("chesterfield_25-08-2021_09-00-00.csv")

### LOAD
engine = create_engine_for_load_step() # this will be useful for pandas df.to_sql method
connection, cursor = setup_db_connection()
create_db_tables(connection, cursor) # set up the sql tables that we will be loading to


df.to_sql('test', engine, index=False, if_exists='replace')