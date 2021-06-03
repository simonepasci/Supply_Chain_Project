import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



data = pd.read_csv('ABC-XYZ-data_2.csv',sep =';')

def ABC_analysis(df):
    
    # groupby Plant and Materials
  
    grouped_df = df.groupby(by=['Plant', 'Material']).sum()
  

    # sorted with highest revenue
    
    grouped_df = grouped_df.sort_values(by=['Plant','Revenue'], ascending=[True, False])
    
    #applied running totals at 2 previous dimentions


    grouped_df['Running'] = grouped_df["Revenue"].groupby(level=[0]).cumsum()
    #new column subtotals
   
    #
    
   #Calculating Subtotals
    grouped_df["Subtotals"] = ' '
    grouped_df["Subtotals"] = grouped_df.groupby('Plant')['Running'].rank(pct=True).mul(100)
   
    ## Checking the Importance of the Customers and Categorising into class A,B,C and splitting based on 20-30-50
    ## Ranking by importance
    grouped_df["ABC"] = ' '
    grouped_df["ABC"] = grouped_df["Subtotals"].apply(lambda x: "A" if x <80 else ('B' if x < 95 else 'C'))
   
    
    
    return grouped_df

ABC = ABC_analysis (data)
print(ABC)
