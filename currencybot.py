"""
REDDIT CURRENCY CONVERSION BOT V0.1
Parses submission titles for currency values and replies with a comment
containing converted values between USD, GBP, and EUR
using up-to-date exchange rates from the fixer.io API

DEPEDENCIES:

PRAW (Python Reddit API Wrapper)
OAuth2Util
currencyconverter library for python (available at my github profile - github.com/cp2846)

"""

import currencyconverter
import praw
import time
import OAuth2Util
import os

subreddits = ["test"]

r = praw.Reddit(user_agent = "Reddit Currency Exchange Bot by /u/Psychovyle")
o = OAuth2Util.OAuth2Util(r)

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
    print "no file"

else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = filter(None, posts_replied_to)

#save replied posts in txt file 
def writeFile():
    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")
                            
#generate and post reply
def generateComment(submission, results):
    signature = "***\n\nCurrent exchange rates from [fixer.io](http://fixer.io) | [Source](https://github.com/cp2846/reddit-currency-bot) | [Contact](https://www.reddit.com/message/compose/?to=Psychovyle)"
    conversions = ""
    
    for result in results:
        type = result[0]
        value = result[1]
        converted_values = currencyconverter.convert(type,value)
        conversions += "\n\n"+converted_values
        
    try:
        submission.add_comment(">"+submission.title+"\n\n"+conversions+"\n\n"+signature)
        print "Successfully added comment on submission "+submission.id
        posts_replied_to.append(submission.id)
        
    except:
        print "Error encountered on submission "+submission.id
           
def runBot():
    o.refresh(force=True)
    
    for subreddit in subreddits:
        print "Searching submissions in r/"+subreddit
        s = r.get_subreddit(subreddit)
        submissions = s.get_hot(limit=25)
        
        for submission in submissions:
            title_text = submission.title.encode("utf-8")
            detected_currency = currencyconverter.parseString(title_text)
            
            if len(detected_currency) > 0 and submission.id not in posts_replied_to:
                print "found one! attempting to reply... "
                generateComment(submission, detected_currency)
        
    writeFile()
    print "Sleeping... "
    time.sleep(3600)

while True:
    runBot()
