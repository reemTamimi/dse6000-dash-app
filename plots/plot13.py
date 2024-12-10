import plotly.express as px
import plotly.graph_objs as go

def create_plot13(df,selected_region):
    filtered_df = df[df['parameter_Electricity demand'] == True]
    # Group data by 'year' and 'region' to get the total values for Sankey
    grouped_df = filtered_df.groupby(['year', 'region']).agg({'value': 'sum'}).reset_index()

    if selected_region == 'All Regions':
        filtered_df = grouped_df
    else:
        filtered_df = grouped_df[grouped_df['region'] == selected_region]
 
    # Create Sankey diagram nodes and links
    nodes = list(set(filtered_df['year'].unique()) | set(filtered_df['region'].unique()))
    node_index = {node: i for i, node in enumerate(nodes)}
 
    links = []
    for index, row in filtered_df.iterrows():
        source = node_index[row['year']]
        target = node_index[row['region']]
        value = row['value']
        links.append({'source': source, 'target': target, 'value': value})
 
    fig = go.Figure(data=[go.Sankey(
        node = dict(
            pad = 15,
            thickness = 20,
            line = dict(color = "black", width = 0.5),
            label = nodes,
            color = "blue"
        ),
        link = dict(
            source = [link['source'] for link in links],
            target = [link['target'] for link in links],
            value = [link['value'] for link in links]
        ))])
 
    fig.update_layout(title_text="Electricity Demand Flow by Region", font_size=10)
    return fig