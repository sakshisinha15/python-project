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
