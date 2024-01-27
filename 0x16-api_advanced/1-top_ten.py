#!/usr/bin/python3
"""
module doc
"""
import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def top_ten(subreddit):
    """method doc"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers)
    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
        print("None")
