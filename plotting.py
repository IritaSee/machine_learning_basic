import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('titanic.csv')
plt.scatter(df['Age'],df['Fare'])
#format si scatter itu akan di plot scatter (x,y)
plt.xlabel('Age');plt.ylabel('Fare')
#Kasih nama biar ga bingung