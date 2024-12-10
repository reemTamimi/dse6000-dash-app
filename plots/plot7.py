import plotly.express as px

def create_plot7(df,selected_region):
    filtered_df = df[(df['parameter_EV stock share'] == True) & (df['powertrain_EV'] == True)]
    # Scale the 'value' column to a decimal format
    filtered_df.loc[:, 'value'] = filtered_df['value'] / 100
    grouped_df = filtered_df.groupby(['region', 'year'])['value'].sum().reset_index()

    # Create the plot
    filtered_df = grouped_df[grouped_df['region'] == selected_region]
    fig = px.line(
        filtered_df, 
        x='year', 
        y='value', 
        title=f'Share of Electric Cars in Use in {selected_region}',
        labels={'year':'Year','value':'Share of new electric cars sold'}
    )
    fig.update_layout(
        xaxis_title='',
        yaxis_title='',
        yaxis=dict(tickformat='0.0%')
    )
    
    return fig