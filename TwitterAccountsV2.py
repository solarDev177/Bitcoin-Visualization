import pandas as pd
import matplotlib.pyplot as plt

# Create a list of the filenames for the CSV files containing Twitter data
csv_filenames = ['BTCP1.csv', 'BTCP2.csv', 'BTCP3.csv', 'BTCP4.csv', 'BTCP5.csv', 'BTCP6.csv', 'BTCP7.csv', 'BTCP8.csv']

# Create an empty dictionary to hold the counts of pings for each account
ping_counts = {}

# Loop through each CSV file
for csv_filename in csv_filenames:
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_filename)

    # Loop through each tweet in the DataFrame
    for tweet in df['text']:
        # Split the tweet into words
        words = tweet.split()
        # Loop through each word in the tweet
        for word in words:
            # If the word is a ping (i.e. it starts with '@')
            if word.startswith('@'):
                # Extract the account name (i.e. everything after the '@' symbol)
                account_name = word[1:]
                # Add the account name to the ping_counts dictionary if it's not already there
                if account_name not in ping_counts:
                    ping_counts[account_name] = 0
                # Increment the count of pings for the account
                ping_counts[account_name] += 1

# Sort the ping_counts dictionary by value (i.e. the count of pings)
sorted_ping_counts = sorted(ping_counts.items(), key=lambda x: x[1], reverse=True)

# Get the top 10 most pinged accounts
top_ping_counts = sorted_ping_counts[:10]

# Extract the account names and ping counts into separate lists for plotting
account_names = [account_name for account_name, count in top_ping_counts]
ping_counts = [count for account_name, count in top_ping_counts]

# Create a bar plot of the top 10 most pinged accounts
plt.bar(account_names, ping_counts)
plt.xlabel('Account Name')
plt.ylabel('Number of Pings')
plt.title('Top 10 Most Pinged Accounts on Twitter')
plt.show()
