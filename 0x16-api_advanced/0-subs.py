#!/usr/bin/python3
"""
Module Docs
"""
import requests

headers = {"User-Agent": "MyCustomUserAgent/1/0"}


def number_of_subscribers(subreddit):
    """
    Function Docs
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    return 0
