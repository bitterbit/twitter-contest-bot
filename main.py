from TwitterAPI import TwitterAPI
from lib.safe_twitter import SafeTwitter
from lib.retweeter import ReTweeter
from lib.contest_scanner import ContestScanner
from lib.config import Config 

import threading
import time
import json
import os.path
import sys


class TweeterBotMain(object):
    def __init__(self):
        config = Config()
        tweet_api = TwitterAPI(config.consumer_key, config.consumer_secret, config.access_token_key, config.access_token_secret)
        safe_api = SafeTwitter(config.min_ratelimit_search, config.min_ratelimit_post, tweet_api)
        self.scanner = ContestScanner(safe_api)
        self.retweeter = ReTweeter(safe_api, fav_keywords, follow_keywords)

    def run(self):
        relevant_tweets = self.scanner.scan(search_queries)
        self.retweeter.retweet_all(relevant_tweets)


if __name__ == "__main__":
    tweet_bot = TweeterBotMain()
    while True:
        tweet_bot.run()
        print "---finish round, waiting: ", scan_update_time, " seconds!---"
        time.sleep(scan_update_time)
