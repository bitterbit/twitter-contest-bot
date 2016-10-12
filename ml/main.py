import json
from random import shuffle
from textblob.classifiers import NaiveBayesClassifier

def load_sample():
	with open('tweets.json', 'rb') as f:
		tweets = json.load(f)

	# Put data in format ready for ML	
	data = []
	for t in tweets["good"]:
		data.append((t, "good"))
		
	for t in tweets["bad"]:
		data.append((t, "bad"))
		
	shuffle(data)
	return data

if __name__ == '__main__':
	print "Hello"
	
	data = load_sample()

	splitIndex = 2*len(data)/3	
	train = data[:splitIndex]
	test = data[splitIndex:]
	
	
	cl = NaiveBayesClassifier(train)	

	for item in test:
		print "text:", item[0]
		print "predicted:", cl.classify(item[0])	
		print "real:", item[1]
		print '-------------------------------'
		
	
	
