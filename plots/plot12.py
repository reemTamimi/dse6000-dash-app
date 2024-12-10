import plotly.express as px

def create_plot12(df,selected_year):
    # Filter the dataset
    filtered_df = df[df['parameter_Oil displacement Mbd'] == True]
    # Group data by country and year, summing the 'unit' column
    grouped_df = filtered_df.groupby(['region', 'year'])['value'].sum().reset_index()


    # Create the plot
    filtered_df = grouped_df[grouped_df['year'] == selected_year]
    fig = px.scatter(
        filtered_df, 
        x='region', 
        y='value', 
        color='region',
        title=f"Oil Displacement (Mbd) by Region in {selected_year}",
        labels={'region':'Region','value':'Oil Displacement (Mbd)'}
    )
    fig.update_xaxes(tickangle=45)
    fig.update_layout(
        xaxis_title='',
        yaxis_title='',
        font=dict(size=12),
    )

    return fig
