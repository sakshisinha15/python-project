import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('datasetproject.csv')
print("Data loaded successfully")
print("------------------------------------\n")
print("1ST 10 ROWS OF THE DATASET")
#1 st 10 rows of the dataset
print("------------------------------------\n")
print(df.head(10))
print("------------------------------------\n")
print("LAST 10 ROWS OF THE DATASET")
#last 10 rows o the dataset
print("------------------------------------\n")
print(df.tail())
print("------------------------------------\n")
print("INFO ABOUT THE DATASET")
#info about the dataset
print("------------------------------------\n")
print(df.info())
print("------------------------------------\n")
print("MEAN ,STD,QUARTILE,MIN,MAX OF THE DATASET")
print("------------------------------------\n")
#info about the mean,std.deviation,quartile one,two,three
print(df.describe())
print("------------------------------------------------------------\n")
print("                    DATA  CLEANING                            ")
print("------------------------------------------------------------\n")
print(df.isnull().sum())
#Filling missing values with specific values
df_filled=df.fillna({'geologic_province':df['geologic_province'].mode()[0],'country': df['country'].mode()[0],
                     'reference':df['reference'].mode()[0]})
print("\nDataframe after filling missing values:")
print(df_filled)
print(df_filled.isnull().sum())

#Dropping rows with missing values
df_dropped_rows=df.dropna()
print("\nDataFrame after dropping rows with missing values:")

#Dropping columns with missing values
df_dropped_cols=df.dropna(axis=1)
print("\nDataFrame after dropping cols with missing values:")
print(df_dropped_cols)

#saving cleaned data
cleaned_file_path="datasetproject.csv"
df.to_csv(cleaned_file_path,index=False)
print(f"Cleaned data saved to: {cleaned_file_path}")
