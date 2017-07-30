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