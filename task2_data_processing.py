import json
import csv
import glob
import os
json_files = glob.glob("data/trends_*.json")

if not json_files:
    print("No JSON file found in the data folder.")
    exit()

# Use the latest JSON file
json_file = sorted(json_files)[-1]

print("Loading:", json_file)
with open(json_file, "r", encoding="utf-8") as file:
    stories = json.load(file)
cleaned_stories = []

for story in stories:

    # Get each required field
    post_id = story.get("post_id")
    title = story.get("title")
    category = story.get("category")
    score = story.get("score", 0)
    num_comments = story.get("num_comments", 0)
    author = story.get("author")
    collected_at = story.get("collected_at")

    # Skip records without a title or ID
    if post_id is None or not title:
        continue

    # Replace missing author with "unknown"
    if not author:
        author = "unknown"

    # Make sure numeric values are numbers
    try:
        score = int(score)
    except (ValueError, TypeError):
        score = 0

    try:
        num_comments = int(num_comments)
    except (ValueError, TypeError):
        num_comments = 0

    # Remove unnecessary spaces from title
    title = title.strip()

    # Create cleaned record
    cleaned_story = {
        "post_id": post_id,
        "title": title,
        "category": category,
        "score": score,
        "num_comments": num_comments,
        "author": author,
        "collected_at": collected_at
    }

    cleaned_stories.append(cleaned_story)
csv_file = "data/trends_processed.csv"

fieldnames = [
    "post_id",
    "title",
    "category",
    "score",
    "num_comments",
    "author",
    "collected_at"
]

with open(csv_file, "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(cleaned_stories)
print()
print("----------------------------------------")
print("Task 2 completed!")
print("Original stories:", len(stories))
print("Cleaned stories:", len(cleaned_stories))
print("CSV saved to:", csv_file)
print("----------------------------------------")