# -*- coding: utf-8 -*-
"""
Reddit exploatory script 

"""

import praw
import pandas as pd

reddit = praw.Reddit(client_id='RNGhJE66F0dfcg', 
                     client_secret='reMSAKkNv5daoHSRG3Cy15BhVw8', 
                     user_agent='cdc',)


subreddit2 = reddit.subreddit('rstats')
r_subreddit = subreddit2.new(limit=1000)
    
reddit_data = []

for i in r_subreddit:
    reddit_data.append(
        [i.title]
        )

df = pd.DataFrame(reddit_data)

