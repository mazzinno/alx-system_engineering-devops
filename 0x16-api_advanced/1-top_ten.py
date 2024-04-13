#!/usr/bin/python3
"""prints the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Mozilla/5.0"},
        params={"limit": 10},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
