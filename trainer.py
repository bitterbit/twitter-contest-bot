import logging
import json
import os.path
from TwitterAPI import TwitterAPI
from lib.safe_twitter import SafeTwitter
from lib.config import Config 

TRAIN_FILE_NAME = "ml/train.json"
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


if __name__ == "__main__":
    logger = logging.getLogger()
    config = Config()
    
    tweet_api = TwitterAPI(config.consumer_key, config.consumer_secret, config.access_token_key, config.access_token_secret)
    safe_api = SafeTwitter(logger, config.min_ratelimit_post, config.min_ratelimit_search, tweet_api)
    
    data_store = Trainer(safe_api)
    data_store.train(TRAIN_QUERY)
