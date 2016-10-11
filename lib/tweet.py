class Tweet:
    def __init__(self, twitter_item):
        self.id = ''
        self.text = ''
        self.author_id = ''
        self.author_name = ''
        self.is_retweet = False
        self._parse_twitter_item(twitter_item)

    def is_retweet(self):
        return self.is_retweet
        
    def get_id(self):
        return self.id
        
    def get_text(self):
        return self.text

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