import plotly.express as px
import pandas as pd

def create_correlation_figure(df, selected_stocks, start_date, end_date):
    """
    Create a correlation matrix figure for the selected stocks.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing stock data with columns for Tickers and their values.
        selected_stocks (list): List of tickers selected by the user.

    Returns:
        plotly.graph_objects.Figure: A correlation heatmap figure.
    """
    # Filter by date
    filtered_df_date = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    
    # Filter the dataset for the selected stocks
    filtered_df = filtered_df_date[filtered_df_date['Ticker'].isin(selected_stocks)]
    
    # Pivot the DataFrame to have stocks as columns
    pivoted_df = filtered_df.pivot(index='Date', columns='Ticker', values='Close')
    
    # Calculate the correlation matrix
    correlation_matrix = pivoted_df.corr().round(2)
    
    #Adjust figure size
    num_tickers = len(selected_stocks)
    fig_size = 300 + num_tickers * 50
    

    # Create the heatmap
    fig = px.imshow(
        correlation_matrix,
        text_auto=True,
        color_continuous_scale='Teal',
        title="Correlation Matrix of Selected Stocks",
        labels={'color': 'Correlation'},
    )
    
    # Update layout for dynamic sizing
    fig.update_layout(
        title="Correlation Heatmap",
        width=fig_size,
        height=fig_size,
        margin=dict(l=40, r=40, t=40, b=40)
    )
    
    return fig