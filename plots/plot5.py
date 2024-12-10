import plotly.express as px

def create_plot5(df,year_range):
    #year_range = (2010,2023)
    # Filter the dataset
    filtered_df = df[df['parameter_EV sales'] == True]
    grouped_df = filtered_df.groupby(['region', 'year'])['value'].sum().reset_index()
    # Create a pivot table to get total sales per country for each year
    pivot_df = grouped_df.pivot_table(index='region', columns='year', values='value')

    # Create the plot
    filtered_df = pivot_df.loc[:, year_range[0]:year_range[1]].sum(axis=1)

    fig = px.choropleth(
        locations=filtered_df.index,
        locationmode='country names',
        color=filtered_df.values,
        color_continuous_scale='Viridis',
        title=f'Number of New Electric Cars Sold in ({year_range[0]} - {year_range[1]})',
        labels={'color':'Number'}
    )

    return fig

 