class Tweet:
    
    def __init__(self, twitter_item):
        #  id, author, author_id, 
		self.text = twitter_item['text'].replace("\n","")
		self.id = twitter_item['id']
		self.author_id = twitter_item['user']
		self.author_name = twitter_item['screen_name']
		self.is_retweet = True
		
		if 'retweeted_status' in twitter_item:
		    self.is_retweet = True
            
    def is_retweet(self):
        return self.is_retweet
        
    def _parse_twitter_item(self, item):
        # text, id, user, screen_name
        self.text =  item['text'].replace("\n","")
        self.is_retweet = False
        
        if 'retweeted_status' in item:
            item = item['retweeted_status']
            self.is_retweet = True
        
        self.id = item['id']
        self.author_id = item['user']
        self.author_name = item['screen_name']