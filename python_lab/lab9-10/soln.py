import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Data
data = {
    "State": ["MadhyaPradesh", "MadhyaPradesh", "MadhyaPradesh", "MadhyaPradesh",
              "Rajasthan", "Rajasthan", "Rajasthan", "Rajasthan"],
    "Party": ["BJP", "INC", "BSP", "Others", "BJP", "INC", "BSP", "Others"],
    "SeatsWon": [163, 66, 0, 1, 115, 69, 2, 13],
    "Total_Seats": [230, 230, 230, 230, 200, 200, 200, 200],
    "Voter_Turnout(%)": [72.1, 72.1, 72.1, 72.1, 74.2, 74.2, 74.2, 74.2]
}

filename = "election_data.csv"

# Step 2: Check if file exists, if not create and write data
try:
    if not os.path.exists(filename):
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"File '{filename}' created successfully.")
    else:
        print(f"File '{filename}' already exists.")
except Exception as e:
    print(f"Error while handling the file: {e}")

# Step 3: Read the data into a DataFrame and calculate Seats_Percentage
try:
    df = pd.read_csv(filename)
    df['Seats_Percentage'] = (df['SeatsWon'] / df['Total_Seats']) * 100
    print("Data with Seats_Percentage:\n", df)
except Exception as e:
    print(f"Error while reading or processing the data: {e}")

# Step 4: Find the party with the highest number of seats in each state
try:
    highest_seats = df.loc[df.groupby('State')['SeatsWon'].idxmax()]
    print("\nParty with highest seats in each state:\n", highest_seats[['State', 'Party', 'SeatsWon']])
except Exception as e:
    print(f"Error while finding the party with the highest seats: {e}")

# Step 5: Create a bar chart
try:
    plt.figure(figsize=(10, 6))
    sns.barplot(x='State', y='SeatsWon', hue='Party', data=df)
    plt.title('Number of Seats Won by Each Party in Each State')
    plt.ylabel('Seats Won')
    plt.xlabel('State')
    plt.legend(title='Party')
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Error while creating the visualization: {e}")
