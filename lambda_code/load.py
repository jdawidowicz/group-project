from lambda_code.sql_utils import setup_db_connection, create_db_tables, create_engine_for_load_step
from lambda_code.transform import *

def load_to_database(df, table_name):
    engine = create_engine_for_load_step() # this will be useful for pandas df.to_sql method
    connection, cursor = setup_db_connection()
    create_db_tables(connection, cursor) # set up the sql tables that we will be loading to

    df.to_sql(table_name, engine, if_exists='append', index=False)

def create_order_basket(df):
    df = format_df(df)
    drop_columns(df, 'date', 'branch', 'total_price', 'payment_type', 'name')
    return df

def load_products_table(df):
    products_df = pd.DataFrame.copy(df)
    products_df = product_table(products_df)
    load_to_database(products_df , 'products')

def load_orders_table(df):
    orders_df = pd.DataFrame.copy(df)
    orders_df = drop_columns(orders_df, 'product')
    load_to_database(orders_df, 'orders')

def load_order_basket_table(df):
    order_basket_df = pd.DataFrame.copy(df)
    order_basket_df = create_order_basket(order_basket_df)
    load_to_database(order_basket_df, 'order_basket')  

def load_item_basket_table():
    item_basket_df = create_item_basket()
    load_to_database(item_basket_df, 'item_basket')  

def import_order_basket():
    engine = create_engine_for_load_step() # this will be useful for pandas df.to_sql method
    df = pd.read_sql("SELECT * FROM order_basket", engine)
    return df

def load_baskets():
    connection, cursor = setup_db_connection()
    sql_update = ("UPDATE item_basket SET product_id = products.product_id FROM products join item_basket t on t.product = products.product")
    cursor.execute(sql_update)
    sql_insert = ("INSERT INTO baskets (SELECT order_id, product_id FROM item_basket)")
    cursor.execute(sql_insert)
    connection.commit()
    cursor.close()
    connection.close()

def create_item_basket():
    df = import_order_basket()
    df = split_product_lines(df)
    col = 'product'
    for i in range(len(df[col])):
        current = df[col].iloc[i]
        df[col].iloc[i] = current[:-7]
    return df