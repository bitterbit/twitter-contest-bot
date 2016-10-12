# twitter-contest-bot
Will poll for Retweet Contests and retweet them. Inspired by http://www.hscott.net/twitter-contest-winning-as-a-service/
Uses Naive Bayes Machine Learning to better pick tweets to retweet :)

[![Build Status](https://travis-ci.org/bitterbit/twitter-contest-bot.svg?branch=master)](https://travis-ci.org/bitterbit/twitter-contest-bot)



Disclaimer
------------

This bot is written purely for educational purposes. I hold no liability for what you do with this bot or what happens to you by using this bot. Abusing this bot *can* get you banned from Twitter, so make sure to read up on [proper usage](https://support.twitter.com/articles/76915-automation-rules-and-best-practices) of the Twitter API.

License
------------

You can fork this repository on GitHub as long as it links back to this original repository. Do not sell this script as I would like the code to remain free.

Prerequisites
------------

  * TwitterAPI
  * textblob
  * Python 2.7
  
Configuration
------------

Open up `lib/config.py` and make the values correspond to your Twitter API credentials.

Installation
------------
From the command line:

	pip install TwitterAPI
	pip install -U textblob nltk
	python -m textblob.download_corpora
	
Then run:

	python main.py

Alternatives
-------------

If you're looking for similar projects in alternative languages, check these out:

* *(JavaScript)* https://github.com/raulrene/Twitter-ContestJS-bot
