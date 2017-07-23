import pandas as pd

def run(path):
    df = pd.read_csv(path)
    #df = df[['query_label','rank']]
    sr = df[[0]]
    return (sr)

run('April_2008.csv')
