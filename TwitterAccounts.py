import pandas as pd

import matplotlib as plt
# specify the csv file names as a list
csv_files = ['BTCP1.csv', 'BTCP2.csv', 'BTCP3.csv', 'BTCP4.csv', 'BTCP5.csv', 'BTCP6.csv', 'BTCP7.csv', 'BTCP8.csv']

# create an empty dictionary to store the frequency of each account
frequency = {}

# loop through each csv file
for csv_file in csv_files:
    # read in the csv file as a pandas dataframe
    data = pd.read_csv(csv_file)
    # loop through each row of the dataframe
    for index, row in data.iterrows():
        # extract the text of the tweet from the 'text' column
        text = row['text']
        # split the text into a list of words
        words = text.split()
        # loop through each word in the list
        for word in words:
            # check if the word starts with '@'
            if word.startswith('@'):
                # remove any punctuation from the word
                account = word.strip('@').rstrip('!:,.;?')
                # increment the count of the account in the frequency dictionary
                if account in frequency:
                    frequency[account] += 1
                else:
                    frequency[account] = 1

# sort the frequency dictionary in descending order based on the frequency count
sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

# print the top 10 accounts with the highest frequency count
print("Top 10 accounts by frequency:")
for account, count in sorted_frequency[:10]:
    print(account, count)

