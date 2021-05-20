#!/usr/bin/python3
""" queries Reddit API and returns number of subscribers for a subreddit """

import requests


def number_of_subscribers(subreddit):
    """ Return number of subscribers for a subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {"User-Agent": "bobthebuilder"}
    request = requests.get(url, headers=user_agent)
    if request.status_code == 200:
        request = request.json()
        data = request.get('data')
        subscribers = data.get("subscribers")
        if data is not None and subscribers is not None:
            return subscribers
        return 0
