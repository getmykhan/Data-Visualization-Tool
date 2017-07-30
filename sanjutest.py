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

    graphplot(dfcol1,dfcol2,path)

def graphplot(dfcol1,dfcol2,path):
   plt.subplot(321)
   plt.plot(dfcol1,dfcol2)                  #line chart
   plt.title(path)
 #  plt.show()
   plt.subplot(322)
   plt.bar(dfcol1,dfcol2)                   #bar chart
   plt.title(path)

   plt.subplot(323)
   plt.hist(dfcol1,dfcol2)                   #histogram
   plt.title(path)

   plt.subplot(324)
   plt.scatter(dfcol1,dfcol2)                #scatter plot

   plt.subplot(325)
   plt.stackplot(dfcol1,dfcol2)              #stack chart

   slices=[6,8]
   plt.subplot(326)
   plt.pie(slices)

   plt.show()
   

if __name__ == '__main__':
    PullDataCsv('April_2008.csv')
