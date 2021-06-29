<<<<<<< HEAD
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
    


    # sorted with highest Pt(a->z), Plant(a->z), Revenue(H->L)
   
    grouped_df = grouped_df.sort_values(by=['Timeperiod'], ascending=[True])
    
    
    # nr months between 2 dates
    #0 =  most recent and ## oldest
    
 
    grouped_df['MonthsD'] = ((grouped_df["MonthsM"] -  grouped_df["MonthsC"]) /np.timedelta64(1, 'M'))
    
    grouped_df["MonthsD"] = grouped_df["MonthsD"].astype(int)


    #drop Timeperiod, MonthsC, MonthsM
    
    grouped_df.drop(['Timeperiod','MonthsC', 'MonthsM'], axis = 1, inplace=True)
    
    #leave only 12 months

    grouped_df = grouped_df[grouped_df["MonthsD"] < 12]
    
    #pivot dataframe

    grouped_df = grouped_df.pivot(columns = "MonthsD", values = "Quantity")

    #replace NaN with 0 in all dataframe

    grouped_df.fillna(0, inplace = True)

    return grouped_df

RRS = RRS_analysis (data)
print(RRS)
print(RRS.dtypes)









#plt.bar(ABC["ABC"], ABC["Revenue"])

#plt.legend()
#plt.xlabel("ABC")
#plt.ylabel("Revenue in USD")
#plt.title("ABC Analysis")
#plt.show()
||||||| empty tree
=======
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




data = pd.read_csv(r ABC-XYZ-data_3.csv',sep =';')

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




>>>>>>> afa7716b591831787dc3ac51515e30cf7a3ddfaa
