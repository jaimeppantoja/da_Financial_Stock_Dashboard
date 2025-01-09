# functions.py 

import plotly.graph_objects as go

def create_comparison_chart(df, selected_ticker):
    # Filter data for the selected ticker and the index
    stock_data = df[df['Ticker'] == selected_ticker]
    index_data = df[df['Ticker'] == 'SPY']

    # Create the figure
    fig = go.Figure()

    # Add stock data to the primary y-axis
    fig.add_trace(go.Scatter(
        x=stock_data['Date'],
        y=stock_data['Close'],
        mode='lines',
        name=selected_ticker,
        line=dict(color='blue')
    ))

    # Add index data to the secondary y-axis
    fig.add_trace(go.Scatter(
        x=index_data['Date'],
        y=index_data['Close'],
        mode='lines',
        name='SPY',
        line=dict(color='green'),
        yaxis='y2'
    ))

    # Update layout for secondary y-axis
    
    fig.update_layout(       
        template='plotly_white',
        xaxis=dict(
            showgrid=False,
            showline=True,
            linecolor='black',
            title="Date"
        ),
        yaxis=dict(
            showgrid=False,
            showline=True,
            linecolor='black',
            title=f"{selected_ticker} Closing Price",
            titlefont=dict(color="blue"),
            tickfont=dict(color="blue")
        ),
        yaxis2=dict(
            showgrid=False,
            showline=True,
            linecolor='black',
            title="SPY Closing Price",
            titlefont=dict(color="green"),
            tickfont=dict(color="green"),
            anchor="x",
            overlaying="y",
            side="right"
        ),
        title=f"Comparison of {selected_ticker} with SPY - Closing Prices",
        legend=dict(x=0.1, y=1.1, orientation="h")
    )

   

    return fig
