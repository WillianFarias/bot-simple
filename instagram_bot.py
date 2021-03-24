from instapy import InstaPy

session = InstaPy(username = "", password = "") #headLess_browser = True
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)

session.set_do_follow(True, percentage = 100)
session.like_by_tags(["bmw", "steam"], amount = 3)
session.set_dont_like(["nsfw"])

#session.unfollow_users(amount=6, allFollowing=True, sleep_delay=60)

session.end()
