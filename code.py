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

####################OBJECTIVE1( Rank Geothermal Sites by Energy Potential)##################################
### ranked list of geothermal areas based on their beneficial heat over 30 years and accessible resource base, identifying the most energy-rich locations in the U.S.#################
top_regions = df.sort_values(by='beneficial_heat_mwh', ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x='beneficial_heat_mwh',y='geothermal_area',hue='geothermal_area',data=top_regions,palette='YlOrRd',dodge=False,legend=False)
plt.title('Top 10 Geothermal Areas by Energy Potential (MWh)')
plt.xlabel('Beneficial Heat (MWh)')
plt.ylabel('Geothermal Area')
plt.tight_layout()
plt.show()
#################OBJECTIVE2(Analyze the Relationship Between Temperature and Energy Output)########################
##############statistically significant correlation between reservoir temperature and energy output (MWh or MW over 30 years).#########
numeric_cols = ['temperature_c', 'beneficial_heat_mwh', 'wells', 'reservoir_area_km2', 'reservoir_volume_km3']
corr_matrix = df[numeric_cols].corr()
# Plot heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap of Geothermal Parameters')
plt.tight_layout()
plt.show()
########################OBJECTIVE3(Compare Efficiency by System Type)####################################
################different geothermal system types (e.g., sedimentary basin, delineated area) to see which offers the best energy yield per well or per unit area.########
df['heat_per_well'] = df['beneficial_heat_mwh'] / df['wells']
efficiency = df.groupby('system_type')['heat_per_well'].mean().sort_values(ascending=False)
efficiency_df = efficiency.reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=efficiency_df,x='heat_per_well',y='system_type',hue='system_type',palette='coolwarm',legend=False)
plt.title('Average Heat Output per Well by System Type')
plt.xlabel('Heat per Well (MWh)')
plt.ylabel('System Type')
plt.tight_layout()
plt.show()
#########################OBJECTIVE4( Visualize Geothermal Energy by State)###############################
######################################### Total geothermal potential per U.S. state based on the dataset###########################################################
area_heat = df.groupby('geothermal_area')['beneficial_heat_mwh'].sum().sort_values(ascending=False)
area_heat_df = area_heat.reset_index()
area_heat_df.columns = ['geothermal_area', 'total_heat']
top_n = 10
area_heat_df = area_heat_df.head(top_n)
plt.figure(figsize=(12, 6))
sns.lineplot(data=area_heat_df, x='geothermal_area', y='total_heat', marker='o', linewidth=2.5)
plt.title('Beneficial Heat Output by Geothermal Area (Top 10)', fontsize=14)
plt.xlabel('Geothermal Area', fontsize=12)
plt.ylabel('Total Heat (MWh)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
##########################OBJECTIVE5( Optimize Well Deployment for Maximum Output)#####################################################
####################### the most efficient well configurations (wells per area, heat per well) to guide future deployment strategies.#######
df['heat_per_well'] = df['beneficial_heat_mwh'] / df['wells']
df['wells_per_km2'] = df['wells'] / df['reservoir_area_km2']
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='wells_per_km2', y='heat_per_well', hue='system_type')
plt.title('Well Optimization: Heat per Well vs Wells per km²')
plt.xlabel('Wells per km²')
plt.ylabel('Heat per Well (MWh)')
plt.tight_layout()
plt.show()

