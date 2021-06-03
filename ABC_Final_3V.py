import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




data = pd.read_csv('ABC-XYZ-data_3.csv',sep =';')

def ABC_analysis(df):
    
    # groupby PT, Plant and Materials
  
    grouped_df = df.groupby(by=['PT', 'Plant', 'Material']).sum()
  

    # sorted with highest Pt(a->z), Plant(a->z), Revenue(H->L)
    
    grouped_df = grouped_df.sort_values(by=['PT','Plant','Revenue'], ascending=[True, True, False])
    
    #applied running totals at 3 previous dimentions


    grouped_df['Running'] = grouped_df["Revenue"].groupby(level=[0]).cumsum()
    #new column subtotals
   
    
    

    grouped_df["Subtotals"] = ' '

    #Calculating percentiles on subtotals


    grouped_df["Subtotals"] = grouped_df.groupby(['PT','Plant'])['Running'].rank(pct=True).mul(100)
   
    # Checking the ABC ranking of the PT and Plant and Categorising into class A,B,C and splitting based on 80%-15%-5%
    

    grouped_df["ABC"] = ' '
    grouped_df["ABC"] = grouped_df["Subtotals"].apply(lambda x: "A" if x <80 else ('B' if x < 95 else 'C'))

    #changing ABC type column from object into categoty to plot it
    grouped_df['ABC'] = grouped_df['ABC'].astype('category')
    
    
    return grouped_df

ABC = ABC_analysis (data)
print(ABC)
print(ABC.dtypes)



x_indexes = np.arange(len(ABC["ABC"]))
width = 0.25

plt.bar(x_indexes-width, ABC["Revenue"], width=width)
plt.bar(x_indexes, ABC["Quantity"], width=width)
plt.legend()
plt.xlabel("ABC")
plt.ylabel("Revenue in USD")
plt.title("ABC Analysis")
plt.show()
