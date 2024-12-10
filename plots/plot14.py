import plotly.express as px

def create_plot14(df,selected_region):
    # Filter the dataset
    filtered_df = df[(df['powertrain_EV'] == True) & (df['parameter_Oil displacement, million lge'] == True)]
    grouped_df = filtered_df.groupby(['region', 'year'])['value'].sum().reset_index()
    
    grouped_df['year_group'] = grouped_df['year'].apply(lambda x: f"{x // 2 * 2}s")
    # Create the plot
    filtered_df = grouped_df[grouped_df['region'] == selected_region]

    fig = px.histogram(
        filtered_df,
        x='year_group',
        y='value',
        title=f'Frequency of Oil Displacement (million lge) from EVs, by Year Groups of Two in {selected_region}',
        labels={'year_group': 'Year Group','value': 'Frequency of oil displacement (million lge)'},
        histfunc='sum', 
        barmode='group'
    )
    fig.update_layout(
        xaxis_title='',
        yaxis_title='',
        font=dict(size=12),
        bargap=0
    )

    return fig