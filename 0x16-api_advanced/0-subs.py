#!/usr/bin/python3
'''
Return number of subs for a give subrddit
'''
import requests


def number_of_subscribers(subreddit):
    '''
    Returns the number of subreddit subscribers
    '''
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    user_agent = 'reddit_user'

    headers = {'User-Agent': user_agent}

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        return 0

    data = req.json()['data']
    page_list = data['children']
    page_data = page_list[0]['data']

    return page_data['subreddit_subscribers']
