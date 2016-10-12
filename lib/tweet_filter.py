import pickle
import os.path
from datetime import datetime
from textblob.classifiers import NaiveBayesClassifier

class TweetContestFilter():
	CLASSIFIER_DATA_PATH = 'tweet_classifier.pickle'
	
	def __init__(self):
		self.classifier = self.load_classifier(self.CLASSIFIER_DATA_PATH) 
	
	def load_classifier(self, path):
		if os.path.isfile(path):
			with open(path, "rb") as f:
				return pickle.load(f)
		
	def filter(self, tweet):
		return self.classifier.classify(tweet.get_text())
		
		
class TweetAgeFilter():
	def filter(self, tweet):
		if datetime.now() - tweet.created_at > timedelta(days=self.MAX_TIME_DELTA_DAYS):
			return False
		return True
		
		
class TweetRTCountFilter():
	def filter(self, tweet):
		if tweet.retweet_count <= 0:
			return False
		return True