import plotly.express as px

def create_plot11(df,selected_region):
    # Filter the dataset
    filtered_df = df[(df['powertrain_PHEV'] == True) & (df['unit'] == 'Vehicles')]

    if selected_region is None:
        return px.pie(title='Select a Region to Display cars using PHEV powertrain')


    # Create the plot
    filtered_df = filtered_df[filtered_df['region'] == selected_region]
    fig = px.pie(
        filtered_df,
        names='year',
        values='value',
        title=f'Number of Plug-In Hybrid Cars, by Year in {selected_region}',
        color_discrete_sequence=px.colors.sequential.Viridis,
        labels={'year':'Year','value':'Number of plug-in hybrid cars'}

    )
    return fig
