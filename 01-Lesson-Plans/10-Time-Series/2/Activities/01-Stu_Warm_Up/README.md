# Time Series Warm-Up

Let’s warm up by using some code from the previous class in order to visualize hourly patterns in the price and volume of Bitcoin.

## Instructions

Using the starter file, complete the following steps. Note that Steps 1 and 2 are completed already in the starter code.

1. Import the required libraries and dependencies.

2. Read in the `bitcoin_hourly` CSV file and prepare the data.

3. Plot the volume in a line plot by using `hvplot` to get a sense of the typical volume for the cryptocurrency.

4. Use Pandas `groupby` and the `weekofyear` function on the `datetime` index to create a `hvplot` bar plot of the data.

   **Hint:** Use `kind='bar'` as a parameter in the hvPlot function.

5. Similarly, group by the `datetime` index hour, and plot average prices and volume by hour, for each of the 24 hours in a day.

6. Determine whether tweets about Bitcoin by Elon Musk have moved the market.

   - Using datetime indexing, slice the volume and price DataFrame to one day before and after Jan 29, 2021, when Elon Musk added the hashtag #bitcoin to his Twitter bio.

   - Did Musk's posts appear to move the market for the cryptocurrency? If so, did it move prices, or just volume?

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
