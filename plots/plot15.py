import plotly.graph_objects as go

def create_plot15(ml_df,selected_categories, selected_parameter, selected_region, selected_models):
    # Filter the dataset
    filtered_df = ml_df[
        (ml_df['category'].isin(selected_categories)) &
        (ml_df['parameter'] == selected_parameter) &
        (ml_df['region'] == selected_region)
    ]
    
    # Get all unique years to ensure the x-axis covers the full range
    all_years = sorted(ml_df['year'].unique())

    # Create the figure
    fig = go.Figure()

    # Add actual values to the graph
    for category in selected_categories:
        category_data = filtered_df[filtered_df['category'] == category]
        fig.add_trace(go.Scatter(
            x=category_data['year'],
            y=category_data['value'],
            mode='lines+markers',
            name=f'Actual ({category})'
        ))

    # Add predictions for selected models
    for model in selected_models:
        if model in filtered_df.columns:
            prediction_data = filtered_df[['year', model]].drop_duplicates()
            fig.add_trace(go.Scatter(
                x=prediction_data['year'],
                y=prediction_data[model],
                mode='lines',
                name=f'Prediction ({model.split("_")[0]})'
            ))

    # Update layout to include all years on the x-axis
    fig.update_layout(
        title=f"{selected_parameter} over Year in {selected_region}",
        xaxis=dict(
            title='Year',
            tickmode='linear',
            range=[min(all_years), max(all_years)]
        ),
        yaxis_title='Value',
        legend_title='Legend'
    )

    return fig
