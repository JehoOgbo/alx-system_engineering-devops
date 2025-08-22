#!/usr/bin/python3
""" A function that retrieves the top 10 hot posts on a given subreddit
"""
from requests import get


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
