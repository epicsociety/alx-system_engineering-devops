#!/usr/bin/python3
""" module contain a recursive function that returns a key value list of words
and count """

import requests
import re


def count_words(subreddit, word_list, after=None, word_dict=None):
    """ a recursive function that get the count of words from titles"""
    if word_dict is None:
        word_dict = {}

    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 100, 'after': after} if after else {'limit': 100}
    headers = {'User-Agent': 'Custom User-Agent'}
    response = requests.get(base_url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                pattern = r'\b{}\b'.format(re.escape(word.lower()))
                if re.search(pattern, title):
                    word_dict[word] = word_dict.get(word, 0) + 1

        after = data['data']['after']
        if after:
            count_words(subreddit, word_list, after, word_dict)
        else:
            sorted_counts = sorted(word_dict.items(),
                                   key=lambda x: x[0].lower())
            for word, count in sorted_counts:
                print('{}: {}'.format(word.lower(), count))

    return
