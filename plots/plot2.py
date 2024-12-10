import plotly.express as px

def create_plot2(df,selected_year):
    # Filter the dataset
    filtered_df = df[(df['parameter_EV sales share'] == True) & (df['powertrain_EV'] == True)]
    # Scale the 'value' column to a decimal format
    filtered_df.loc[:, 'value'] = filtered_df['value'] / 100
    grouped_df = filtered_df.groupby(['region', 'year'])['value'].sum().reset_index()

    # Create the plot
    filtered_df = grouped_df[grouped_df['year'] == selected_year]
    fig = px.bar(
        filtered_df, 
        x='region', 
        y='value', 
        title=f'Share of New Electric Cars Sold in {selected_year}',
        labels={'year':'Year', 'value':'Share of new electric cars sold'}
    )
    fig.update_layout(
        xaxis_title='',
        yaxis_title='',
        yaxis=dict(tickformat='0.0%')
    )
    return fig