from TwitterAPI import TwitterAPI
from tweet import Tweet


class SafeTwitter(object):

    def __init__(self, min_ratelimit_search, min_ratelimit_post, twitter_api):
        self.min_search_rate_limit = min_ratelimit_search
        self.min_post_rate_limit = min_ratelimit_post
        self.api = twitter_api

    def _check_error(self, r):
        if r.status_code != 200:
            r = r.json()
            print("We got an error message: " +
                  r['errors'][0]['message'] + " Code: " + str(r['errors'][0]['code']))
            return True
        return False

    def _check_rate_limit_search(self):
        self._check_limit_loop('/search/tweets', self.min_search_rate_limit)

    def _check_rate_limit_post(self):
        self._check_limit_loop('/application/rate_limit_status', self.min_post_rate_limit)

    def _check_limit_loop(self, limit_name, min_percent, sleep=30):
        while True:
            percent = self._get_limit_percent(limit_name)
            if percent is None:
                print "ERROR"
            elif percent < min_percent:
                print "post rate limit too low: ", precent, " want: ", min_percent, " waiting", sleep, "sec"
                time.sleep(sleep)
            else:
                return

    def _get_limit_percent(self, limit_name):
        r = self.api.request('application/rate_limit_status')
        err = self._check_error(r)
        if not err:
            r = r.json()
            for res_family in r['resources']:
                for res in r['resources'][res_family]:
                    limit = r['resources'][res_family][res]['limit']
                    remaining = r['resources'][res_family][res]['remaining']
                    perecent = float(remaining) / float(limit) * 100
                    if res == limit_name:
                        return perecent

        return None


    def retweet(self, tweet):
        self._check_rate_limit_post()
        r = self.api.request('statuses/retweet/:' + str(tweet.get_id()))
        print "retweet to tweed id: ", str(tweet.get_id()), " text: ", tweet.get_text()
        self._check_error(r)

    def favorite(self, tweet):
        self._check_rate_limit_post()
        r = self.api.request('favorites/create', {'id': tweet.get_id()})
        print "favorite tweet id: ", tweet.get_id()
        self._check_error(r)

    def follow(self, tweet):
        self._check_rate_limit_post()
        r = self.api.request('friendships/create',
                             {'screen_name': tweet.username})
        print "follow tweet id: ", tweet.get_id()
        self._check_error(r)

    def serch_tweets(self, search_query, count):
        self._check_rate_limit_search()
        tweets = []
        r = self.api.request(
            'search/tweets', {'q': search_query, 'result_type': "mixed", 'count': count})
        error = self._check_error(r)
        if not error:
            for tweet_item in r:
                tweets.append(Tweet(tweet_item))
        print "found ", len(tweets), " new tweets for ", search_query, " query"
        return tweets
