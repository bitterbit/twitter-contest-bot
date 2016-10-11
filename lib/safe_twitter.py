from TwitterAPI import TwitterAPI
from tweet import Tweet

class SafeTwitter(object):

    def __init__(self, min_ratelimit_search, min_ratelimit_post):
        self.min_search_rate_limit = min_ratelimit_search
        self.min_post_rate_limit = min_ratelimit_post

    def _check_error( self, r ):
    	r = r.json()
    	if 'errors' in r:
    	    print("We got an error message: " + r['errors'][0]['message'] + " Code: " + str(r['errors'][0]['code']) )
    	    #sys.exit(r['errors'][0]['code'])
                return True
            return False

    def _check_rate_limit_search(self):
    	r = api.request('application/rate_limit_status').json()

    	for res_family in r['resources']:
    	    for res in r['resources'][res_family]:
    		limit = r['resources'][res_family][res]['limit']
    		remaining = r['resources'][res_family][res]['remaining']
    		prcent = float(remaining)/float(limit)*100

    		if res == "/search/tweets":
    		    if precent < self.min_search_rate_limit:
                    print "search rate limit too low: ", precent, " want: ", self.min_search_rate_limit, " waiting 30 sec"
                    time.sleep(30)
                    self._check_rate_limit_search()

    def _check_rate_limit_post(self):
        r = api.request('application/rate_limit_status').json()

    	for res_family in r['resources']:
    	    for res in r['resources'][res_family]:
    		    limit = r['resources'][res_family][res]['limit']
    		    remaining = r['resources'][res_family][res]['remaining']
    		    prcent = float(remaining)/float(limit)*100

                if res == "/application/rate_limit_status":
                    print "post rate limit too low: ", precent, " want: ", self.min_post_rate_limit, " waiting 30 sec"
                    if precent < self.min_post_rate_limit:
                        time.sleep(30)
                        self._check_rate_limit_post()

    def retweet(self, tweet):
        self._check_rate_limit_post()
        r = api.request('statuses/retweet/:' + str(tweet.get_id()))
        print "retweet to tweed id: ", str(tweet.get_id()), " text: ", tweet.get_text()
	    self._check_error(r)

    def favorite(self, tweet):
        self._check_rate_limit_post()
        r = api.request('favorites/create', {'id': tweet.get_id()})
        print "favorite tweet id: ", tweet.get_id()
	    self._check_error(r)

    def serch_tweets(self, serch_query, count):
        self._check_rate_limit_search()
        tweets = []
        r = api.request('search/tweets', {'q':search_query, 'result_type':"mixed", 'count':count})
	    error = self._check_error(r)
        if not error:
            print "found ", len(r), " new tweets for ", serch_query, " query"
            for tweet_item in r:
                tweets.append(Tweet(tweet_item))
        return tweets
