import pandas as pd
import matplotlib.pyplot as plt

def PullDataCsv(path):
    df =  pd.read_csv(path)
    a=df['distance']
    b=df['rank']
    plt.plot(a,b)
    plt.xlabel('Query Label')
    plt.ylabel('Rank')
    plt.title('April 2008\ncsv file')
    plt.show()

PullDataCsv('April_2008.csv')
