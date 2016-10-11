from TwitterAPI import TwitterAPI

class safeTwitter(object):
    rate_limit_precent = 100

    def _check_error( self, r ):
	r = r.json()
	if 'errors' in r:
	    print("We got an error message: " + r['errors'][0]['message'] + " Code: " + str(r['errors'][0]['code']) )
	    #sys.exit(r['errors'][0]['code'])

    def _check_rate_limit_search(self):
	
	r = api.request('application/rate_limit_status').json()

	for res_family in r['resources']:
	    for res in r['resources'][res_family]:
		limit = r['resources'][res_family][res]['limit']
		remaining = r['resources'][res_family][res]['remaining']
		prcent = float(remaining)/float(limit)*100

		if res == "/search/tweets":
		    if precent < self.min_search_rate_limit:
                        time.sleep(30)
                        _check_rate_limit_search()

                            
    def _check_rate_limit_post(self):
        r = api.request('application/rate_limit_status').json()

	for res_family in r['resources']:
	    for res in r['resources'][res_family]:
		limit = r['resources'][res_family][res]['limit']
		remaining = r['resources'][res_family][res]['remaining']
		prcent = float(remaining)/float(limit)*100
                
            if res == "/application/rate_limit_status":
                if precent < self.min_post_rate_limit:
                    time.sleep(30)
                    _check_rate_limit_post()

    def retweet(self, tweet):
        _check_rate_limit_post()
        r = api.request('statuses/retweet/:' + str(tweet.get_id()))
	CheckError(r)

    def favorite(self, tweet):
        _check_rate_limit_post()
        r = api.request('favorites/create', {'id': tweet.get_id()})
	CheckError(r)

    def serch_tweets(self, serch_query, count):
        _check_rate_limit_search()
        r = api.request('search/tweets', {'q':search_query, 'result_type':"mixed", 'count':count})
	CheckError(r)
