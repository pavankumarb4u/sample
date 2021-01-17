import matplotlib.pyplot as plt
import pandas as pd 
data = pd.read_csv("btc.csv") 

result={'Date':[],'Volume':[],'Low':[],'High':[]}
for index, row in data.iloc[-365:].iterrows():
    result['Date'].append(row['Date'])
    result['Volume'].append(row['Volume'])
    result['Low'].append(round(row['Low']*0.87,6))
    result['High'].append(round(row['High']*0.87,6))

newdata=pd.DataFrame(result)
newdata.columns = ['Date', 'Volume','Low (EUR)','High (EUR)']
newdata.to_csv('output.csv',index = False, header=True)

y=['min','max','mean']
print ("\t\t"+"\t".join(y))
z=['Low (EUR)','High (EUR)','Volume']
z1=['Low (EUR)','High (EUR)','Volume (Billion)']
for x in z:
    v=[]
    
    if x=='Volume':
        v.append('Volume (Billion)')
        v.append(str(round(newdata[x].min()/1000000000,2)))
        v.append(str(round(newdata[x].max()/1000000000,2)))
        v.append(str(round(newdata[x].mean()/1000000000,2)))
    else:
        v.append(x)
        v.append(str(round(newdata[x].min(),2)))
        v.append(str(round(newdata[x].max(),2)))
        v.append(str(round(newdata[x].mean(),2)))
    print("\t".join(v))



newdata.plot(x ='Date', y=['Low (EUR)','High (EUR)'], kind = 'line', title=" Bitcoin price from "+newdata['Date'].min()+" to "+newdata['Date'].max())

plt.savefig('graph.png')  
