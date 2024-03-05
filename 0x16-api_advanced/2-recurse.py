#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to retrieve hot articles for a
    subreddit

    Args:
        subreddit (str): The subreddit to search
        hot_list (list): List to store hot article titles
        after (str): A token indicating the starting point of the next
        page of results
    
    Returns:
        list or None: A list containing titles of hot articles, or None
        if subreddit is invalid
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
                hot_list.append(post['data']['title'])
            if data['data']['after']:
                return recurse(subreddit, hot_list, data['data']['after'])
            else:
                return hot_list
        else:
            return None
    else:
        return None

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
