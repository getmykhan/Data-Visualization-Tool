import pandas as pd
import matplotlib.pyplot as plt
import sys

def PullDataCsv(path):
    df =  pd.read_csv(path)                 #Reading CSV file
    dfnum = df._get_numeric_data()          #Getting only numeric columns
    i=0
    dfcol = {}

    for column in dfnum:
        dfcol[i] = dfnum[column]            #Extracting columns
        #(dfcol + str(i)) = dfnum[column]
        i = i+1

    dfcolarr = {}
    j=0
    while j < len(col_list):
        dfcolarr[j] = dfcol[col_list[j]].values
        j=j+1
    #dfcol1 = dfnum.ix[:,0]
    #dfcol2 = dfnum.ix[:,1]
    #dfcol1 = dfcol[1].values                #Create array of values in the dictionary
    #dfcol2 = dfcol[2].values

    csvplot(dfcolarr[0],dfcolarr[1],path)

def csvplot(dfcol1,dfcol2,path):

    plt.plot(dfcol1,dfcol2)
    plt.title(path)
    plt.show()

if __name__ == '__main__':
    col_list = []
    while True:
        cols = input("Enter the column: ")
        col_list.append(int(cols))
        exit = input("Done?: ")
        if exit == "yes":
            break
        else:
            continue

    print (col_list[1])
    PullDataCsv('April_2008.csv')
