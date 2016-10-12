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
import logging

class TweeterBotMain(object):
    def __init__(self):
        config = Config()
        self.config = config
        logger = self._prepare_logger(config.log_path)
        tweet_api = TwitterAPI(config.consumer_key, config.consumer_secret, config.access_token_key, config.access_token_secret)
        
        safe_api = SafeTwitter(logger, config.min_rate_limit_search, config.min_rate_limit_post, tweet_api)
        self.scanner = ContestScanner(safe_api)
        self.retweeter = ReTweeter(safe_api, config.keywords_fav, config.keywords_follow)

    def run(self):
        relevant_tweets = self.scanner.scan(self.config.search_queries)
        self.retweeter.retweet_all(relevant_tweets)
        
    def _prepare_logger(self, path):
    	logger = logging.getLogger('spam_application')
    	logger.setLevel(logging.DEBUG)
    	fh = logging.FileHandler(path)
    	fh.setLevel(logging.DEBUG)
    	formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    	fh.setFormatter(formatter)
    	logger.addHandler(fh)
    	return logger


if __name__ == "__main__":
    tweet_bot = TweeterBotMain()
    while True:
        tweet_bot.run()
        print "---finish round, waiting: ", scan_update_time, " seconds!---"
        time.sleep(scan_update_time)