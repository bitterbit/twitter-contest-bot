from datetime import datetime, timedelta
import pickle

class ContestScanner:

	MAX_RESULTS = 100
	MAX_TIME_DELTA_DAYS = 10

	def __init__(self, api):
		self.api = api
		self.scanned_ids = dict()
		
	def scannAll(self, queries):
		results = []
		for query in queries:
			results.append(self.scan(query))
			
		return results 
		
	def scan(self, query):
		results = []
		
		tweets = self.api.serch_tweets(query, self.MAX_RESULTS)
		for tweet in tweets:
			if not self._exists(tweet) and self._is_valid(tweet):
				self._add(tweet)
				results.append(tweet)
					
		return results
				
	def _add(self, tweet):
		self.scanned_ids[tweet.get_id()] = True
	
	def _exists(self, tweet):
		if tweet.get_id() in self.scanned_ids:
			return True
		return False
	
	def _is_valid(self, tweet):
		if tweet.retweet_count <= 0:
			return False
			
		if datetime.now() - tweet.created_at > timedelta(days=self.MAX_TIME_DELTA_DAYS):
			return False
			
		return True
		
	def _cache_scanned_ids(self):
		with open('tweeted.pickle', 'wb') as f:
			pickle.dump(self.scanned_ids.keys(), f)	
			
	def _load_cached_scanned_ids(self):
		with open('tweeted.pickle', 'rb') as f:
			ids = pickle.load(f)
			for id in ids:
				self.scanned_ids[id] = True