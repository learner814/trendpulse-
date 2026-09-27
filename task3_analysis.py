import pandas as pd
import numpy as np
# Load the processed CSV file
df = pd.read_csv("data/trends_processed.csv")

print("TrendPulse - Task 3")
print("----------------------------------------")

# Basic information
print("Total stories:", len(df))
print()

# Category count
print("Stories by category:")
print(df["category"].value_counts())
print()

# Average score
print("Average score:", round(df["score"].mean(), 2))
print()

# Average comments
print("Average comments:", round(df["num_comments"].mean(), 2))
print()

# Highest scoring story
highest_score = df.loc[df["score"].idxmax()]

print("Highest scoring story:")
print("Title:", highest_score["title"])
print("Score:", highest_score["score"])
print("Category:", highest_score["category"])
print()

# Most commented story
most_commented = df.loc[df["num_comments"].idxmax()]

print("Most commented story:")
print("Title:", most_commented["title"])
print("Comments:", most_commented["num_comments"])
print("Category:", most_commented["category"])
print()

# NumPy calculations
scores = np.array(df["score"])

print("Score statistics:")
print("Minimum:", np.min(scores))
print("Maximum:", np.max(scores))
print("Mean:", round(np.mean(scores), 2))

print("----------------------------------------")
print("Task 3 completed!")
