#!/usr/bin/python3
""" using a recurcive function to parse the title of all hoy articles"""


import requests as request


def recurse(subreddit, hot_list=None, after=None):
    headers = {'User-Agent': 'Custom User-Agent'}

    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after} if after else None
    response = request.get(url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                title = post['data']['title']
                hot_list.append(title)

            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after=after)
            else:
                return hot_list

        except (KeyError, ValueError):
            pass

    return None
