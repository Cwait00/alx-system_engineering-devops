#!/usr/bin/python3

"""
Function that queries the Reddit API and prints the titles of
the first 10 hot posts
listed for a given subreddit
"""
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit

    Args:
        subreddit (str): The subreddit to search

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            if 'data' in data and 'children' in data['data']:
                for post in data['data']['children']:
                    print(post['data']['title'])
            else:
                print("No hot posts found for this subreddit.")
        except ValueError:
            print("Error: Invalid JSON response from the Reddit API.")
    else:
        print("Error: Failed to fetch data from the Reddit API. Please check the subreddit name.")

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
