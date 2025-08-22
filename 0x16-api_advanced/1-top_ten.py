#!/usr/bin/python3
""" A function that retrieves the top 10 hot posts on a given subreddit
"""
from requests import get


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 10}
    response = get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        titles = data['data']['children']
        for item in titles:
            print(item['data']['title'])
    else:
        print("None")
