import pickle
import os.path
from textblob.classifiers import NaiveBayesClassifier

class TweetFilter():
	
	CLASSIFIER_DATA_PATH = 'tweet_classifier.pickle'
	
	def __init__(self):
		self.classifier = self.load_classifier(self.CLASSIFIER_DATA_PATH) 
	
	def load_classifier(self, path):
		if os.path.isfile(path):
			with open(path, "rb") as f:
				return pickle.load(f)
		
	def filter(self, tweet):
		return self.classifier.classify(tweet.get_text())