#import pandas (handling data) and seaborn (visuals)
import pandas as pd 
import seaborn as sb


#TO DO: ADD CLEANING LOGIC 
def cleaning_data(): 
    return 

#TO DO: ADD LOGIC TO SUM NET UNIT PER YEAR
def sum_net_per_year(year): 
    return 

def process_csv(): 
    #df=pd.read_csv("housing_dev.csv")
    return
    
def contains_null_value(df,column): 
    if (df[column].isnull().sum()!=0): 
        return True
    else: 
        return False

def check_entries_per_year(df):
    for i in range(2005,2025): 
      
        print(f"Year: {i} | Number Of Entries: {(df["BMR Reporting Year"]==i).sum()}")


#import the csv 
df=pd.read_csv("housing_dev.csv")
#print(df.columns.tolist())

#Check For Null Values
print(contains_null_value(df,"Net Units"))
print(contains_null_value(df,"BMR Reporting Year"))

check_entries_per_year(df)


#print unique data 
#print(df["Zoning District"].unique())
#print(df["Net Units"].unique())

#print(df["Planning Dist."].unique())

#print the net units 
#print(df["Net Units"]>=0)
