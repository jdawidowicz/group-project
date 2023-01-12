from lambda_code.sql_utils import setup_db_connection, create_db_tables, create_engine_for_load_step
from lambda_code.transform import *

def load_to_database(df, table_name):
    engine = create_engine_for_load_step() # this will be useful for pandas df.to_sql method
    connection, cursor = setup_db_connection()
    create_db_tables(connection, cursor) # set up the sql tables that we will be loading to

    df.to_sql(table_name, engine, if_exists='append', index=False)


def load_baskets(df):
    baskets_df = pd.DataFrame.copy(df)
    baskets_df = create_basket_base(baskets_df)
    load_to_database(baskets_df, 'order_id', 'basket')

    connection, cursor = setup_db_connection()

    # update product_id from product table
    sql = "UPDATE basket SET product_id = products.product_id FROM products WHERE basket.product LIKE products.product"

    # drop product column
    sql_two = "ALTER TABLE basket DROP product"
    
    
    cursor.execute(sql)
    cursor.execute(sql_two)
    connection.commit()
    cursor.close()


def load_products_table(df):
    products_df = pd.DataFrame.copy(df)
    products_df = product_table(products_df)
    load_to_database(products_df , 'products')
    

def load_orders_table(df):
    orders_df = pd.DataFrame.copy(df)
    orders_df = drop_columns(orders_df, 'product')
    load_to_database(orders_df, 'orders')