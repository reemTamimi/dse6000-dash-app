import plotly.express as px
import numpy as np
import pandas as pd

def create_plot8(df,selected_region):
    filtered_df = df[(df['parameter_EV stock'] == True)]
    grouped_df = filtered_df.groupby(['region', 'year'])['value'].sum().reset_index()

    # Create the plot
    filtered_df = grouped_df[grouped_df['region'] == selected_region]
    fig = px.line(
        filtered_df, 
        x='year', 
        y='value', 
        title=f'Electric Car Stocks in {selected_region}',
        labels={'year':'Year','value':'Number of electric car stocks'}
    )
    fig.update_layout(
        xaxis_title='',
        yaxis_title=''
    )
    return fig