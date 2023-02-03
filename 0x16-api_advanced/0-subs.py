#!/usr/bin/python3
"""
function that queries the Reddit API and
returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    send a get request to Reddit API.
    return number of subscribers or 0
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    response = requests.get(url, headers=headers).json()
    subscribers = response.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
