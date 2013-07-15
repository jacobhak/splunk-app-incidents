from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="qwVXeuKs6Z5Wy1nxMbpqA"
consumer_secret="5HMCIe1MgCsPYqaTk8H4YpZgf7ucvGdranDyE4sboSA"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="49442495-thSv09wPgEYdJ8pMOa3l0m4uS5tHcgGYGdqmcVVxS"
access_token_secret="Khe8w5aq0lzVaMzVdq87sbtGdyD3QrSnjJB0VPXBWY"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    It only accepts tweets that has geolocation data.

    """
    def on_data(self, data):
        parsed = json.loads(data)
        geo = None
        try:
            geo = parsed['geo']
        except (KeyError):
            return True
        if (geo is not None):
            print data
            return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.sample()
