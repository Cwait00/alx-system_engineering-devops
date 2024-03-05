#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}  # Reddit API requires a custom User-Agent header
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0


# Test the function
if __name__ == '__main__':
    subreddit = input("Enter the name of the subreddit: ")
    subscribers_count = number_of_subscribers(subreddit)
    print(f"Number of subscribers in '{subreddit}': {subscribers_count}")
