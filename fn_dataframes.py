import pandas as pd

def run(path):
    df =  pd.read_csv(path)
    #print(aa['query_label'],['rank'])
    #df1 = df[['distance', 'rank']]
    #df1 = df.ix[0:,2:]
    sr = list(df[[0]])
    sr2 = list(df[[1]])
    print(sr, sr2)
    #plt.plot(sr, sr2)
    return (sr, sr2)

run('April_2008.csv')
