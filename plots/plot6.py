import plotly.express as px

def create_plot6(df,selected_region):
    bev_phev_sales = df[
        (df['parameter_EV sales'] == True) & 
        ((df['powertrain_BEV'] == True) | (df['powertrain_PHEV'] == True))
        ].groupby(['region', 'year'])['value'].sum()
    df['BEV_PHEV_sales'] = df.set_index(['region', 'year']).index.map(bev_phev_sales)
    ev_sales_share = df[df['parameter_EV sales share'] == True].groupby(['region', 'year'])['value'].sum()
    total_sales = bev_phev_sales/(ev_sales_share/100) # Normalize within each year
    df['total_sales'] = df.set_index(['region', 'year']).index.map(total_sales)
    df['non_EV_sales'] = df['total_sales'] - df['BEV_PHEV_sales']

    # Filter the dataset
    filtered_df = df[(df['parameter_EV sales share'] == True)]
    # transform into single DF for EV and non-EV sales
    combined_df = filtered_df[['region', 'year', 'non_EV_sales','BEV_PHEV_sales']].melt(
        id_vars=['region', 'year'],
        value_vars=['non_EV_sales', 'BEV_PHEV_sales'],
        var_name='sales_type',
        value_name='value'
        )

    # Create the plot
    filtered_df = combined_df[combined_df['region'] == selected_region]
    fig = px.bar(
        filtered_df, 
        x='year', 
        y='value', 
        color='sales_type', 
        title=f'Number of New Cars Sold, by Type, in {selected_region}',
        labels={'year':'Year', 'value':'Number of new cars sold', 'sales_type': 'Type'}
    )

    fig.for_each_trace(lambda t: t.update(name=t.name.replace('non_EV_sales', 'Non-electric cars')
                                      .replace('BEV_PHEV_sales', 'Electric cars')))
    
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