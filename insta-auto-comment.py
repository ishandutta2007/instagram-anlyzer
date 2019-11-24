from instagram_private_api import Client, ClientCompatPatch

user_name = ''
password = ''

api = Client(user_name, password)
posts_counter = 0
ads_counter = 0
verified_counter = 0
# post = api.post_comment('2168883123794135818', '😃')
# comments = api.media_comments('2179941564690764534')
# #
# a = 4;
# results = api.feed_timeline()
# next_max_id = results['next_max_id']
# items = [item for item in results.get('feed_items', []) if item.get('media_or_ad')]
# for item in items:
#     # Manually patch the entity to match the public api as closely as possible, optional
#     # To automatically patch entities, initialise the Client with auto_patch=True
#     posts_counter += 1
#     ClientCompatPatch.media(item['media_or_ad'])
#     if not item['media_or_ad']['user']['friendship_status']['following']:
#         ads_counter += 1
#     elif item['media_or_ad']['user']['is_verified']:
#         verified_counter += 1
#     print(item['media_or_ad']['user']['username'])
next_max_id = ''
for i in range(1, 10):
    # results = api.feed_timeline(seen_posts=watched[:-1])
    results = api.feed_timeline(max_id=next_max_id)
    next_max_id = results['next_max_id']
    items = [item for item in results.get('feed_items', []) if item.get('media_or_ad')]
    for item in items:
        # Manually patch the entity to match the public api as closely as possible, optional
        # To automatically patch entities, initialise the Client with auto_patch=True
        posts_counter += 1
        ClientCompatPatch.media(item['media_or_ad'])
        if not item['media_or_ad']['user']['friendship_status']['following']:
            ads_counter += 1
        elif item['media_or_ad']['user']['is_verified']:
            verified_counter += 1
        #print(item['media_or_ad']['user']['username'])
print('stats : ' + str(posts_counter) + ' posts total, from all of them : ' + str(verified_counter + ads_counter)
      +" are ads or verified " + str(verified_counter) + '(verified) ' + str(ads_counter) + '(ads) ~ ' + str(100*(verified_counter + ads_counter)/posts_counter)+'%')
