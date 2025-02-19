import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Read Twitter data from CSV files
csv_files = ['BTCP1.csv', 'BTCP2.csv', 'BTCP3.csv', 'BTCP4.csv', 'BTCP5.csv', 'BTCP6.csv', 'BTCP7.csv', 'BTCP8.csv']
frames = []
for file in csv_files:
    for chunk in pd.read_csv(file, chunksize=10000):
        frames.append(chunk)
df = pd.concat(frames)
df['created_at'] = pd.to_datetime(df['created_at'])
tweets_by_day = df.groupby(df['created_at'].dt.date).size()

# Fetch Bitcoin data using yfinance
bitcoin_data = yf.download('BTC-USD', start='2013-09-30', end='2021-03-29')

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the Twitter data on the left y-axis as a bar chart
ax.bar(tweets_by_day.index, tweets_by_day.values, color='blue')
ax.set_ylabel('Price in USD', color='blue')

# Create a twin y-axis on the right for Bitcoin data
ax2 = ax.twinx()

# Plot the Bitcoin data on the right y-axis as a line chart
ax2.plot(bitcoin_data.index, bitcoin_data['Close'], color='orange')
ax2.set_ylabel('Number of Tweets', color='orange')

# Set the x-axis label
ax.set_xlabel('Date')

# Add a title to the plot
ax.set_title('Twitter Data vs Bitcoin Data')

# Show the plot
plt.show()

