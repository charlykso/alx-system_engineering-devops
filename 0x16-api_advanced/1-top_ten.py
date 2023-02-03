#!/usr/bin/python3
"""
function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    if not a valid subreddit print None
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    res = requests.get(url, headers=headers).json()
    hot_posts = res.get('data', {}).get('children', [])
    if not hot_posts:
        print(None)
    for top in hot_posts:
        print(top.get('data').get('title'))
