import plotly.express as px

def create_plot10(df,selected_year):
    # Filter the dataset
    bool_columns = df.select_dtypes(include=['bool']).columns
    filtered_df = df.loc[(df[bool_columns] == True).any(axis=1)]
    filtered_df = filtered_df[['year','value', 'unit'] + list(bool_columns)]
    # convert 'unit' column to categorical codes for numerical analysis
    filtered_df['unit'] = filtered_df['unit'].astype('category').cat.codes

    # Define feature name replacements
    feature_name_map = {
        'unit': 'Unit',
        'parameter_EV sales':'EV sales',
        'parameter_EV sales share':'EV sales share',
        'parameter_EV stock':'EV stock ',
        'parameter_EV stock share':'EV stock share ',
        'parameter_Electricity demand':'Electricity demand',
        'parameter_Oil displacement Mbd':'Oil displacement Mbd',
        'parameter_Oil displacement, million lge':'Oil displacement, million lge',
        'powertrain_BEV':'BEV powertrain',
        'powertrain_EV':'EV powertrain',
        'powertrain_FCEV':'FCEV powertrain',
        'powertrain_PHEV':'PHEV powertrain'

    }

    # filter data for selected year and compute correlation matrix
    year_data = filtered_df[filtered_df['year'] == selected_year]
    relevant_features = ['unit','parameter_EV sales','parameter_EV sales share',
                         'parameter_EV stock','parameter_EV stock share','parameter_Electricity demand',
                         'parameter_Oil displacement Mbd','parameter_Oil displacement, million lge',
                         'powertrain_BEV','powertrain_EV','powertrain_FCEV','powertrain_PHEV']
    correlation_matrix = year_data[relevant_features].corr()
    renamed_matrix = correlation_matrix.rename(index=feature_name_map, columns=feature_name_map)

    # Create the plot
    fig=px.imshow(
            renamed_matrix,
            color_continuous_scale='Viridis',
            title=f'Correlation Matrix for {selected_year}',
            labels=dict(x='Features', y='Features', color='Correlation')
        )
    fig.update_xaxes(tickangle=90)
    fig.update_layout(
        title_x=0.5,
        title_pad=dict(t=5),
        xaxis_title='',
        yaxis_title='',
        font=dict(size=12),
    )

    return fig
