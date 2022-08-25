# Inspecting Time Zones in Stock Data

## Background

You have an internship opportunity at a stock-trading fintech company in Germany. You feel excited about this opportunity to collaborate with a European company, so you accept the position.

This company is based in Berlin. They want to start offering investment opportunities in companies from the US that are disrupting the automotive industry. Your first project is to analyze Tesla Motors stock. After getting the historical stock data, you realize that the prices are based on Chicago time. So, you need to change the time zone to that of Berlin. It’s time to put your `datetime` transformation skills in action!

## Instructions

1. Read the Tesla historical stock data from the CSV file into a DataFrame.

2. Use the Pandas `head` function to inspect the data. Use the Pandas `info` function to check the data types of each column.

3. Convert the “time” column to the `datetime` data type by using the Pandas `to_datetime` function.

   **Hint:** Because the “time” column contains UTC `Timestamp` data, remember to set `utc=True`.

4. Use the Pandas `head` and `info` functions to verify both the data type transformation and the time zone.

5. Convert the time zone to that of Berlin (`Europe/Berlin`), and then verify the time zone transformation by using the Pandas `head` and `info` functions.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
