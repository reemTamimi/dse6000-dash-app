import plotly.graph_objects as go

def create_plot15(ml_df,selected_region):
    # Filter the dataset
    filtered_df = ml_df[(ml_df['mode'] == 'Cars') & 
                  ((ml_df['parameter_EV sales'] == True) | (ml_df['powertrain_BEV'] == True))]
    # Scale the 'value' column to a decimal format
    grouped_df = filtered_df.groupby(['region', 'year'])[['value', 'pred_lin_reg', 'pred_rf_reg','pred_xgb_reg']].sum().reset_index()

    # Create the plot
    filtered_df = grouped_df[grouped_df['region'] == selected_region]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_df['year'], y=filtered_df['value'], mode='lines', name='Actual'))
    fig.add_trace(go.Scatter(x=filtered_df['year'], y=filtered_df['pred_lin_reg'], mode='lines', name='Predicted LR'))
    fig.add_trace(go.Scatter(x=filtered_df['year'], y=filtered_df['pred_rf_reg'], mode='lines', name='Predicted RF'))
    fig.add_trace(go.Scatter(x=filtered_df['year'], y=filtered_df['pred_xgb_reg'], mode='lines', name='Predicted XGB'))


    fig.update_layout(
        title=f'Predictions of EV Sales by Year in {selected_region}',
        xaxis_title='',
        yaxis_title=''
    )
    return fig
