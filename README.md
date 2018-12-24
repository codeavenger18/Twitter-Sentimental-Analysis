# Twitter-Sentimental-Analysis
Here we are performing sentimental analysis on Tweets .

Here we are fetching tweets from Twitter with the help of tweepy library and performing sentiment analysis ,we are storing the result in report.csv and for demo version an image is also uploaded..

And then we will pre-process the tweets for our sentiment algorithm .

In pre-processing we will perform  :-

A) Removing Twitter Handles (@user)

B) Removing Punctuations, Numbers, and Special Characters

C) Removing Short Words

We have to be a little careful here in selecting the length of the words which we want to remove. So, I have decided to remove all the words having length 3 or less. For example, terms like “hmm”, “oh” are of very little use. It is better to get rid of them.

D) Tokenization

Now we will tokenize all the cleaned tweets in our dataset. Tokens are individual terms or words, and tokenization is the process of splitting a string of text into tokens.

E) Stemming

Stemming is a rule-based process of stripping the suffixes (“ing”, “ly”, “es”, “s” etc) from a word. For example, For example – “play”, “player”, “played”, “plays” and “playing” are the different variations of the word – “play”.

After Pre-Processing our tweets we will use TextBlob library which is advance version of NLP and there we will check the sentiment of the tweets .

Our final result is displayed with the help of graph.

Pre-requisite :-

->tweepy(token id and keys should be requested from twitter)

->nltk

->textblob

->pandas

->numpy

->matplotlib

for runnng the code :-

->python t1.py
