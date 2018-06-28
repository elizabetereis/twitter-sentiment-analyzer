import tweepy
from textblob import TextBlob

consumer_key='0Bm3NYNmFgNTw29MZjJmKfu1j'
consumer_secret='fpVlzBkYeSoQPWIGPEUBpQFcUbxnzKMhr4typGHMDH9uHZ8osa'

access_token='1152174679-rvXu3baNFYuNyyIVPZ3IpJuh2Kgat6pFrYOYNd6'
access_token_secret='2tYySG0MJiodG0b2rKMmisZzK2DLYA4l3pe4IPGnWGeai'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

tweets = api.search(q='Neymar', count=100)

ftweets = open('tweets.csv','w')
fresults = open('results.csv','w') 

'''
-POLARITY - sendo -1.0 referente a 100% negativo e 1.0 a 100% positivo.
-SUBJECTIVITY - sendo 0.0 referente a 100% objetivo e 1.0 a 100% subjetivo. 
'''

for tweet in tweets:
    frase = TextBlob(tweet.text)
    if frase.detect_language() != 'en':
        traducao = TextBlob(str(frase.translate(to='en')))
        fresults.write('{0}'.format(traducao.sentiment)) 
        fresults.write('\n')
    else:
        fresults.write('{0}'.format(frase.sentiment)) 
        fresults.write('\n')
    
    s = tweet.text.replace ( "\n", " " ) 
    ftweets.write(s) 
    ftweets.write('\n') 

ftweets.close()
fresults.close()