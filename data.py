import pandas as pd
import matplotlib.pyplot as plt

def PullDataCsv(path):
    df =  pd.read_csv(path)                 #Reading CSV file
    dfnum = df._get_numeric_data()          #Getting only numeric columns
    i=0
    dfcol = {}

    for column in dfnum:
        dfcol[i] = dfnum[column]            #Extracting columns
        #(dfcol + str(i)) = dfnum[column]
        i = i+1

    #dfcol1 = dfnum.ix[:,0]
    #dfcol2 = dfnum.ix[:,1]
    dfcol1 = dfcol[0].values                #Create array of values in the dictionary
    dfcol2 = dfcol[1].values

    csvplot(dfcol1,dfcol2,path)

def csvplot(dfcol1,dfcol2,path):

    plt.plot(dfcol1,dfcol2)
    plt.title(path)
    plt.show()

if __name__ == '__main__':
    PullDataCsv('April_2008.csv')
