import pandas as pd
import matplotlib.pyplot as plt

# Load processed CSV
df = pd.read_csv("data/trends_processed.csv")

print("TrendPulse - Task 4")
print("----------------------------------------")

# Chart 1: Number of stories by category
category_counts = df["category"].value_counts()

plt.figure()
category_counts.plot(kind="bar")
plt.title("Number of Stories by Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.tight_layout()
plt.savefig("data/stories_by_category.png")
plt.close()

print("Created: data/stories_by_category.png")


# Chart 2: Average score by category
average_scores = df.groupby("category")["score"].mean()

plt.figure()
average_scores.plot(kind="bar")
plt.title("Average Score by Category")
plt.xlabel("Category")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("data/average_score_by_category.png")
plt.close()

print("Created: data/average_score_by_category.png")

print("----------------------------------------")
print("Task 4 completed!")
