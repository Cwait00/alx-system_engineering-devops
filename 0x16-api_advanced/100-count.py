#!/usr/bin/python3

import re
import requests
import sys

def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively queries the Reddit API, parses the titles of hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): A list of keywords to count.
        after (str): A pagination token.
        counts (dict): A dictionary to store keyword counts.

    Returns:
        None
    """
    if after == "STOP":
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": "100", "after": after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print("Invalid subreddit or no posts match.")
        return

    data = response.json().get("data")

    if not data or "children" not in data:
        print("Invalid subreddit or no posts match.")
        return

    posts = data["children"]

    for post in posts:
        title = post["data"]["title"]
        for word in word_list:
            matches = re.findall(rf'(?<![a-zA-Z]){word}(?![a-zA-Z])', title, re.IGNORECASE)
            if matches:
                counts[word.lower()] = counts.get(word.lower(), 0) + len(matches)

    after = data.get("after")
    count_words(subreddit, word_list, after, counts)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./script.py subreddit keyword1 keyword2 ...")
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2:]
        count_words(subreddit, word_list)
