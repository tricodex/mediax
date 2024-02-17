import os
import tweepy

# Setting the environment variables
os.environ['TWITTER_API_KEY'] = "xxx"
os.environ['TWITTER_API_SECRET_KEY'] = "xxx"
os.environ['TWITTER_ACCESS_TOKEN'] = "xxx"
os.environ['TWITTER_ACCESS_TOKEN_SECRET'] = "xxx"

# Fetch your credentials from environment variables or other configuration
consumer_key = os.getenv('TWITTER_API_KEY')
consumer_secret = os.getenv('TWITTER_API_SECRET_KEY')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')

# Initialize the tweepy Client with OAuth 1.0a User Context
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

image_path="xxx"
tweet_text="xxx"

tweepy_auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
tweepy_api = tweepy.API(tweepy_auth)

# Upload media using Tweepy (Twitter API v1.1)
media = tweepy_api.media_upload(image_path)
media_id = media.media_id

response = client.create_tweet(text=tweet_text, media_ids=[media.media_id])

print("Tweet posted:", response)

# Save response in a txt file
with open('posts.txt', 'a') as file:
    post_number = len(open('posts.txt').readlines()) + 1
    post_name = f"Post:{post_number}Tweet:{tweet_text.replace(' ', '_')}"
    file.write(f"{post_name}: {response}\n")
