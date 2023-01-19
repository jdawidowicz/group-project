from lambda_code.sql_utils import setup_db_connection, create_db_tables, create_engine_for_load_step
from lambda_code.transform import *

##Function to load a given dataframe to a given table
def load_to_database(df, table_name):
    engine = create_engine_for_load_step() # this will be useful for pandas df.to_sql method
    connection, cursor = setup_db_connection()
    create_db_tables(connection, cursor) # set up the sql tables that we will be loading to

    df.to_sql(table_name, engine, if_exists='append', index=False)
    cursor.close()
    connection.close()

##Functions to load individual tables
def load_temp_orders_table(df):
    load_to_database(df, 'temp_orders')

def load_products_table(df):
    products_df = pd.DataFrame.copy(df)
    products_df = product_table(products_df)
    load_to_database(products_df , 'products')

def load_orders_table():
    connection, cursor = setup_db_connection()
    cursor.execute("""
    INSERT INTO orders (order_id, total_price, branch, "time", payment_type) 
    SELECT order_id, total_price, branch, "time", payment_type  
    FROM temp_orders
    """)
    connection.commit()
    cursor.close()
    connection.close()
 

def load_item_basket_table():
    item_basket_df = create_item_basket()
    load_to_database(item_basket_df, 'item_basket')  

def import_order_basket():
    engine = create_engine_for_load_step() # this will be useful for pandas df.to_sql method
    df = pd.read_sql("SELECT order_id, product FROM temp_orders", engine)
    return df

def load_baskets():
    connection, cursor = setup_db_connection()
    sql2 = ("UPDATE item_basket SET product_id = products.product_id FROM products join item_basket t on t.product = products.product")
    cursor.execute(sql2)
    sql4 = ("INSERT INTO baskets (SELECT order_id, product_id FROM item_basket)")
    cursor.execute(sql4)
    connection.commit()
    cursor.close()
    connection.close()

def create_item_basket():
    pd.options.mode.chained_assignment = None  # default='warn'
    df = import_order_basket()
    split_df = split_product_lines(df)
    col = 'product'
    for i in range(len(split_df[col])):
        current = split_df[col].iloc[i]
        split_df[col].iloc[i] = current[:-7]
    return split_df
     
def drop_temporary_rows():
    connection, cursor = setup_db_connection()
    sql = ("DELETE FROM temp_orders;")
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()