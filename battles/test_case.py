import tweepy
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
from twitter_api_keys import ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

class MyListener(StreamListener):
        def on_status(self, status):
                try:
                        print(status.text)
                except UnicodeEncodeError:
                        pass

        def on_error(self, status_code):
                if status_code == 420:
                        return False

myListener = MyListener()
stream = Stream(auth = api.auth, listener=myListener)
##stream.filter(track=['love'], async=True)
##stream.filter(track=['cat'], async=True)

def getTweets(*args):
        
##        tweets = ', '.join(arg for arg in args)
##        stream.filter(track=[tweets])

getTweets('python', 'java', 'haskell')
