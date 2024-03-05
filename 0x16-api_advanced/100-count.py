#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of 
all hot articles,
and prints a sorted count of given keywords
"""
import requests
import re

def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords

    Args:
        subreddit (str): The subreddit to search
        word_list (list): List of keywords to count
        after (str): A token indicating the starting point of the
        next page of results
        counts (dict): Dictionary to store counts of keywords

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title']
                for word in word_list:
                    # Case-insensitive search for words not
                    #preceded or followed by other letters
                    matches = re.findall(rf'(?<![a-zA-Z]){word}(?![a-zA-Z])',
                            title, re.IGNORECASE)
                    if matches:
                        counts[word.lower()] = counts.get(word.lower(), 0)
                        + len(matches)
            if data['data']['after']:
                return count_words(subreddit, word_list, data['data']
                        ['after'], counts)
            else:
                sorted_counts = sorted(counts.items(), key=lambda x:
                        (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word.lower()}: {count}")
        else:
            return None
    else:
        return None

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: ./script.py subreddit keyword1 keyword2 ...")
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2:]
        count_words(subreddit, word_list)
