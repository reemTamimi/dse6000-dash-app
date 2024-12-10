import plotly.express as px

def create_plot3(df,selected_region):
    # Filter the dataset
    filtered_df = df[df['parameter_EV sales'] == True]
    grouped_df = filtered_df.groupby(['region', 'year', 'powertrain'])['value'].sum().reset_index()

    # Create the plot
    filtered_df = grouped_df[grouped_df['region'] == selected_region]
    # Create the choropleth map
    fig = px.bar(
        filtered_df, 
        x='year', 
        y='value', 
        color='powertrain', 
        title=f'Number of New Electric Cars Sold in {selected_region}',
        labels={'year':'Year', 'value':'Number of new electric cars sold', 'powertrain': 'Powertrain Type'},
    )
    # update legend names
    fig.for_each_trace(lambda t: t.update(name=t.name.replace('BEV', 'Battery-Electric')
                                      .replace('PHEV', 'Plug-in Hybrid')
                                      .replace('FCEV', 'Fuel Cell Electric')))
    fig.update_layout(
        xaxis_title='',
        yaxis_title='',
        legend=dict(
            title=None,
            x=0,  
            y=1, 
            xanchor='left',  
            yanchor='top'
        )
    )
    return fig