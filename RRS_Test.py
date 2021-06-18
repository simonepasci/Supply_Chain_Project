import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




data = pd.read_csv(r'C:\Users\NA26035\OneDrive - Trinseo\Desktop\Udacity\Github_projects\ABC-XYZ-data_3.csv',sep =';')

def RRS_analysis(df):
    
    #Remove Revenue from Columns
    
    df = df.drop(columns=['Revenue'])

    # groupby Plant and Materials and Months
    
    grouped_df = df.groupby(['Plant','Material', 'Timeperiod'])['Quantity'].sum().to_frame().reset_index()

    #transform months into datatime
    grouped_df["MonthsC"] = pd.to_datetime(grouped_df['Timeperiod'])
    
    #found the most recent month
    grouped_df["MonthsM"] = grouped_df['MonthsC'].max()

    # nr months between 2 dates

"""check the difference between 2 dates"""
    #grouped_df['MonthsD'] = grouped_df["MonthsC"] - grouped_df['MomthsM']
    #grouped_df['MonthsD'] = ((grouped_df["MonthsC"] - grouped_df['MomthsM'])/np.timedelta64(1,'M'))
    #grouped_df['MonthsD'] = grouped_df['MonthsD'].astype(int)



    # sorted with highest Pt(a->z), Plant(a->z), Revenue(H->L)
    
    grouped_df = grouped_df.sort_values(by=['Timeperiod'], ascending=[True])
    

   
    
   
  
   
    
    
    return grouped_df

RRS = RRS_analysis (data)
print(RRS)
print(RRS.dtypes)




