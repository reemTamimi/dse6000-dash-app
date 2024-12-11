import pandas as pd
import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from plots.plot1 import create_plot1
from plots.plot2 import create_plot2
from plots.plot3 import create_plot3
from plots.plot4 import create_plot4
from plots.plot5 import create_plot5
from plots.plot6 import create_plot6
from plots.plot7 import create_plot7
from plots.plot8 import create_plot8
from plots.plot9 import create_plot9
from plots.plot10 import create_plot10
from plots.plot11 import create_plot11
from plots.plot12 import create_plot12
from plots.plot13 import create_plot13
from plots.plot14 import create_plot14
from plots.plot15 import create_plot15

# reading cleaned dataset
df=pd.read_csv('data/IEA-EV-dataEV salesHistoricalCars_Cleaned.csv')
ml_df=pd.read_csv('data/ML_Predictions.csv')

app = dash.Dash(__name__)
server = app.server

# Pass the dataset to the plot functions
app.layout = html.Div([

    html.H1('Exploring and Analyzing Electric Vehicle Sales and Stocks', className='title-box'),
   
    html.P('''Electric vehicles (EVs) run on rechargeable batteries, producing zero tailpipe emissions. 
           They are gaining popularity due to their environmental benefits and advancements in battery technology.''',className='text-style'),
    html.P(['In this dashboard, we observe various historical and projected data on EV sales and stock around the world. This data comes from the ',
           html.A("International Energy Agency", href='https://www.iea.org/data-and-statistics/data-tools/global-ev-data-explorer', target='_blank'),           
           ' data explorer.'],className='text-style'),
    
    html.P('In this dashboard, all charts refer to electric cars as fully battery-electric vehicles and plug-in hybrids.',className='text-style'),
    
    html.H2('Exploratory Data Analysis', className='h2-style'),
    html.P('In this section, we perform basic exploratory data analysis (EDA) for a better understanding of the dataset.',className='text-style'),
    html.P('''In most regions, the total number of automobiles sold over the decade from 2010 to 2020 is 
           either comparable to or lower than the total sales achieved in just the three years between 2021 
           and 2023. This stark difference highlights a significant acceleration in electric vehicle (EV) 
           adoption in recent years. The data underscores a rapidly growing shift in consumer preferences toward EVs, 
           driven by technological advancements, increased environmental awareness, and supportive government policies.''',className='text-style'),
    html.Div(
        [

            dcc.Dropdown(
                id='region-dropdown1',
                options=[{'label': i, 'value': i} for i in df['region'].unique()],
                value='USA',
                className='dropdown-style'  
            ),
            dcc.Graph(id='plot1', className='graph-style'),
        ],
        className='graph-container'
    ),
    html.P('''The sales share shows a clear upward trend over the years, reflecting increasing 
           adoption and market growth. Among all regions, Norway consistently achieves the highest sales share, 
           showcasing its leadership in this domain. This sustained performance highlights Norway's strong 
           policies and infrastructure supporting the trend.''',className='text-style'),
    html.Div(
        [
            dcc.Dropdown(
                id='year-dropdown2',
                options=[{'label': i, 'value': i} for i in df['year'].unique()],
                value=2023,
                className='dropdown-style' 
            ),
            dcc.Graph(id='plot2', className='graph-style'),
        ],
        className='graph-container'
    ),
    html.P('''In every region, Plug-in Hybrid Electric Vehicles (PHEVs) account for approximately 10% of 
           Battery Electric Vehicle (BEV) sales, while Fuel Cell Electric Vehicles (FCEVs) consistently record 
           the lowest sales. Despite sales increasing across all vehicle types each year, BEVs dominate the 
           market with a substantial lead. This trend highlights the overwhelming preference for BEVs over other 
           alternatives in the growing electric vehicle sector.''',className='text-style'),
    html.H3('Fully-electric cars vs plug-in hybrids', className='H3-style'),
    html.Div(
        [
            dcc.Dropdown(
                id='region-dropdown3',
                options=[{'label': i, 'value': i} for i in df['region'].unique()],
                value='USA',
                className='dropdown-style'  
            ),
            dcc.Graph(id='plot3', className='graph-style'),
        ],
        className='graph-container'
    ),
    html.P('''In this dataset, the term "electric cars" has a lot of meanings, but mostly refers to fully
           battery-electric or plug-in hybrid vehicles. This graph below shows the share of new electric cars sold 
           that are fully-battery electric. There is a general increase across regions and over the years, with occasional dips.''',className='text-style'),
    html.Div(
        [
            dcc.Dropdown(
                id='region-dropdown4',
                options=[{'label': i, 'value': i} for i in df['region'].unique()],
                value='USA',
                className='dropdown-style'  
            ),
            dcc.Graph(id='plot4', className='graph-style'),
        ],
        className='graph-container'
    ),
    html.P('''China leads global EV sales, being the only country to surpass double-digit millions. 
           This highlights its dominance through strong policies and adoption. Meanwhile, North America 
           and Europe are rapidly implementing EVs on a large scale, marking significant strides in transportation sector.''',className='text-style'),
    html.Div(
        [
            dcc.RangeSlider(
                id='year_slider5',
                min=df['year'].min(),
                max=df['year'].max(),
                value=[df['year'].min(), df['year'].max()],
                marks={str(year): {'label':str(year), 'style': {'font-size': '16px'}} for year in df['year'].unique()},
            ),
            dcc.Graph(id='plot5', className='graph-style'),
        ],
        className='graph-container'
    ),
    html.P('''From the dataset, we were able to calculate the number of cars sold each year, separated by type - 
           non-electric and electric cars. As expected, there is a global increase of electric car sales in recent
           years. However, there is still a majority of non-electric cars sold.''',className='text-style'),
    html.Div(
        [
            dcc.Dropdown(
                id='region-dropdown6',
                options=[{'label': i, 'value': i} for i in df['region'].unique()],
                value='USA', 
                className='dropdown-style'  
            ),
            dcc.Graph(id='plot6', className='graph-style'),
        ],
        className='graph-container'
    ),
    html.P('''Stock values represent the total number of cars in use. Since people keep cars for years, 
           changes in new sales take time to impact stocks. As a result, the share of electric cars on 
           the road is much lower than their share of new car sales. The chart below shows the share of 
           electric cars in use.''',className='text-style'),
    html.Div(
        [
            dcc.Dropdown(
                id='region-dropdown7',
                options=[{'label': i, 'value': i} for i in df['region'].unique()],
                value='USA',
                className='dropdown-style'  
            ),
            dcc.Graph(id='plot7', className='graph-style'),
        ],
        className='graph-container'
    ),
    html.P('''The number of electric cars on the road represents the total sales over the years, minus 
           those no longer in use. The chart below shows the global total of electric car stocks, which 
           has grown rapidly since 2022.''',className='text-style'),
    html.Div(
        [ 
            dcc.Dropdown(
                id='region-dropdown8',
                options=[{'label': i, 'value': i} for i in df['region'].unique()],
                value='USA',
                className='dropdown-style'   
            ),
            dcc.Graph(id='plot8', className='graph-style')
        ],
        className='graph-container'
    ),
    html.P('''This is a violin plot, a data visualization tool that is used to visualize distribution of the dataset
            and its density. Here, the above plot displays the number of Electrical vehicles stocked in different years
            and at different regions. As we can see, the EV stock was adopted in small scale all across the world during
            the year 2010 which is why the violin plot shows minimal variation, but in year 2023, the violin plot is wider
            and spans broader range, reflecting a significant growth in EV adaptation. This growth could be attributed to 
            the spread of awareness about EV concept and technological advancements and an increased focus on reducing carbon
            emissions.''',className='text-style'),
    html.Div(
        [ 
            dcc.Dropdown(
                id='region-dropdown9',
                options=[{'label': i, 'value': i} for i in df['region'].unique()],
                value='USA',
                className='dropdown-style'   
            ),
            dcc.Dropdown(
                id='year-dropdown9',
                options=[{'label': i, 'value': i} for i in df['year'].unique()],
                value=2023,
                className='dropdown-style'   
            ),
            dcc.Graph(id='plot9', className='graph-style')
        ],
        className='graph-container'
    ),
    html.P('''Below is a correlation matrix, a table that is used to identify the relationship and dependencies
            between different variables. The major correlation changes that can be observed in this table from
            year 2010 to 2024 are, increase in correlation strenght between parameters because the EV market matured
            and their sales, stocks and other factors improved, reduced noise in data due to improved data consistancy
            and maturity in EV markets, powertrain differentiation between specific powertrain types have become clearer
            indicating an increase in specializations and distinct market behaviour of these technologies. The shift in 
            the correlation matrix from 2010 to 2023 reflects the transition from an emerging technology to an integrated
            and influential component of global energy and transportation systems.''',className='text-style'),
    html.Div(
        [ 
            dcc.Dropdown(
                id='year-dropdown10',
                options=[{'label': i, 'value': i} for i in df['year'].unique()],
                value=2023,
                className='corr-dropdown-style'   
            ),
            dcc.Graph(id='plot10', className='graph-style')
        ],
        className='corr-graph-container'
    ),
    html.P('''This is a pie chart that displays the growth of PHEV (Plug-in Hybrid Electric Vehicles) powertrain adaptation
            all across the world. As we can see the PHEV adaptation grew exponentially from 2010 to 2024. The chart displays
            how negligible the PHEV adaptation was in 2010, indicating the infancy stage of PHEV. But in 2024 the PHEV has
            become a mainstream niche for sustainable automobiles. This trend reflects the increasing importance of hybrid
            and electric vehicles in mitigating environmental concerns and reducing carbon emissions.''',className='text-style'),
    html.Div(
        [ 
            dcc.Dropdown(
                id='region-dropdown11',
                options=[{'label': i, 'value': i} for i in df['region'].unique()],
                value='USA',
                className='dropdown-style'   
            ),
            dcc.Graph(id='plot11', className='graph-style')
        ],
        className='graph-container'
    ),
    html.P('''Oil displacement measures how much oil consumption is avoided by using alternative energy sources,
           in this case EVs. This chart displays the measure in million barrels a day. China takes the lead, 
           however it is still a large number when measured globally.''',className='text-style'),
    html.Div(
        [ 
            dcc.Dropdown(
                id='year-dropdown12',
                options=[{'label': i, 'value': i} for i in df['year'].unique()],
                value=2023,
                className='dropdown-style'   
            ),
            dcc.Graph(id='plot12', className='graph-style')
        ],
        className='graph-container'
    ),
    html.P('''As the number of EVs on the road increases, the demand for electricity to power these vehicles
           also grows. The graph below portrays the rise in electricity demand corresponding to the rise in 
           EVs from 2010-2023.''',className='text-style'),
    html.Div(
        [ 
            dcc.Dropdown(
                id='region-dropdown13',
                options=[{'label': i, 'value': i} for i in df[df['parameter_Electricity demand'] == True]['region'].unique()],
                value='USA',
                className='dropdown-style'   
            ),
            dcc.Graph(id='plot13', className='graph-style')
        ],
        className='graph-container'
    ),
    html.P('''There is a common trend across multiple regions and globally - that is the number of oil displacement 
           (in units million liters of gasoline equivalent) basically doubles just from the year ranges 2020-2021 and
           2022-2023. This indicates a decrease in the volume of oil/gasoline that is avoided by using alternative 
           energy sources, in this case EVs.''',className='text-style'),
    html.Div(
        [ 
            dcc.Dropdown(
                id='region-dropdown14',
                options=[{'label': i, 'value': i} for i in df[(df['powertrain_EV'] == True) & (df['parameter_Oil displacement, million lge'] == True)]['region'].unique()],
                value='USA',
                className='dropdown-style'   
            ),
            dcc.Graph(id='plot14', className='graph-style')
        ],
        className='graph-container'
    ),
    html.H2('Projections', className='h2-style'),
    html.P('''We created a few machine learning models looking at all parameters from our EV data. We analyzed 
           linear regression (LR), random forest (RF), and XGBoost (XGB) models and compared them to 
           the actual data. What can be observed is that the random forest and XGBoost models were more accurate than 
           the linear regression model.''',className='text-style'),
    html.Div(
        [ 
            html.Label("Select Category:"),
            dcc.Checklist(
                id='category-checklist15',
                options=[
                    {'label': 'Historical', 'value': 'Historical'},
                    {'label': 'Projection-STEPS', 'value': 'Projection-STEPS'}
                ],
                value=['Historical'],  # Default selection
                inline=True
            ),

            # Dropdown for Parameter
            html.Label("Select Parameter:"),
            dcc.Dropdown(
                id='parameter-dropdown15',
                options=[{'label': param, 'value': param} for param in ml_df['parameter'].unique()],
                value=ml_df['parameter'].unique()[0]
            ),

            # Dropdown for Region
            html.Label("Select Region:"),
            dcc.Dropdown(
                id='region-dropdown15',
                options=[{'label': region, 'value': region} for region in ml_df['region'].unique()],
                value=ml_df['region'].unique()[0]
            ),

            # Checklist for Model Predictions
            html.Label("Select Predictions to Display:"),
            dcc.Checklist(
                id='model-checklist15',
                options=[
                    {'label': 'Linear Regression', 'value': 'Linear_Prediction'},
                    {'label': 'Random Forest', 'value': 'RF_Prediction'},
                    {'label': 'XGBoost', 'value': 'XGB_Prediction'}
                ],
                value=['Linear_Prediction'],  # Default selection
                inline=True
            ),
            dcc.Graph(id='plot15', className='graph-style')
        ],
        className='graph-container'
    ),
],
className='full-container')
# callback and update each plot sequentially
@app.callback(
    Output('plot1', 'figure'),
    Input('region-dropdown1', 'value')
)
def update_plot(selected_region):
    return create_plot1(df, selected_region)

