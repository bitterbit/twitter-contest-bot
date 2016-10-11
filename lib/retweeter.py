class ReTweeter:
	def __init__(self, api, fav_keywords, follow_keywords):
		self.api = api
		self.fav_keywords = fav_keywords
		self.follow_keywords = follow_keywords
	
	def retweet_all(self, tweets):
		for tweet in tweets:
			self.retweet(tweet)
	
	def retweet(self, tweet):
		self.api.retweet(tweet)
		
		if self._shoud_follow(tweet):
			self.api.follow(tweet)
			
		if self._should_favotrite(tweet):
			self.api.favorite(tweet)
		
	def _shoud_follow(self, tweet):
		return self._tweet_contains_keyword(tweet, self.follow_keywords)
	
	def _should_favotrite(self, tweet):
		return self._tweet_contains_keyword(tweet, self.fav_keywords)
	
	def _tweet_contains_keyword(self, tweet, keywords):
		words = tweet.get_text().lower().split(' ')
		for word in words:
			if word in keywords:
				return True
		return False
		