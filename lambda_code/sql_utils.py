import psycopg2
import os
#from dotenv import load_dotenv
from sqlalchemy import create_engine
import boto3
import json
#import redshift_connector

ssm = boto3.client('ssm')
parameter = ssm.get_parameter(Name='team1', WithDecryption=True)
secret_json = json.loads(parameter['Parameter']['Value'])
#{"username":"team1","password":"Ghio4*(2dxc","engine":"redshift","host":"redshiftcluster-uskxazijhsjf.cfpmkbr0g5vs.eu-west-1.redshift.amazonaws.com","port":5439,"dbClusterIdentifier":"redshiftcluster-uskxazijhsjf"}

HOST=secret_json['host']
USER=secret_json['username']
PASSWORD=secret_json['password']
DB_NAME=secret_json['database']
PORT=secret_json['port']

DB_DATA = 'postgresql+psycopg2://' + USER + ':' + PASSWORD + '@' + HOST + ':5439/' \
       + DB_NAME
# + '?charset=utf8mb4'
#f"postgresql+psycopg2://{USER}:{PASSWORD}@localhost:5432\{DB_NAME}'?charset=utf8mb4"


def setup_db_connection(host=HOST, user=USER, password=PASSWORD, port=PORT, db_name=DB_NAME):

    connection = psycopg2.connect(host=host, user=user, password=password, port=port, database=db_name)
    cursor = connection.cursor()
    
    # connection = redshift_connector.connect(
    #     host=host,
    #     database='dev',
    #     port='5439',
    #     user='awsuser',
    #     password='my_password'
    # )
  
    #cursor = connection.cursor()
    
    return connection, cursor

def create_db_tables(connection, cursor):
    
    # create_basket_data_table = \
    # """
    #     CREATE TABLE IF NOT EXISTS basket(
    #         order_id int NOT NULL AUTO_INCREMENT,
    #         product varchar(50),
    #         product_id int NULL
    #     );
    # """;
    # create_product_data_table = \
    # """
    #     CREATE TABLE IF NOT EXISTS products(
    #         product_id int NOT NULL AUTO_INCREMENT,
    #         product varchar(50),
    #         price float
    #     );
    # """;
    create_order_data_table = \
    """
        CREATE TABLE IF NOT EXISTS team1orders(
            
            date varchar(20),
            payment_type varchar(7),
            total_price decimal,
            branch varchar(20)
        );
    """;
    #order_id int smallseria,
    
    #cursor.execute(create_basket_data_table)
    #cursor.execute(create_product_data_table)
    cursor.execute(create_order_data_table)
    connection.commit()
    cursor.close()
    connection.close()

def create_engine_for_load_step(db_data=DB_DATA):
    return create_engine(db_data)
