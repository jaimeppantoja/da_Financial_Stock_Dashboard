# Financial Data Dashboard

## Introduction

This project focuses on developing a **financial data dashboard** that empowers users with detailed insights into stock market trends and financial metrics. The dashboard is designed to provide a comprehensive view of price movements, correlations, and variations across selected stocks and a stock index. Additionally, it offers an integrated news feed that provides contextual information about the companies being analyzed. The dashboard can be accessed via [https://jaimepantoja.pythonanywhere.com/].

The project architecture employs a modular approach, dividing the functionality into dedicated directories for different components. For example, data processing functions are housed in separate modules, allowing the callback functions in the Dash app to access specialized capabilities such as creating visualizations and retrieving news. The key steps in handling data and creating the dashboard include:

### Data Collection and Processing
- Financial data is collected, transformed, and analyzed using **Pandas**, which enables efficient manipulation of stock prices and related metrics.
- News data is fetched and displayed alongside the visualizations to provide market context.

### Visualization Creation
- **Line Charts**: Used to depict the evolution of prices for individual stocks and to compare them against a stock index over time.  
- **Correlation Tables**: Created to explore relationships between different stock tickers, providing insights into how their prices move relative to each other.  
- **Clustered Bar Charts**: Designed to visualize the variation in stock prices, showing percentage changes across multiple tickers for easy comparison.

### Dashboard Development
- The dashboard was built using **Dash**, a Python framework that enables interactive web-based applications, while **Plotly** was utilized to generate visually engaging and responsive charts.

This modular design ensures that the app is both extensible and maintainable, allowing for additional features to be incorporated in the future.

---

## Key Focus Areas of the Dashboard

This type of dashboard provides valuable insights to various audiences, including investors, financial analysts, and market enthusiasts. The main areas of focus include:

### Trend Analysis
- Visualize the evolution of stock prices over time to identify patterns, trends, and anomalies.  
- Compare individual stock performance against broader market indices to gauge relative strength.  

### Correlation Insights
- Understand how different stocks are interrelated, aiding in portfolio diversification strategies.  
- Identify clusters of stocks with strong positive or negative correlations for hedging or speculative purposes.  

### Performance Variations
- Highlight short-term and long-term changes in stock prices across multiple tickers, helping users spot high-performing or underperforming assets.  

### Market Context via News Integration
- Provide users with timely, relevant news about specific companies, enriching their understanding of the factors influencing stock performance.  

### Customizable Visualizations
- Enable users to select specific tickers and metrics, tailoring the dashboard to their individual interests and investment strategies.

By combining these focus areas, the dashboard serves as a powerful tool for making data-driven decisions, whether for day-to-day trading or long-term investment planning.
