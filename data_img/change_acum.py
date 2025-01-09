import plotly.graph_objects as go

def create_acum_chart(df, selected_tickers):
    # Create the figure
    fig = go.Figure()

    # Add a trace for each selected stock ticker
    for ticker in selected_tickers:
        stock_data = df[df['Ticker'] == ticker]
        fig.add_trace(go.Scatter(
            x=stock_data['Date'],
            y=stock_data['Normalized'],
            mode='lines',
            name=ticker
        ))

    # Add the index (SPY) data to the chart
    index_data = df[df['Ticker'] == 'SPY']
    fig.add_trace(go.Scatter(
        x=index_data['Date'],
        y=index_data['Normalized'],
        mode='lines',
        name='SPY',
        line=dict(color='green', dash='dot')  # Different style for SPY
    ))

    # Update layout for better visualization
    fig.update_layout(
        template='plotly_white',
        title="Comparison of Selected Stocks with SPY",
        xaxis=dict(
            title="Date",
            showgrid=False,
            showline=True,
            linecolor='black',),
        yaxis=dict(
            title="Normalized Performance (Week by Week)",
            showgrid=False,
            showline=True,
            linecolor='black',
        ),
        legend=dict(x=0.1, y=1.1, orientation="h")
    )

    return fig
