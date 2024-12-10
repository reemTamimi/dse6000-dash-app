import pandas as pd

historical_df = pd.read_csv('IEA-EV-dataEV salesHistoricalCars.csv')
projected_df = pd.read_csv('IEA-EV-dataEV salesProjection-STEPSCars.csv')

# check for missing values in each dataframe
print(f'Check # missing values in historical data:\n{historical_df.isnull().sum()}\n')
print(f'Check # missing values in projecteds data:\n{projected_df.isnull().sum()}\n')

# check for duplicate data in each dataframe
print(f'Check # duplicated values in historical data:\n{historical_df.duplicated().sum()}\n')
print(f'Check # duplicated values in projecteds data:\n{projected_df.duplicated().sum()}\n')

# Make each separate parameter and powertrain its own column in each dataframe
historical_powertrain_dummies = pd.get_dummies(historical_df['powertrain'], prefix='powertrain')
historical_parameter_dummies = pd.get_dummies(historical_df['parameter'], prefix='parameter')
projected_powertrain_dummies = pd.get_dummies(projected_df['powertrain'], prefix='powertrain')
projected_parameter_dummies = pd.get_dummies(projected_df['parameter'], prefix='parameter')

historical_df = pd.concat([historical_df, historical_parameter_dummies, historical_powertrain_dummies], axis=1)
projected_df = pd.concat([projected_df, projected_parameter_dummies, projected_powertrain_dummies], axis=1)

# merging both datasets for ML model
merged_df = pd.concat([historical_df, projected_df], ignore_index=True)
merged_df_cleaned = pd.get_dummies(merged_df, columns=['category'])

# drop unnecessary columns in each dataframe
historical_df_cleaned = historical_df.drop(columns=['mode','parameter'])
projected_df_cleaned = projected_df.drop(columns=['mode','parameter'])
merged_df_cleaned = merged_df_cleaned.drop(columns=['mode','parameter'])



# Create .csv files of cleaned data for each dataframe
historical_df_cleaned.to_csv('IEA-EV-dataEV salesHistoricalCars_Cleaned.csv', index=False)
projected_df_cleaned.to_csv('IEA-EV-dataEV salesProjection-STEPSCars_Cleaned.csv', index=False)
merged_df_cleaned.to_csv('IEA-EV-dataEV_Historical_Projected_Cleaned.csv', index=False)





'''
# Step 1: Load your historical and projection DataFrames
historical_data = pd.read_csv('path_to_historical_data.csv')  # Adjust with the correct file path
projection_data = pd.read_csv('path_to_projection_data.csv')  # Adjust with the correct file path
 
# Step 2: Merge historical data with projection data on the relevant columns
# Merge will match rows where region, parameter, mode, powertrain, year, and unit are the same
merged_data = pd.merge(historical_data, projection_data[['region', 'parameter', 'mode', 'powertrain', 'year', 'unit', 'value']], 
                       how='left', 
                       on=['region', 'parameter', 'mode', 'powertrain', 'year', 'unit'], 
                       suffixes=('_H', '_P'))
 
# Step 3: Add 'value_P' column to the merged data
# 'value_P' will now have projection values aligned with the matching historical records
# For rows without a matching projection, 'value_P' will be NaN (since it's from a left merge)
merged_data['value_P'] = merged_data['value_P'].fillna(merged_data['value_H'])
 
# Step 4: Optionally, remove the duplicate 'value' column if you don't need it anymore
merged_data = merged_data.drop(columns=['value_H', 'value'])
 
# Step 5: Check the merged dataframe
print(merged_data.head())
'''