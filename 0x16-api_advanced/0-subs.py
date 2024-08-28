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
    
    # Define custom headers
    headers = {'User-Agent': 'KisingiMichael'}
    
    try:
        # Make a GET request to the Reddit API without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response and extract the number of subscribers
            data = response.json()
            return data['data'].get('subscribers', 0)
        else:
            # If the subreddit is invalid or the request fails, return 0
            return 0
    except requests.RequestException:
        # In case of any network-related errors, return 0
        return 0
