import plotly.express as px

def create_plot9(df,selected_region,selected_year):
    # Filter the dataset
    filtered_df = df[(df['parameter_EV stock'] == True) & (df['unit'] == 'Vehicles')]
    #grouped_df = filtered_df.groupby(['region', 'year'])['value'].sum().reset_index()

    # Create the plot
    filtered_df = filtered_df[(filtered_df['region'] == selected_region) &
                              (filtered_df['year'] == selected_year)]
    fig = px.violin(
        filtered_df,
        y='value',
        points='all',
        box=True,
        color_discrete_sequence=px.colors.qualitative.Pastel,
        title=f'Stock of New Electric Cars in {selected_region} for {selected_year}'
    )

    # Adding gridlines for better understanding of plot
    fig.update_layout(
        yaxis_title='',
        xaxis_visible=False,
        yaxis=dict(showgrid=True),
        title=dict(font_size=18),
        violingap=0.1,
    )

    return fig