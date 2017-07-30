from fn_dataframes import run
import matplotlib.pyplot as plt

#df = run('April_2008.csv')
#plt.plot([1,2,3],[4,5,1])
sr = run('April_2008.csv')
#sr1 = run.sr2
plt.plot(sr)
plt.xlabel('Query Label')
plt.ylabel('Rank')
plt.title('April 2008\ncsv file')
plt.show()
