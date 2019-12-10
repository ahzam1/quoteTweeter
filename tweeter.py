import tweepy
import requests
import time
# Authenticate to Twitter, removed for security purposes.
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
except:
    print("Error during authentication")
    exit()

# Function that fetches the quote from the API endpoint, and formats it as a tuple.
def getQuote(): 
    response = requests.get('https://quote-garden.herokuapp.com/quotes/random').json()
    if response['quoteAuthor'] == "":
        response['quoteAuthor'] = "Unknown"
    return (response['quoteText'], response['quoteAuthor'])

# Main function, loops until cancelled manually.
def main():
    while True: # this one runs forever
        while True: # this one runs until we get a valid lengthed tweet.
            tweet = getQuote() # calls our function above to get a tweet.
            tweetString = '"' + tweet[0] + '" - ' + tweet[1] # formats fetched tweet into a string, with quotation marks.
            # checks if string meets tweet length requirements, if it does, break out of this loop.
            if(len(tweetString) <280):
                break
        
        # make the tweet
        api.update_status(tweetString)

        # 12 hour delay until next tweet
        time.sleep(43200)

main()