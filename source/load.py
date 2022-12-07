from sql_utils import setup_db_connection, create_db_tables, create_engine_for_load_step

def load_to_database(df, df_index, table_name):
    engine = create_engine_for_load_step() # this will be useful for pandas df.to_sql method
    connection, cursor = setup_db_connection()
    create_db_tables(connection, cursor) # set up the sql tables that we will be loading to

    df.to_sql(table_name, engine, index=df_index, if_exists='replace')