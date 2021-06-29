import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy




data = pd.read_csv('ABC-XYZ-data_3.csv',sep =';')

def ABC_analysis(df):
    
   
    # remove Quantity and Timeperiod columns

    df =df.drop(columns = ['Timeperiod', 'Quantity'])


    # groupby PT, Plant and Materials
  
    grouped_df = df.groupby(by=['PT', 'Plant', 'Material']).sum()
  

    # sorted with highest Pt(a->z), Plant(a->z), Revenue(H->L)
    
    grouped_df = grouped_df.sort_values(by=['PT','Plant','Revenue'], ascending=[True, True, False])
    
    #applied running totals at 3 dimentions (level = when runningtotal restarts)
    
    
    grouped_df['Running'] = grouped_df["Revenue"].groupby(level=['PT',"Plant"]).cumsum()

    #grouped_df['Running'] = grouped_df["Revenue"].groupby(level=[0]).cumsum()
    #new column subtotals
   
    

    
    
    #Calculating Subtotals of PT and Plants combined
    grouped_df["subt2"]=""
    grouped_df['subt2'] = grouped_df.groupby(['PT','Plant'])['Revenue'].sum()

    #Calculating percentiles on subtotals


    grouped_df["Subtotals"] = ' '
    grouped_df['Subtotals'] = grouped_df['Running']/grouped_df['subt2']
    # grouped_df["Subtotals"] = grouped_df.groupby(by=['PT','Plant'])['Running'].rank(pct=True).mul(100)
   
    # Checking the ABC ranking of the PT and Plant and Categorising into class A,B,C and splitting based on 80%-15%-5%
    

    grouped_df["ABC"] = ' '
    grouped_df["ABC"] = grouped_df["Subtotals"].apply(lambda x: "A" if x <0.801 else ('B' if x < 0.9501 else 'C'))

    #changing ABC type column from object into categoty to plot it
    grouped_df['ABC'] = grouped_df['ABC'].astype('category')
    
    
    return grouped_df

ABC = ABC_analysis (data)
print(ABC)
print(ABC.dtypes)

# plot





plt.bar(ABC["ABC"], ABC["Revenue"])

plt.legend('Revenue')
plt.xlabel("ABC")
plt.ylabel("Revenue in USD")
plt.title("ABC Analysis")
plt.show()
