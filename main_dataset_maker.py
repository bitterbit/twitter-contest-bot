import logging
import json
import os.path
from TwitterAPI import TwitterAPI
from lib.safe_twitter import SafeTwitter
from lib.config import Config 

TWEET_QUERY = "WIN"


class DatasetMaker(object):
    def __init__(self, api, dataset_size=10):
        self.api = api
        self.dataset_size = dataset_size
        self.dataset_file = 'files/dataset_test.json'

    def make_dataset(self, query):
        tweets = self._fetch_tweets(query)
        trained_tweets = self._load_dataset()
        for tweet in tweets:
            if tweet not in [t[0] for t in trained_tweets]:
                feedback = self._get_user_feedback(tweet)
                self._save_tweet_feedbak(tweet, feedback)
                
    def _fetch_tweets(self, query):
        tweets = self.api.serch_tweets(query, self.dataset_size)
        return [t.get_clean_text() for t in tweets]

    def _get_user_feedback(self, tweet):
        print tweet
        print "------------------------------------"
        x = raw_input("would you retweet this? ")
        if x == 'y':
            return True
        elif x == 'n':
            return False
        else:
            print "please enter 'y' or 'n' "
            return self._get_user_feedback(tweet)

    def _save_tweet_feedbak(self, tweet, feedback):
        self._create_file_if_dosent_exist(self.dataset_file, "[]")
        dataset = self._load_dataset()
        dataset.append((tweet, feedback))
        with open(self.dataset_file, 'w') as f:
            json.dump(dataset, f, indent=4)
            
    def _load_dataset(self):
        if not os.path.isfile(self.dataset_file):
            return []
            
        with open(self.dataset_file, 'r') as train_file:
            return json.load(train_file)
            
    def _create_file_if_dosent_exist(self, path, default_data=""):
        if not os.path.isfile(path):
            with open(path, "w") as f:
                f.write(default_data)


if __name__ == "__main__":
    logger = logging.getLogger()
    config = Config()
    
    tweet_api = TwitterAPI(config.consumer_key, config.consumer_secret, config.access_token_key, config.access_token_secret)
    safe_api = SafeTwitter(logger, config.min_rate_limit_post, config.min_rate_limit_search, tweet_api)
    
    data_store = DatasetMaker(safe_api)
    data_store.make_dataset(TWEET_QUERY)
