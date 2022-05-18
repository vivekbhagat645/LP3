from google.colab import files
uploaded = files.upload()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

data=pd.read_csv('d2.csv')

plt.scatter(data['x1'],data['y1'])

def dist(c,x):
    return np.sum(np.abs(c-x))

data1=np.array(data)

c1=data1[1]
c2=data1[7]
x=np.array(data1)
c1=c1.reshape(1,2)
c2=c2.reshape(1,2)
x.shape,c1.shape,c2.shape

for i in range(20):
    l1=[]
    l2=[]
    for j in range(len(x)):
        d1=dist(c1,x[j])
        d2=dist(c2,x[j])
        if(d1<=d2):
            l1.append(x[j])
            
        else:
            l2.append(x[j])
    
    c1=np.mean(l1,axis=0)
    c2=np.mean(l2,axis=0)
    
l1=np.array(l1)
l1.shape

l2=np.array(l2)
l2.shape

plt.scatter(x=l1[:,0],y=l1[:,1],c='r')
plt.scatter(x=l2[:,0],y=l2[:,1],c='g')
plt.scatter(x=c1[0],y=c1[1],c='b')
plt.scatter(x=c2[0],y=c2[1],c='y')