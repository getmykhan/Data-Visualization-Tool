import pandas as pd

def run(path):
<<<<<<< HEAD
    df = pd.read_csv(path)
    #df = df[['query_label','rank']]
    sr = df[[0]]
    return (sr)

run('April_2008.csv')
=======
    def run(path):
    df =  pd.read_csv(path)
    #print(aa['query_label'],['rank'])
    #df1 = df[['distance', 'rank']]
    #df1 = df.ix[0:,2:]
    sr = df[[3]]
    sr2 = df[[2]]
    print(sr, sr2)
    #plt.plot(sr, sr2)
    return (sr, sr2)
run('April_2008.csv')
>>>>>>> 861c9db176c7a28500891f1bcc9c1e9fa49f7d05
