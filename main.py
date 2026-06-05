#import pandas
import pandas as pd 

#import the csv 
df=pd.read_csv("housing_dev.csv")
#print(df.columns.tolist())

print(df)

#print unique data 
#print(df["Zoning District"].unique())
#print(df["Net Units"].unique())

#print(df["Planning Dist."].unique())

#print the net units 
#print(df["Net Units"]>=0)
