from TwitterAPI import TwitterAPI
from lib.safe_twitter import SafeTwitter
from lib.retweeter import ReTweeter
from lib.contest_scanner import ContestScanner
import threading
import time
import json
import os.path
import sys
import logging
import logging.handlers

# Load our configuration from the JSON file.
with open('config.json') as data_file:
	data = json.load(data_file)

# These vars are loaded in from config.
consumer_key = data["consumer-key"]
consumer_secret = data["consumer-secret"]
access_token_key = data["access-token-key"]
access_token_secret = data["access-token-secret"]
scan_update_time = data["scan-update-time"]
min_ratelimit_post = data["min-ratelimit-post"]
min_ratelimit_search = data["min-ratelimit-search"]
search_queries = data["search-queries"]
follow_keywords = data["follow-keywords"]
fav_keywords = data["fav-keywords"]
log_file_name = data["log-file-name"]


tweet_api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

def prepare_logger():
    # create logger with 'spam_application'
	logger = logging.getLogger('spam_application')
	logger.setLevel(logging.DEBUG)
	# create file handler which logs even debug messages
	fh = logging.FileHandler(log_file_name)
	fh.setLevel(logging.DEBUG)
	# create formatter and add it to the handlers
	formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
	fh.setFormatter(formatter)
	# add the handlers to the logger
	logger.addHandler(fh)
	return logger


class TweeterBotMain(object):
    def __init__(self):
        logger = prepare_logger()
        safe_api = SafeTwitter(logger, min_ratelimit_search, min_ratelimit_post, tweet_api)
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
