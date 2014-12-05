import pprint
import twitter

from local_settings import *

api = twitter.Api(consumer_key=Consumer_Key_API_Key,
                      consumer_secret=Consumer_Secret_API_Secret,
                      access_token_key=Access_Token,
                      access_token_secret=Access_Token_Secret)

print pprint.pformat(str(api.VerifyCredentials()))
