# -*- coding: utf-8 -*-
"""
Reddit exploatory script 

"""

import praw

reddit = praw.Reddit(client_id='RNGhJE66F0dfcg', 
                     client_secret='reMSAKkNv5daoHSRG3Cy15BhVw8', 
                     user_agent='cdc')


no_subreddit = reddit.subreddit('rstats')
hot = no_subreddit.hot(limit=1000)

for submission in hot:
    print(submission.title, submission.permalink)