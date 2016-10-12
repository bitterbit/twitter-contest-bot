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
		
		self.consumer_key = "rfxDa60lp96LKuSxlFp7WpvH2"
		self.consumer_secret = "MTEVi0gsSBbQoCubltaOL5FYsbRdn9AbsOnM4nij7hYarWfoe8"
		self.access_token_key = "785893095581757440-cLlr6U3MihnjyeZHS1jBn4cUgK4yx44"
		self.access_token_secret = "Ec6yS4Kki72JcNIDCBXmfjifdq5RYSAdk9tdCzFAh1GWo"
		
		self.log_path = 'files/info.log'
		
