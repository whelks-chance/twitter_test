import pprint
import twitter

from local_settings import *

api = twitter.Api(consumer_key=Consumer_Key_API_Key,
                      consumer_secret=Consumer_Secret_API_Secret,
                      access_token_key=Access_Token,
                      access_token_secret=Access_Token_Secret)

# print pprint.pformat(api.VerifyCredentials().__dict__)

# print pprint.pformat(api.GetRateLimitStatus())

user1 = 'keyz182'
user2 = 'whelks_chance'

user1 = 'wiserdnews'
user2 = 'esrc'

u1_ids = api.GetFriendIDs(screen_name=user1)

u2_ids = api.GetFriendIDs(screen_name=user2)


commons = []
for key in u1_ids:
    if key in u2_ids:
        commons.append(key)

# print commons
print 'Commonalities between {} and {} : {} / ({}) / {}'.format(user1, user2, len(u1_ids), len(commons), len(u2_ids))
print '{} : {}'.format(user1, float(len(commons))/len(u1_ids))
print '{} : {}'.format(user2, float(len(commons))/len(u2_ids))

u1_followed_by = api.GetFollowerIDs(screen_name=user1)

u2_followed_by = api.GetFollowerIDs(screen_name=user2)

commons_followed_by = []
for key in u1_followed_by:
    if key in u2_followed_by:
        commons_followed_by.append(key)

print 'Commonalities between {} and {} : {} / ({}) / {}'.format(user1, user2, len(u1_followed_by), len(commons_followed_by), len(u2_followed_by))
print '{} : {}'.format(user1, float(len(commons_followed_by))/len(u1_followed_by))
print '{} : {}'.format(user2, float(len(commons_followed_by))/len(u2_followed_by))

# print api.GetUser(user_id=commons[0])

# friends = api.GetFriends(screen_name='whelks_chance')[3]
#
# for friend in friends:
#     print pprint.pformat(friend.name)