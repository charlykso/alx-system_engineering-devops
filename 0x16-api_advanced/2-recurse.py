#!/usr/bin/python3
"""
function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit
"""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit
    returns: a list containing the titles of
    all hot articles for a given subreddit
    or return None if no results are found for a give subreddit
    """

    global after
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)
    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')
        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)
