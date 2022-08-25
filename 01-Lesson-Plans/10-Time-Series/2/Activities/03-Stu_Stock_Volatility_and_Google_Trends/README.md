# Stock Volatility and Google Trends

## Background

There’s no doubt that Apple is a globally recognized brand. Have you ever wondered if its fame impacts its stock price?

Nowadays, a novel approach to enriching a company’s assessment is to include an analysis of its social profiles. However, back in 2013, a multidisciplinary group of researchers from the United Kingdom and the United States presented an exciting approach to quantifying trading behavior in financial markets by using Google Trends.

In this activity, you’ll analyze how Google Trends might impact the revenue and volatility of Apple stock (AAPL).

You can read the original article, [Quantifying Trading Behavior in Financial Markets Using Google Trends](https://doi.org/10.1038/srep01684), which _Scientific Reports_ published in April 2013.

## Instructions

Do a time series analysis of Apple from October 2015 to October 2020. Evaluate if any predictable relationship exists among the Google Trends data, Apple’s stock price, and Apple’s volatility and return metrics. To do all of that, complete the steps in the following two sections.

### Set Up and Visualize the Data

1. Read the time series data into two Pandas DataFrames, `df_stock` and `df_trends`. Set the “date” column as the index for each of these DataFrames.

2. Concatenate the `df_stock` DataFrame to the `df_trends` DataFrame, creating a single DataFrame named `df_apple`.

3. Create a plot of the concatenated DataFrame by using hvPlot to visually analyze any trends and correlations. Do you observe any seasonal patterns?

   **Hint:** You might find it useful to refer to the [Apple Events page](https://www.apple.com/apple-events/) and the [Timeline of Apple Inc. products](https://en.wikipedia.org/wiki/Timeline_of_Apple_Inc._products) to spotlight moments over time that could have triggered a particular pattern.

### Build Time Trends

1. Note that on September 10, 2019, Apple organized an event where it presented the new iPhone 11 family, the Apple Watch Series 5, and a new iPad. This event gained worldwide attention.

2. Closely examine the data from March 1, 2019 to January 31, 2020.

3. Create a plot by using hvPlot, and then identify whether both time series indicate a common trend that might correspond to this narrative.

4. Before seeking any correlations between these time series, add columns to the `df_apple` DataFrame to analyze the impact of the Google Trends data on the weekly returns and stock volatility, as follows:

   - Use the Pandas `shift` function to add a new column that lags the Google Trends data by one period.

     **Hint:** Google Trends data is reported every week on Sunday, so you have a weekly period in this time series.

   - Use the Pandas `pct_change` function to add a new column that has the weekly price returns.

   - Compute the rolling stock volatility for Apple by using the following Pandas method:

     `df_apple["weekly_volatility"] = df_apple["close"].pct_change().rolling(window=4).std()`

5. Use the Pandas `corr` function to compute the correlations among the lagged Google Trends data, the price returns, and the stock volatility. Does any predictable relationship exist?

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
