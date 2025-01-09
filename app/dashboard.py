import sys
import os

#data_img directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../data_img')))

# Now you can import your modules
from change_acum import create_acum_chart
from get_news import fetch_company_news
from correlation_figure import create_correlation_figure
from variation_calc import calculate_variation
from closing_prices import create_comparison_chart

# Dash and Plotly imports
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go

# Data processing and analysis
import pandas as pd

# Load the data from a CSV file
data = pd.read_csv('final_df.csv')
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Time Slider auxiliar variables
date_range = sorted(df['Date'].unique())
date_marks = {i: date_range[i].strftime('%Y-%m-%d') for i in range(0, len(date_range), max(1, len(date_range) // 10))}


# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div(style={'margin': '10px 30px', 'background-color':'white'}, children=[
    
     html.H1("Stock Analysis Dashboard",                                     
                    style={ 'backgroundColor': '#03045e', # New blue background 
                        'color': '#ffffff', # White text color for better contrast 
                        'textAlign': 'center',
                        'margin':'10px 0px',
                        'padding':'30px 0px',
                        'min-width':'600px',},
                    ),
    
    html.Div(
        style={
            'display': 'flex',
            'flexWrap':'wrap',
            'justifyContent': 'space-around',  # Adjust spacing between the sections
            'alignItems': 'flex-start',  # Align items at the top
            'gap': '10px',  # Space between the sections
            'padding': '10px',  # Add some padding around the row 
            'boxSizing': 'border-box', 
            'min-width':'600px',
            'flex': '1 1 45%'      
        },
        
        children=[                     
                      
            # Section for the price comparison chart
            html.Div(className='container',
                     style={
                    #'flex': '1 1 45%',  # Allow this section to grow/shrink and take ~45% of the row
                    'flex': '1 ',
                    'boxSizing': 'border-box',  # Ensure proper padding calculation
                    'minWidth': '600px',
                    },                     
                     children=[
                
                html.H2("Stock Pick vs. S&P 500: A Comparative Analysis",
                    style={ 'backgroundColor': '#0077b6', # New blue background 
                        'color': '#ffffff', # White text color for better contrast 
                        'textAlign': 'center',
                        'margin':'10px 0px',
                        'padding':'20px'}),           
                
                # Dropdown list to select one stock
                dcc.Dropdown(
                    id='stock-dropdown-one',
                    options=[{'label': ticker, 'value': ticker} for ticker in df['Ticker'].unique()],
                    value='AAPL',  # Default value
                    placeholder="Select a Stock",
                    style={'width': '50%'}
                ),
                
                # Displays the price comparison chart
                dcc.Graph(id='price-comparison-chart')
            ]),
            
            # Section for latest company news
            html.Div(className='section', 
                     style={
                    #'flex': '1 1 auto',  # Allow this section to grow/shrink and take ~45% of the row
                    'flex': '1 ',
                    'boxSizing': 'border-box',  # Ensure proper padding calculation
                    'minWidth': '600px'
                    },
                     children=[ 
                html.H2(
                    #"Latest Company News",
                    id='news-title',
                    style={ 'backgroundColor': '#0077b6', # New blue background 
                        'color': '#ffffff', # White text color for better contrast 
                        'textAlign': 'center',
                        'margin':'10px 0px',
                        'padding':'20px',
                        'flex': '1 1 45%',
                        'boxSizing': 'border-box',
                        }), 
                html.Ul(id='news-list', className='news-list') 
            ]),
        ]
    ),

    # Section for the multiple stock comparison chart
    html.Div(className='section', 
             style={
                    'minWidth': '600px'
                    },
             children=[
        html.H2("Annual Growth Tracker",
            style={ 'backgroundColor': '#0077b6', # New blue background 
                   'color': '#ffffff', # White text color for better contrast 
                   'textAlign': 'center',
                   'margin':'10px 0px',
                   'padding':'20px', }),
        
        # Dropdown list to select multiple stocks
        dcc.Dropdown(
            id='stock-dropdown-two',
            options=[{'label': ticker, 'value': ticker} for ticker in df['Ticker'].unique()],
            value=['AAPL', 'MSFT', 'GOOGL'],  # Default values
            multi=True,  # Allow multiple selections
            placeholder="Select Stocks",
            style={'width': '50%'}
        ),
        
        # Display the comparison chart
        dcc.Graph(id='multiple-stock-comparison-chart')
    ]),
    
    # Section for illustrating the correlation matrix
    html.Div(className='section', 
             style={
                    'minWidth': '600px',
                    #'display': 'flex',
                    #'justifyContent':'center'
                    },
             children=[
        html.H2("Correlation Matrix",
            style={ 'backgroundColor': '#0077b6', # New blue background 
                   'color': '#ffffff', # White text color for better contrast 
                   'textAlign': 'center',
                   'margin':'10px 0px',
                   'padding':'20px'}),
               
        html.Div(
            style={'display': 'flex', 'flexDirection':'column',  'gap': '10px', 'width':'100%', 'marginTop':'10px'},
            children=[
                html.Div('Choose your desired time range and select the stock tickers to generate the correlation table',
                         style={'textAlign': 'left', 'margin':'10px'}),
                # Range slider
                html.Div(
                    dcc.RangeSlider(
                        id='date-range-slider',
                        min=0,
                        max=len(date_range) - 1,
                        step=1,
                        marks={i: date_marks[i] for i in range(0, len(date_range), len(date_range) // 10)},
                        value=[0, len(date_range) - 1],
                        tooltip={"placement": "bottom", "always_visible": False},  # Optional: Improves UX
                        
                    ),
                    style={'flex': '0 0 70%', 'maxWidth':'70%', 'margin':'10px'},  # Adjust slider width to occupy remaining space                     
                )      
            ]
        ),
        
        # Dropdown list
        dcc.Dropdown(
            id='correlation-dropdown',
            options=[{'label': ticker, 'value': ticker} for ticker in df['Ticker'].unique()],
            value=['AAPL', 'MSFT'],  # Default selected stocks
            multi=True,  # Allow multiple selections
            placeholder="Select Stocks for Correlation",
            style={'width': '50%'}    
        ),
        
        html.Div(
            dcc.Graph(id='correlation-figure'),
            style={
                    'display': 'flex',
                    'justifyContent':'center',
                    'margin':'10px'
                    }
        )          
    ]),
    
    html.Div(className='section', 
             style={
                    'minWidth': '600px',
                    
                    },
             children=[
        html.H1("Stock Price Variation",
            style={ 'backgroundColor': '#0077b6', # New blue background 
                   'color': '#ffffff', # White text color for better contrast 
                   'textAlign': 'center',
                   'margin':'10px 0px',
                   'padding':'20px'}),
        
        # Description
        html.Div('Specify the stock tickers and the time frame to generate the stock variation graph',
                         style={'textAlign': 'left', 'margin':'10px'}),
        
        # Dropdown for selecting stock
        dcc.Dropdown(
            id='stock-dropdown-variation',
            options=[{'label': ticker, 'value': ticker} for ticker in df['Ticker'].unique()],
            style={'width': '50%'},
            value=['AAPL', 'MSFT'],  # Default values
            multi=True,  # Allow multiple selections
            placeholder="Select Stocks"
        ),
        
        # Dropdown for selecting time frame
        dcc.Dropdown(
            id='timeframe-dropdown',
            options=[
                {'label': 'Monthly', 'value': 'monthly'},
                {'label': 'Quarterly', 'value': 'quarterly'},
                {'label': 'YTD', 'value': 'ytd'}
            ],
            value='monthly',  # Default time frame
            style={'width': '50%'}
        ),
        
        # Graph to display the change
        dcc.Graph(id='clustered-bar-chart')
    ])
        
])

# Callback for the price comparison chart
@app.callback(
    Output('price-comparison-chart', 'figure'),
    Input('stock-dropdown-one', 'value')
)
def update_price_comparison_chart(selected_ticker):
    if not selected_ticker:
        return {}
    return create_comparison_chart(df, selected_ticker)

# Callback for the multiple stock comparison chart
@app.callback(
    Output('multiple-stock-comparison-chart', 'figure'),
    Input('stock-dropdown-two', 'value')
)
def update_three_stock_comparison_chart(selected_tickers):
    if not selected_tickers:
        return {}
    return create_acum_chart(df, selected_tickers)

# Callback for fetching company news
@app.callback( 
    Output('news-list', 'children'),
    Input('stock-dropdown-one', 'value')
) 
def update_news_list(ticker_symbol):
    if ticker_symbol:
        try:
            news = fetch_company_news(ticker_symbol)
            return [
                html.Li([
                    f"{news_item.get('content', {}).get('title', 'No Title')} - ",
                    html.A(
                        "🔗 link", 
                        href=news_item.get('url', news_item.get('content', {}).get('canonicalUrl', {}).get('url', '#')), 
                        target="_blank"
                    )
                ])
                for news_item in news
            ]
        except Exception as e:
            return [html.Li(f"Error fetching news: {e}")]
    return []





# Callback title fetching news
@app.callback(
    Output('news-title', 'children'),
    Input('stock-dropdown-one', 'value'),
)
def update_news_title(selected_ticker):
          
    return f"Latest Company News: {selected_ticker}"

# Callback function to create the correlation graph.
@app.callback(
    Output('correlation-figure', 'figure'),
    [Input('correlation-dropdown', 'value'),
    Input('date-range-slider','value')]
)
def update_correlation_figure(selected_stocks, slider_range):  #start_date, end_date,
       
    start_date = date_range[slider_range[0]].strftime('%Y-%m-%d')
    end_date = date_range[slider_range[1]].strftime('%Y-%m-%d')
    
    return create_correlation_figure(df, selected_stocks, start_date, end_date)

# Callback function to create the cluster bar chart of the % variations over time
@app.callback(
    Output('clustered-bar-chart', 'figure'),
    [
        Input('stock-dropdown-variation', 'value'),
        Input('timeframe-dropdown', 'value')
    ]
)
def update_chart(selected_stocks, timeframe):
    # Retrieve data based on user selection
    df1 = calculate_variation(df, timeframe, selected_stocks)
    
    # Format the 'Date' column for the x-axis labels
    if timeframe == 'monthly':
        df1['Formatted Date'] = df1['Date'].dt.strftime('%B')  # Full month name
    elif timeframe == 'quarterly':
        df1['Formatted Date'] = df1['Date'].dt.to_period('Q').astype(str)  # Q1, Q2, etc.
    elif timeframe == 'ytd':
        df1['Formatted Date'] = df1['Date'].dt.year.astype(str)  # Year
    
    # Prepare data for the clustered bar chart
    dates = df1['Formatted Date']
    change_columns = [col for col in df1.columns if 'Change (%)' in col]
    
    # Create the figure
    fig = go.Figure()
    for col in change_columns:
        fig.add_trace(go.Bar(
            x=dates,
            y=df1[col],
            name=col.replace(' Change (%)', ''),  # Stock name without 'Change (%)'
        ))
    
    # Calculate positions for the edges of bar clusters
    cluster_edges = list(range(len(dates) + 1))
    vertical_lines = [
    dict(
        type="line",
        x0=edge - 0.5,  # Offset to align at the edge
        x1=edge - 0.5,  # Same x value for a vertical line
        y0=0,           # Start at the bottom of the y-axis
        y1=1,           # End at the top of the y-axis
        xref="x",       # Reference to x-axis
        yref="paper",   # Reference to the entire plot height
        line=dict(color="lightgrey", width=1, dash="dot"),  # Line style
    )
    for edge in cluster_edges
    ]
    
    # Update layout
    fig.update_layout(
        title=f"Stock Percentage Changes ({timeframe.capitalize()})",
        xaxis_title="Date",
        yaxis_title="Change (%)",
        barmode="group",
        xaxis=dict(
            tickmode='array',            
            tickvals=list(range(len(dates))),
            ticktext=dates,
            showgrid=False,
            showline=True,
            linecolor='black',            
        ),
        yaxis=dict(
            showgrid=False,
            showline=True,
            linecolor='black',
        ),
        shapes=vertical_lines,
        legend_title="Stocks",
        template="plotly_white"
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
