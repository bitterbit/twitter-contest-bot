import json
from random import shuffle
import pickle
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

def _ask_about_result():
	i = raw_input("are you satistfied ? ")
	if i == "y":
		return True
	if i == 'n':
		return False
	else:
		print " y or n please"
		return self._ask_about_result()

if __name__ == '__main__':
	print "Hello"

	data = load_sample()

	splitIndex = 2*len(data)/3
	train = data[:splitIndex]
	test = data[splitIndex:]

	cl = NaiveBayesClassifier(train)

	for item in test:
		print_item(item)

	print "accuarciy", cl.accuracy(test)

	happy = _ask_about_result()
	if happy:
		with open('classifier.pickle', "wb") as f:
			pickle.dump(cl, f)
