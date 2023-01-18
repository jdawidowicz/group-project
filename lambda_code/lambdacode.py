from lambda_code.transform import *
from lambda_code.load import *
from lambda_code.extract import*
import os
import json
import pandas as pd
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
  # TODO implement
  bucket = event['Records'][0]['s3']['bucket']['name']
  csv_file_name = event['Records'][0]['s3']['object']['key']
 
  csv_object = s3_client.get_object(Bucket=bucket,Key=csv_file_name)
  df = read_files(csv_object)
  df = format_df(df)
  
  load_temp_orders_table(df)
  #create and load orders table
  load_orders_table()
  

  #create and load products table
  load_products_table(df)
  
  #print(import_order_basket)
  #create and load basket table
  load_item_basket_table()
  load_baskets()
  drop_temporary_rows()
  
  return {
    'statusCode': 200,
    'body': json.dumps('Hello from Lambda!')
    }  