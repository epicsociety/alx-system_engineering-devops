#!/usr/bin/python3
""" Gets the number of subscribers of the given subreddit"""


import requests as request


def number_of_subscribers(subreddit):
    """ Gets the number if subcribers """

    headers = {'User-Agent': 'Custom User-Agent'}

    response = request.get('https://www.reddit.com/r/{}/about.json'
                           .format(subreddit), headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            total_subscribers = data['data']['subscribers']
            return total_subscribers
        except (KeyError, ValueError):
            pass
    return 0
