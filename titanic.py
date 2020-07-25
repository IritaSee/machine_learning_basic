import pandas as pd
df=pd.read_csv('titanic.csv')
print(df.head()) #ngebaca 5 row pertama
print(df.describe()) #nulis statistiknya
#select cuman fare:
col = df['Fare']
print(col)
# select beberapa aja
small_df=df[['Age','Sex','Survived']]
print(small_df.head())