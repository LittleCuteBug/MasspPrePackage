import numpy as np 
import matplotlib.pyplot as plt 
from scipy.spatial.distance import cdist

def init_data (n,k): # n = number points of each center, k = number of center
    means = np.random.randint(low = 0, high = 100, size = (k,2))
    cov = np.eye(2)*1000
    data = []
    for i in range(0,k):
        data.append(np.random.multivariate_normal(means[i],cov,n))
    return [means,np.concatenate(data[:],axis = 0)]
def init_center (k,data):
    return data[np.random.choice(data.shape[0],k,replace = False)]
def assign_label (data,center):
    return np.argmin(cdist(data,center),axis = 1)
def update_center(data,label,k):
    center = np.array([np.mean(data[label==i],axis = 0) for i in range(k)])
    return center
def stop_check (center,newcenter):
    return np.array_equal(center,newcenter)
def display (data,k,label):
    mark = ['bo','gv','r^','cs','m*','yD']
    for i in range(k):
        plt.plot(data[label==i,0],data[label==i,1],mark[i],markersize = 4)
def kmeans (k,data):    
    center = init_center(k,data)
    label = assign_label(data,center)
    while True:
        newcenter = update_center(data,label,k)
        newlabel = assign_label(data,newcenter)
        if stop_check(center,newcenter):
            break
        else: 
            center = newcenter
            label = newlabel
    return [center,label]
n = 1000
k = 3
means,data = init_data(n,k)
store = []
value = []
for i in range(100):
    center,label = kmeans (k,data)
    store.append([center,label])
    value.append(np.sum(cdist(data,center[label])))
center,label = store[np.argmin(value)]
display(data,k,label)
plt.plot(center[:,0],center[:,1],'kH',markersize = 10)
plt.axis("square")
