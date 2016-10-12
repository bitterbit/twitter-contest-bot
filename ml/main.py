import json
from random import shuffle
from textblob.classifiers import NaiveBayesClassifier

def load_sample():
	with open('train.json', 'rb') as f:
		data = json.load(f)

	shuffle(data)
	return data

def print_item(item):
	print "text:", item[0]
	print "predicted:", cl.classify(item[0])
	print "real:", item[1]
	print '-------------------------------'

if __name__ == '__main__':
	print "Hello"

	data = load_sample()

	splitIndex = 2*len(data)/3
	train = data[:splitIndex]
	test = data[splitIndex:]


	cl = NaiveBayesClassifier(train)

	print "accuarciy", cl.accuracy(test)
	for item in test:
		print_item(item)
