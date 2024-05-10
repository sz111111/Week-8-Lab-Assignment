# -*- coding: utf-8 -*-
"""
Created on Mon May  6 06:00:38 2024

@author: ChelseySSS
"""

# 1. Using Pandas DataReader, retrieve the average monthly closing stock
#prices of Tesla (TSLA) from January 1st 2019 to December 31st 2021.

#Hint: https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-alphavantage
#Hint: https://www.alphavantage.co/support/#api-key
#  Then use Pandas DataReader's interface for Alpha Vantage, not the
#  API that they describe on their site (DataReader does all that for
#  you!)

import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

# Set the start and end dates
start_date = datetime(2019, 1, 1)
end_date = datetime(2021, 12, 31)

# Use DataReader to fetch the basic daily stock prices with Alpha Vantage API key
tesla_data = web.DataReader('TSLA', 'av-daily', start_date, end_date, api_key='6WHSQ1M9ZCDJDGO8')

# Ensure the 'date' column is a datetime type and set it as the index
tesla_data.index = pd.to_datetime(tesla_data.index)

# Convert the 'close' column to float and calculate the average monthly closing prices
tesla_data['close'] = tesla_data['close'].astype(float)
monthly_average = tesla_data['close'].resample('M').mean()

# Display the results
print(monthly_average)




# 2. Create a new column that holds the rolling 3 month average.

# Convert the 'close' column to float
tesla_data['close'] = tesla_data['close'].astype(float)

# Calculate the average monthly closing prices
monthly_average = tesla_data['close'].resample('M').mean()

# Calculate the rolling 3-month average of the monthly closing prices
monthly_average['3_month_avg'] = monthly_average.rolling(window=3).mean()

# Display the results
print(monthly_average)




# 3. Create a new dataframe from the base data from part 1 that resamples
# the data to quarterly, using the mean value.

# Calculate the quarterly average closing prices
quarterly_average = tesla_data['close'].resample('Q').mean()

# Create a new DataFrame from the quarterly data
quarterly_df = pd.DataFrame(quarterly_average)

# Display the DataFrame
print(quarterly_df)




# 4. Create a figure showing the time series for the monthly level and
# the monthly rolling average together.

import matplotlib.pyplot as plt

# Calculate the average monthly closing prices
monthly_average = tesla_data['close'].resample('M').mean()

# Calculate the rolling 3-month average of the monthly averages
monthly_average_rolling = monthly_average.rolling(window=3).mean()

# Plotting both the monthly average and the rolling average
plt.figure(figsize=(10, 5))
plt.plot(monthly_average.index, monthly_average, label='Monthly Average')
plt.plot(monthly_average_rolling.index, monthly_average_rolling, label='3-Month Rolling Average', color='red')
plt.title('Monthly Average vs 3-Month Rolling Average of TSLA Closing Prices')
plt.xlabel('Date')
plt.ylabel('Average Closing Price')
plt.legend()
plt.grid(True)
plt.show()






