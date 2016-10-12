class Config:
	def __init__(self):
		self.search_queries = ["RT to win", "Retweet and win"]
		self.keywords_follow = [" follow ", " follower "]
		self.keywords_fav = [" fav ", " favorite "]
		
		self.scan_update_time = 1800
		self.rate_limit_update_time = 10
		self.min_rate_limit = 10
		self.min_rate_limit_post = 10
		self.min_rate_limit_search = 40
		
		self.consumer_key = "ENTER_CODE_HERE"
		self.consumer_secret = "ENTER_CODE_HERE"
		self.access_token_key = "ENTER_CODE_HERE"
		self.access_token_secret = "ENTER_CODE_HERE"
		
		self.log_path = 'files/info.log'
		
