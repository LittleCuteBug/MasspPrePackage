import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

# import the data

df = pd.read_csv("Salary_Data.csv")

X = ["YearsExperience","CollegeDegree"]

Y = ["Salary"]
X = df[X]
Y = df[Y]


n = X.shape[0]
one = np.array([[1]]*n)
Xbar = np.concatenate((one,X),axis = 1)

A = np.dot(Xbar.T,Xbar)
B = np.dot(Xbar.T,Y)
w = np.dot(np.linalg.pinv(A),B)

print(w)