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
    response = requests.get(url, headers={'User-Agent': 'app/1.0'})
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
