import pandas as pd

def read_chain():
    df = pd.read_csv("spy_eod_202303.txt")

    return df 

df = read_chain()

print(df.head())