import math

# Use these constants in place of int and string literals to make your code
# easier to read, and less error prone.
# Note that we are using a shorter tweet length to make testing easier.
MAX_TWEET_LENGTH = 50
HASH = '#'


# Add your own constants here, as needed

def contains_owly_url(tweet):
    """ (str) -> bool

    Return True if and only if tweet contains a link to an ow.ly URL of the 
    form 'http://ow.ly/'.

    Assume tweet is a valid tweet.

    >>> contains_owly_url('Cook receives award: http://ow.ly/WXJFN')
    True
    >>> contains_owly_url('http://ow.ly/VGpA9 Team to transform U of T campus')
    True
    >>> contains_owly_url('Fairgrieve to play in goal http://www.nhl.com')
    False
    """

    # Complete this function body.
    if 'http://ow.ly/' in tweet :
        return True
    else :
        return False
    
# Now define the other functions described in the handout.

def is_valid_tweet(tweet):
    """ (str) -> bool
    
    Return True if and only if the tweet 
    contains between 1 and MAX_TWEET_LENGTH characters, inclusive.
    
    >>> is_valid_tweet('Cook receives award: http://ow.ly/WXJFN')
    True
    >>> is_valid_tweet('http://ow.ly/VGpA9 Team to transform U of T campus ....')
    False
    """
    if len(tweet) > 0 and len(tweet) <= MAX_TWEET_LENGTH:
        return True
    else:
        return False
    
def add_hashtag(tweet, hash_tag) :
    """ (str,str) -> str
    
    return a new str with the hash_tag added at the end of the tweet 
    with a space and a hash symbol at the front of the hast_tag.
    If the new tweet exceeds the valid length, return the orgina tweet.
    
    >>> add_hashtag('Cook receives award: http://ow.ly/WXJFN', 'tag')
    'Cook receives award: http://ow.ly/WXJFN #tag'
    >>> add_hashtag('http://ow.ly/VGpA9 Team to transform U of T campus','tag')
    'http://ow.ly/VGpA9 Team to transform U of T campus'
    """    
    
    if len(tweet) + len (hash_tag) < MAX_TWEET_LENGTH -1 :
        return tweet + ' #' + hash_tag
    else :
        return tweet

def contains_hashtag(tweet, hash_tag):
    """ (str, str) -> bool
    
    The first parameter represents a valid tweet, and second parameter 
    represents a hashtag. Return True if and only if the tweet contains 
    the hashtag.
    
    >>>contains_hashtag('i love canada #canada','#canada')
    True
    >>>contains_hashtag('I like #csc108','#csc')
    False
    """
    splited_tweet = tweet.split()
    if hash_tag in splited_tweet :
        return True
    else :
        return False

def report_longest(tweet_one, tweet_two):
    """ (str, str) -> str
    
    Return 'Tweet 1' if the first tweet is longer than the second, 
    'Tweet 2' if the second tweet is longer than the first, 
    and 'Same length' if the tweets have the same length.
    
    >>>report_longest('abc', 'ab')
    "Tweet 1"
    >>>report_longest('abc', 'abcd')
    "Tweet 2"
    >>>report_longest('abc', 'def')
    "Same length"
    """
    if len(tweet_one) > len(tweet_two):
        return "Tweet 1"
    elif len(tweet_two) > len(tweet_one):
        return "Tweet 2"
    else :
        return "Same length"

def num_tweets_required(message):
    """ (str) -> int
    Return the minimum number of tweets that would be required to 
    communicate all of the message.    
    
    >>>num_tweets_required('Cook receives award: http://ow.ly/WXJFN')
    1
    >>>num_tweets_required('http://ow.ly/VGpA9 Team to transform U of T campus ....')
    2
    """
    return math.ceil(len(message)/MAX_TWEET_LENGTH)

def get_nth_tweet(message,index):
    """
    return the nth valid tweet in the sequence of tweets by spliting the message
    using the valid maximum length 
    
    >>>get_nth_tweet('Cook receives award: http://ow.ly/WXJFN',1)
    'Cook receives award: http://ow.ly/WXJFN'
    >>>get_nth_tweet('http://ow.ly/VGpA9 Team to transform U of T campus ....',2)
    ' ....'
    """
    splited_message = []
    while message:
        splited_message.append(message[:MAX_TWEET_LENGTH])
        message = message[MAX_TWEET_LENGTH: ]
    return splited_message[index-1]