@app.callback(
    Output('plot2', 'figure'),
    Input('year-dropdown2', 'value')
)
def update_plot(selected_year):
    return create_plot2(df, selected_year)

@app.callback(
    Output('plot3', 'figure'),
    Input('region-dropdown3', 'value')
)
def update_plot(selected_region):
    return create_plot3(df, selected_region)

@app.callback(
    Output('plot4', 'figure'),
    Input('region-dropdown4', 'value')
)
def update_plot(selected_region):
    return create_plot4(df, selected_region)

@app.callback(
    Output('plot5', 'figure'),
    Input('year_slider5', 'value')
)
def update_plot(year_range):
    return create_plot5(df, year_range)

@app.callback(
    Output('plot6', 'figure'),
    Input('region-dropdown6', 'value')
)
def update_plot(selected_region):
    return create_plot6(df, selected_region)

@app.callback(
    Output('plot7', 'figure'),
    Input('region-dropdown7', 'value')
)
def update_plot(selected_region):
    return create_plot7(df, selected_region)

@app.callback(
    Output('plot8', 'figure'),
    Input('region-dropdown8', 'value')
)
def update_plot(selected_region):
    return create_plot8(df, selected_region)

@app.callback(
    Output('plot9', 'figure'),
    [Input('region-dropdown9', 'value'),
     Input('year-dropdown9', 'value')]
)
def update_plot(selected_region, selected_year):
    return create_plot9(df, selected_region, selected_year)

@app.callback(
    Output('plot10', 'figure'),
    Input('year-dropdown10', 'value')
)
def update_plot(selected_year):
    return create_plot10(df, selected_year)

@app.callback(
    Output('plot11', 'figure'),
    Input('region-dropdown11', 'value')
)
def update_plot(selected_region):
    return create_plot11(df, selected_region)

@app.callback(
    Output('plot12', 'figure'),
    Input('year-dropdown12', 'value')
)
def update_plot(selected_year):
    return create_plot12(df, selected_year)

@app.callback(
    Output('plot13', 'figure'),
    Input('region-dropdown13', 'value')
)
def update_plot(selected_region):
    return create_plot13(df, selected_region)

@app.callback(
    Output('plot14', 'figure'),
    Input('region-dropdown14', 'value')
)
def update_plot(selected_region):
    return create_plot14(df, selected_region)

@app.callback(
    Output('plot15', 'figure'),
    Input('category-checklist15', 'value'),
    Input('parameter-dropdown15', 'value'),
    Input('region-dropdown15', 'value'),
    Input('model-checklist15', 'value')
)
def update_plot(selected_categories, selected_parameter, selected_region, selected_models):
    return create_plot15(ml_df, selected_categories, selected_parameter, selected_region, selected_models)

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
