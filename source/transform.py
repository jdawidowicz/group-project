
import numpy as np

def split_product_lines():
    # splits product lines into separate rows and removes spaces
    df = drop_sensitive()
    df = df.assign(product=df['product'].str.split(',')).explode('product')
    col = 'product'
    for i in range(len(df[col])):
        current = df[col].iloc[i]
        if str(current).startswith(' '):
            df[col].iloc[i] = current[1:]
        return df


def product_table():
    # spaces not removed even though it works in the source function. Had to repeat the code
    # needs work but the output is correct
    product_df = split_product_lines()
    col = 'product'
    for i in range(len(product_df[col])):
        current = product_df[col].iloc[i]
        if str(current).startswith(' '):
            product_df[col].iloc[i] = current[1:]
    product_list = []
    product_list = product_df['product'].tolist()
    product_list = np.unique(product_list)
    product_dict_list = []
    for item in product_list:
        product_dict = {}
        product_dict['product'] = item[:-7]
        product_dict['price'] = item[-4:]
        product_dict_list.append(product_dict)
    product_df = pd.DataFrame(product_dict_list)
    return product_df











        

