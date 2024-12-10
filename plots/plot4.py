import plotly.express as px
import numpy as np
import pandas as pd

def create_plot4(df,selected_region):
    regional_yearly_sums = df[df['parameter_EV sales']].groupby(['region', 'year'])['value'].sum()
    df['regional_yearly_sum'] = df.set_index(['region', 'year']).index.map(regional_yearly_sums)
    df['BEV/EV_sales'] = np.where(
        (df['parameter_EV sales'] == True) & (df['powertrain_BEV'] == True),
        (df['value'] / df['regional_yearly_sum']),
        np.nan
    )

    # Filter the dataset
    filtered_df = df[pd.notna(df['BEV/EV_sales'])]
    grouped_df = filtered_df.groupby(['region', 'year'])['BEV/EV_sales'].sum().reset_index()

    # Create the plot
    filtered_df = grouped_df[grouped_df['region'] == selected_region]
    fig = px.line(
        filtered_df, 
        x='year', 
        y='BEV/EV_sales', 
        title=f'Share of New Electric Cars Sold in {selected_region}',
        labels={'year':'Year','BEV/EV_sales':'Share of new electric cars sold'}
    )
    fig.update_layout(
        xaxis_title='',
        yaxis_title='',
        yaxis=dict(tickformat='0.0%')
    )
    return fig