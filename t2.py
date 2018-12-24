import pandas as pd
df=pd.read_csv('report.csv')
print(df.columns.values)
df.drop('Unnamed: 0',axis=1,inplace=True)
df.Tweet[df.Report==-1]