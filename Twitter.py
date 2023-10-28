import tkinter as tk
import tweepy

# Function to save API credentials


def save_credentials():
    global consumer_key, consumer_secret, access_token, access_token_secret
    consumer_key = consumer_key_entry.get()
    consumer_secret = consumer_secret_entry.get()
    access_token = access_token_entry.get()
    access_token_secret = access_token_secret_entry.get()
    status_label.config(text="Credentials saved successfully!")

# Function to post a tweet


def post_tweet():
    tweet_text = tweet_entry.get()
    api.update_status(status=tweet_text)
    status_label.config(text="Tweet posted successfully!")

# Function to retweet a tweet


def retweet():
    tweet_id = retweet_entry.get()
    api.retweet(tweet_id)
    status_label.config(text="Retweet successful!")

# Function to follow a user


def follow_user():
    user_id = follow_entry.get()
    api.create_friendship(user_id)
    status_label.config(text=f"Followed user {user_id}!")

# Function to like a tweet


def like_tweet():
    tweet_id = like_entry.get()
    api.create_favorite(tweet_id)
    status_label.config(text="Liked tweet!")


# Initialize Tweepy API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Create a GUI window
window = tk.Tk()
window.title("Twitter Bot")

# Create labels and entry fields for API credentials
consumer_key_label = tk.Label(window, text="Consumer Key:")
consumer_key_label.pack()
consumer_key_entry = tk.Entry(window)
consumer_key_entry.pack()

consumer_secret_label = tk.Label(window, text="Consumer Secret:")
consumer_secret_label.pack()
consumer_secret_entry = tk.Entry(window)
consumer_secret_entry.pack()

access_token_label = tk.Label(window, text="Access Token:")
access_token_label.pack()
access_token_entry = tk.Entry(window)
access_token_entry.pack()

access_token_secret_label = tk.Label(window, text="Access Token Secret:")
access_token_secret_label.pack()
access_token_secret_entry = tk.Entry(window)
access_token_secret_entry.pack()

credentials_button = tk.Button(
    window, text="Save Credentials", command=save_credentials)
credentials_button.pack()

# Create labels and entry fields for tweet actions
tweet_label = tk.Label(window, text="Tweet:")
tweet_label.pack()
tweet_entry = tk.Entry(window)
tweet_entry.pack()
tweet_button = tk.Button(window, text="Tweet", command=post_tweet)
tweet_button.pack()

retweet_label = tk.Label(window, text="Retweet (Tweet ID):")
retweet_label.pack()
retweet_entry = tk.Entry(window)
retweet_entry.pack()
retweet_button = tk.Button(window, text="Retweet", command=retweet)
retweet_button.pack()

follow_label = tk.Label(window, text="Follow User (User ID):")
follow_label.pack()
follow_entry = tk.Entry(window)
follow_entry.pack()
follow_button = tk.Button(window, text="Follow", command=follow_user)
follow_button.pack()

like_label = tk.Label(window, text="Like Tweet (Tweet ID):")
like_label.pack()
like_entry = tk.Entry(window)
like_entry.pack()
like_button = tk.Button(window, text="Like", command=like_tweet)
like_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()
