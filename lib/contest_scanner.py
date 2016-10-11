class ContestScanner:

	MAX_RESULTS = 100

	def __init__(self, api):
		self.api = api
		self.scanned_tweets = []
		self.scanned_ids = dict()
		
	def scan(self, query):
		tweets = self.api.serch_tweets(query, self.MAX_RESULTS)

		for tweet in tweets:
			if not self._exists(tweet) and self._is_valid(tweet):
				self._add(tweet)
				
	def _add(self, tweet):
		self.scanned_tweets.append(tweet)
		self.scanned_ids[tweet.get_id()] = True
	
	def _exists(self, tweet):
		pass
	
	def _is_valid(self, tweet):
		pass