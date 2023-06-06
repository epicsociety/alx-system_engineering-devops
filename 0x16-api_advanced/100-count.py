#!/usr/bin/python3
""" Using recursive function to get the wordlist"""


import requests as request


def count_words(subreddit, word_list, count_dict=None, after=None):
    headers = {'User-Agent': 'Custom User-Agent'}
    if count_dict is None:
        count_dict = {}

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after} if after else None
    response = request.get(url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                title = post['data']['title']
                for word in word_list:
                    count = title.lower().count(word.lower())
                    if count > 0:
                        count_dict[word] = count_dict.get(word, 0) + count
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list,
                                   count_dict, after=after)
            else:
                sorted_counts = sorted(count_dict.items(), key=lambda x:
                                       (-x[1], x[0]))
                for word, count in sorted_counts:
                    print('{}: {}'.format(word.lower(), count))

        except (KeyError, ValueError):
            pass

    return
