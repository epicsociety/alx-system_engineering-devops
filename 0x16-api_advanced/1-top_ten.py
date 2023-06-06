#!/usr/bin/python3
""" Gets the 10 top hot posts """


import requests as request


def top_ten(subreddit):
    """ Gets the titles of the 10 top host posts"""

    headers = {'User-Agent': 'Custom User-Agent'}

    response = request.get('https://www.reddit.com/r/{}/hot.json'
                           .format(subreddit), headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']

            for i in range(min(len(posts), 10)):
                title = posts[i]['data']['title']
                print("{}. {}".format(i+1, title))
        except (KeyError, ValueError):
            pass
    else:
        print(None)
