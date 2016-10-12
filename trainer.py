import logging
import json
import os.path
from TwitterAPI import TwitterAPI
from lib.safe_twitter import SafeTwitter

TRAIN_FILE_NAME = "train.json"
TRAIN_QUERY = "WIN"


class Trainer(object):
    def __init__(self, api):
        self.api = api

    def fetch_tweets(self, query):
        tweets = self.api.serch_tweets(query, 10)
        return [t.get_clean_text() for t in tweets]


    def load_train(self):
        if not os.path.isfile(TRAIN_FILE_NAME):
            return []
        with open(TRAIN_FILE_NAME, 'r') as train_file:
            return json.load(train_file)

    def train(self, query):
        tweets = self.fetch_tweets(query)
        trained_tweets = self.load_train()
        for tweet in tweets:
            if tweet not in [t[0] for t in trained_tweets]:
                feedback = self.get_feedback(tweet)
                self.save_feedback(tweet, feedback)

    def get_feedback(self, tweet):
        print tweet
        print "------------------------------------"
        x = raw_input("would you retweet this? ")
        if x == 'y':
            return True
        elif x == 'n':
            return False
        else:
            print "please enter 'y' or 'n' "
            return self.get_feedback(tweet)

    def save_feedback(self, tweet, feedback):
        if not os.path.isfile(TRAIN_FILE_NAME):
            with open(TRAIN_FILE_NAME, mode='w') as f:
                f.write(json.dumps([(tweet, feedback)], indent=4))
        else:
            with open(TRAIN_FILE_NAME) as feedsjson:
                feeds = json.load(feedsjson)
            feeds.append((tweet, feedback))
            with open(TRAIN_FILE_NAME, mode='w') as f:
                f.write(json.dumps(feeds, indent=4))

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

tweet_api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

if __name__ == "__main__":
    logger = logging.getLogger()
    safe_api = SafeTwitter(logger, min_ratelimit_post, min_ratelimit_search, tweet_api)
    data_store = Trainer(safe_api)
    data_store.train(TRAIN_QUERY)
