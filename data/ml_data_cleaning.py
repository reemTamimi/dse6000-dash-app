import pandas as pd

predictions_df = pd.read_csv('ML_Predictions.csv')

# Make each separate parameter and powertrain its own column in each dataframe
predictions_powertrain_dummies = pd.get_dummies(predictions_df['powertrain'], prefix='powertrain')
predictions_parameter_dummies = pd.get_dummies(predictions_df['parameter'], prefix='parameter')

predictions_df = pd.concat([predictions_df, predictions_parameter_dummies, predictions_powertrain_dummies], axis=1)

# drop unnecessary columns in each dataframe
predictions_df_cleaned = predictions_df.drop(columns=['parameter'])

# Create .csv files of cleaned data for each dataframe
predictions_df_cleaned.to_csv('ML_Predictions_Cleaned.csv', index=False)






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