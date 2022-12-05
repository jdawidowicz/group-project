import psycopg2
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
HOST = os.environ.get("POSTGRES_host")
USER = os.environ.get("POSTGRES_user")
PASSWORD = os.environ.get("POSTGRES_pass")
DB_NAME = os.environ.get("POSTGRES_db")

DB_DATA = 'postgresql+psycopg2://' + USER + ':' + PASSWORD + '@' + 'localhost' + ':5432/' \
       + DB_NAME
# + '?charset=utf8mb4'
#f"postgresql+psycopg2://{USER}:{PASSWORD}@localhost:5432\{DB_NAME}'?charset=utf8mb4"


def setup_db_connection(host=HOST, user=USER, password=PASSWORD, db_name=DB_NAME):

    connection = psycopg2.connect(host=host, user=user, password=password, database=db_name)
    cursor = connection.cursor()
    return connection, cursor

def create_db_tables(connection, cursor):
    
    create_test_data_table = \
    """
        CREATE TABLE IF NOT EXISTS test(
            customer_id int NOT NULL,
            purchase_date date,
            purchase_amount decimal(19,2),
            product_id varchar(10)
        );
    """;
    
    cursor.execute(create_test_data_table)
    connection.commit()
    cursor.close()
    connection.close()

def create_engine_for_load_step(db_data=DB_DATA):
    return create_engine(db_data)
