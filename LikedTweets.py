import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into a pandas dataframe
df = pd.read_csv('BTCP1.csv')

# Clean the data by removing any tweets with no likes or retweets
df = df[(df['likes'] > 0) & (df['retweets'] > 0)]

# Sort the dataframe by number of likes in descending order
df = df.sort_values('likes', ascending=False)

# Select the top 10 tweets by number of likes
df = df[:10]

# Create a bar chart of the top 10 tweets by number of likes
plt.bar(df['id'], df['likes'])

# Set the title and axis labels
plt.title('Top 10 Tweets by Number of Likes')
plt.xlabel('Tweet ID')
plt.ylabel('Number of Likes')

# Show the chart
plt.show()
