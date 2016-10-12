from datetime import datetime

class Tweet:
    def __init__(self, twitter_item):
        self.is_retweet = False
        self.retweet_count = 0
        self._parse_twitter_item(twitter_item)

    def is_retweet(self):
        return self.is_retweet

    def get_id(self):
        return self.id

    def get_text(self):
        return self.text

    def __str__(self):
        tweet_text = ''.join([i if ord(i) < 128 else ' ' for i in self.text])
        return "tweet_id={0} tweet_text={1}".format(self.id, tweet_text)

    def get_clean_text(self):
            return ''.join([i if ord(i) < 128 else ' ' for i in self.text])

    def _parse_twitter_item(self, item):
        # text, id, user, screen_name
        self.text =  item['text'].replace("\n","")
        self.is_retweet = False

        if 'retweeted_status' in item:
            item = item['retweeted_status']
            self.is_retweet = True

        self.id = item['id']
        self.user = item['user']
        self.username = self.user['screen_name']
        self.retweet_count = item['retweet_count']
        self.created_at = self._parse_date(item['created_at'])

    def _parse_date(self, date_str):
        # Mon Sep 24 03:35:21 +0000 2012
        d = date_str.split(' ')
        date_str = ' '.join(d[:4]) +  ' ' + d[5]
        return datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
