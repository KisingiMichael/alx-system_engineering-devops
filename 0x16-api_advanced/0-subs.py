#!/usr/bin/python3

import requests

""" A function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

def number_of_subscribers(subreddit):
    # Define the URL for the subreddit's JSON data
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    num_subs = data.get("subsribers")

    return num_subs
