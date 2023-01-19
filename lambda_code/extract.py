## Imports
import pandas as pd
import glob
import os
import io

## Functions
# Reads CSV file
def read_files(csv_object):
    
    df = pd.read_csv(io.BytesIO(csv_object['Body'].read()), names=['time', 'branch', 'name', 'product', 'total_price', 'payment_type', 'card_details'])

    return df