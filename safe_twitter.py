from TwitterAPI import TwitterAPI

class safeTwitter(object):
    rate_limit_precent = 100

    def checkError( self, r ):
	r = r.json()
	if 'errors' in r:
		print("We got an error message: " + r['errors'][0]['message'] + " Code: " + str(r['errors'][0]['code']) )
		#sys.exit(r['errors'][0]['code'])

    def checkRateLimit(self):
	
	r = api.request('application/rate_limit_status').json()

	for res_family in r['resources']:
		for res in r['resources'][res_family]:
			limit = r['resources'][res_family][res]['limit']
			remaining = r['resources'][res_family][res]['remaining']
			self_limit_prcent = float(remaining)/float(limit)*100

			if res == "/search/tweets":
				ratelimit_search=[limit,remaining,percent]

			if res == "/application/rate_limit_status":
				ratelimit=[limit,remaining,percent]

			#print(res_family + " -> " + res + ": " + str(percent))
			if percent < 5.0:
				LogAndPrint(res_family + " -> " + res + ": " + str(percent) + "  !!! <5% Emergency exit !!!")				
				sys.exit(res_family + " -> " + res + ": " + str(percent) + "  !!! <5% Emergency exit !!!")
			elif percent < 30.0:
				LogAndPrint(res_family + " -> " + res + ": " + str(percent) + "  !!! <30% alert !!!")				
			elif percent < 70.0:
				print(res_family + " -> " + res + ": " + str(percent))


    def Retweet(tweet):
        pass

    def Favorite(tweet):
        pass

    def Query(serch_query, count):
        pass
