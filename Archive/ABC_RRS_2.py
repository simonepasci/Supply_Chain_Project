import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


data = pd.read_csv(r'C:\Users\NA26035\OneDrive - Trinseo\Desktop\Udacity\Github_projects\ABC-XYZ-data.csv',sep =';')

def ABC_analysis(df):
    grouped_df = (
            df.loc[:, ['CustomerID','Revenue']]
            .groupby('CustomerID')
            .sum()         
        )

    grouped_df = grouped_df.sort_values(by=['Revenue'], ascending=False)
    
    ## Ranking by importance
    grouped_df["Rank"] = grouped_df['Revenue'].rank(ascending = False)
    grouped_df["Importance"] = ' '
    grouped_df = grouped_df.reset_index()

    ## Checking the Importance of the Customers and Categorising into class A,B,C and splitting based on 20-30-50
    grouped_df['Importance'][0: int(0.2 * grouped_df['Rank'].max())] = 'A'
    grouped_df['Importance'][int(0.2 * grouped_df['Rank'].max()) : int(0.95 * grouped_df['Rank'].max())] = 'B'
    grouped_df['Importance'][int(0.95 * grouped_df['Rank'].max()): ] = 'C'                  
    
    return grouped_df



ABC_groups = ABC_analysis(data)
print(ABC_groups.head())

