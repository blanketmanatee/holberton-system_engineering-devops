#!/usr/bin/python3
""" queries Reddit API and prints titles of first 10 hot posts in a sub """

import requests


def top_ten(subreddit):
    """ titles of first 10 hot posts in a sub """
    url="https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent={"User-Agent": "bobthebuilder"}
    request=requests.get(url, headers=user_agent)
    if request.status_code == 200:
        request = request.json()
        data = request.get("data")
        children = data.get("children")
        if data is not None and children is not None:
            for post in children[:10]:
                post_data = post.get("data")
                title = post_data.get("title")
                print(title)
            else:
                print("None")
