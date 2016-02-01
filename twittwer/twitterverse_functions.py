"""
Type descriptions of Twitterverse and Query dictionaries
(for use in docstrings)

Twitterverse dictionary:  dict of {str: dict of {str: object}}
    - each key is a username (a str)
    - each value is a dict of {str: object} with items as follows:
        - key "name", value represents a user's name (a str)
        - key "location", value represents a user's location (a str)
        - key "web", value represents a user's website (a str)
        - key "bio", value represents a user's bio (a str)
        - key "following", value represents all the usernames of users this 
          user is following (a list of str)
       
Query dictionary: dict of {str: dict of {str: object}}
   - key "search", value represents a search specification dictionary
   - key "filter", value represents a filter specification dictionary
   - key "present", value represents a presentation specification dictionary

Search specification dictionary: dict of {str: object}
   - key "username", value represents the username to begin search at (a str)
   - key "operations", value represents the operations to perform (a list of str)

Filter specification dictionary: dict of {str: str}
   - key "following" might exist, value represents a username (a str)
   - key "follower" might exist, value represents a username (a str)
   - key "name-includes" might exist, value represents a str to match (a case-insensitive match)
   - key "location-includes" might exist, value represents a str to match (a case-insensitive match)

Presentation specification dictionary: dict of {str: str}
   - key "sort-by", value represents how to sort results (a str)
   - key "format", value represents how to format results (a str)
       
"""
     
# --- Sorting Helper Functions ---
def tweet_sort(twitter_data, results, cmp):
    """ (Twitterverse dictionary, list of str, function) -> NoneType
    
    Sort the results list using the comparison function cmp and the data in 
    twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> result_list = ['c', 'a', 'b']
    >>> tweet_sort(twitter_data, result_list, username_first)
    >>> result_list
    ['a', 'b', 'c']
    >>> tweet_sort(twitter_data, result_list, name_first)
    >>> result_list
    ['b', 'a', 'c']
    """
    
    # Insertion sort
    for i in range(1, len(results)):
        current = results[i]
        position = i
        while position > 0 and cmp(twitter_data, results[position - 1], current) > 0:
            results[position] = results[position - 1]
            position = position - 1 
        results[position] = current  
            
def more_popular(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int
    
    Return -1 if user a has more followers than user b, 1 if fewer followers, 
    and the result of sorting by username if they have the same, based on the 
    data in twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> more_popular(twitter_data, 'a', 'b')
    1
    >>> more_popular(twitter_data, 'a', 'c')
    -1
    """
    
    a_popularity = len(all_followers(twitter_data, a)) 
    b_popularity = len(all_followers(twitter_data, b))
    if a_popularity > b_popularity:
        return -1
    if a_popularity < b_popularity:
        return 1
    return username_first(twitter_data, a, b)
    
def username_first(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int
    
    Return 1 if user a has a username that comes after user b's username 
    alphabetically, -1 if user a's username comes before user b's username, 
    and 0 if a tie, based on the data in twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> username_first(twitter_data, 'c', 'b')
    1
    >>> username_first(twitter_data, 'a', 'b')
    -1
    """
    
    if a < b:
        return -1
    if a > b:
        return 1
    return 0

def name_first(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int
        
    Return 1 if user a's name comes after user b's name alphabetically, 
    -1 if user a's name comes before user b's name, and the ordering of their
    usernames if there is a tie, based on the data in twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> name_first(twitter_data, 'c', 'b')
    1
    >>> name_first(twitter_data, 'b', 'a')
    -1
    """
    
    a_name = twitter_data[a]["name"]
    b_name = twitter_data[b]["name"]
    if a_name < b_name:
        return -1
    if a_name > b_name:
        return 1
    return username_first(twitter_data, a, b)       

def process_data(file):
    """ (file open for reading) -> Twitterverse dictionary
    The function reads all the line from a opened file and process the data into a dictrionary with
    the form of dict of {str: dict of {str: object}}
    
    :return twitter_data: a dictionary of the informations from the file
    
    """
    twitter_data = {}
    line = file.readline()
    while line:
        user_name = line.strip()
        real_name = file.readline().strip()
        location = file.readline().strip()
        web = file.readline().strip()
        line = file.readline()
        bio =''
        while 'ENDBIO' not in line:
            bio += line
            line = file.readline()
        bio = bio.strip()
        following =[]
        line = file.readline()
        while "END" not in line:
            following.append(line.strip())
            line = file.readline()
        twitter_data[user_name]={'name':real_name,'bio':bio,'location':location,'web':web,'following':following}
        line = file.readline()
    return twitter_data

def process_query(file):
    """ (file open for reading) -> Twitterverse dictionary
    
    The function reads all the line from a opened file and process the data into a dictrionary with
    the form of dict of {str: dict of {str: object},str: dict of {str: object},str: dict of {str: object}}
    
    :return query_dic: a dictionary of the informations from the file
    
    """    
    line = file.readline()
    username =''
    operations =[]
    fileter_query ={}
    present_query ={}
    query_dic = {}
    while line.strip() != 'FILTER':
        if username =='':
            username = file.readline().strip()
        else:
            operations.append(line.strip())
        line = file.readline()
    line = file.readline()
    while line.strip() != 'PRESENT' :
        filter_key = line.strip().split(' ',1)
        fileter_query[filter_key[0]] = filter_key[1]
        line = file.readline()
    line = file.readline()
    while line :
        present_key = line.strip().split(' ',1)
        present_query[present_key[0]] = present_key[1]
        line = file.readline()
    query_dic['search']={'username':username,'operations':operations}
    query_dic['filter']= fileter_query
    query_dic['present']= present_query
    return query_dic

def all_followers(twitter_data, user_name):
    """ (Twitterverse dictionary, str) -> list of str
    
    find all the users from the twitter_data that is following the user_name, and return them in a list of str
    >>> twitter_data = {'tomCruise': {'following': ['katieH'], 'name': 'Tom Cruise', \
    'bio': 'Official TomCruise.com crew tweets.', \
    'web': 'http://www.tomcruise.com','location': 'Los Angeles, CA'}, \
    'katieH': {'following': [], 'name': 'Katie Holmes','bio': '', \
    'web': 'www.tomkat.com', 'location': ''}}   
    >>> all_followers(twitter_data,'katieH')
    ['tomCruise']
    
    """
    follower_list = []
    for key in twitter_data:
        if user_name in twitter_data[key]['following']:
            follower_list.append(key)
    return follower_list

def all_following(twitter_data, user_name):
    """ (Twitterverse dictionary, str) -> list of str

    find all the users from the user_name is following from the twittwer_data and return them as a list of str
    >>> twitter_data = {'tomCruise': {'following': ['katieH'], 'name': 'Tom Cruise', \
    'bio': 'Official TomCruise.com crew tweets.', \
    'web': 'http://www.tomcruise.com','location': 'Los Angeles, CA'}, \
    'katieH': {'following': [], 'name': 'Katie Holmes','bio': '', \
    'web': 'www.tomkat.com', 'location': ''}}
    >>> all_following(twitter_data,'tomCruise')
    ['katieH']

    """    
    following_list =[]
    for user in twitter_data[user_name]['following']:
        following_list.append(user)
    return following_list

def get_search_results(twitter_data, query_data):
    """ (Twitterverse dictionary, search specification dictionary) -> list of str
    Perform the specific search operation from the query_data and apply it on twitter_data to generate
    a list of user name that matches the search
    
    >>> twitter_data = {'tomCruise': {'following': ['katieH'], 'name': 'Tom Cruise', \
    'bio': 'Official TomCruise.com crew tweets.', \
    'web': 'http://www.tomcruise.com','location': 'Los Angeles, CA'}, \
    'katieH': {'following': [], 'name': 'Katie Holmes','bio': '', \
    'web': 'www.tomkat.com', 'location': ''}}
    >>> query_data = {'operations': ['following'], 'username': 'tomCruise'}
    >>> get_search_results(twitter_data, query_data)
    ['katieH']
    """
    user_name_list = [query_data['username']]
    operation_list = query_data['operations']
    for operation in operation_list:
        result_list =[]
        if operation == 'following':
            for user_name in user_name_list :
                for user_follows in all_following(twitter_data,user_name):
                    result_list.append(user_follows)
            user_name_list = list(set(result_list))
        else:
            for user_name in user_name_list:
                for followers in all_followers(twitter_data,user_name):
                    result_list.append(followers)
            user_name_list = list(set(result_list))
    return user_name_list

def get_filter_results(twitter_data,search_result,query_data):
    """ (Twitterverse dictionary, list of str, filter specification dictionary) -> list of str
    Perform the specific filter operation from the query_data and combining with the data from
    twitter_data to filter user_names in the search_result to generate a new 
    list of user name that matches the filter

    >>> twitter_data = {'tomCruise': {'following': ['katieH'], 'name': 'Tom Cruise', \
    'bio': 'Official TomCruise.com crew tweets.', \
    'web': 'http://www.tomcruise.com','location': 'Los Angeles, CA'}, \
    'katieH': {'following': [], 'name': 'Katie Holmes','bio': '', \
    'web': 'www.tomkat.com', 'location': ''}}
    >>> search_result = ['tomCruise']
    >>> query_data = {'following':'katieH'}
    >>> get_filter_results(twitter_data, search_result, query_data)
    ['tomCruise']
    """    
    user_name_list = search_result
    for key in query_data:
        filtered_list = []
        if key == 'name-includes':
            for user in user_name_list:
                if query_data[key] in user:
                    filtered_list.append(user)
        elif key == 'location-includes':
            for user in user_name_list:
                if query_data[key] in twitter_data[user]['location']:
                    filtered_list.append(user)
        elif key == 'following':
            for user in user_name_list:
                if query_data[key] in twitter_data[user]['following']:
                    filtered_list.append(user)
        elif key =='follower':
            for user in user_name_list:
                if user in twitter_data[query_data[key]]['following']:
                    filtered_list.append(user)
        user_name_list = filtered_list
    return user_name_list


def generate_long_format(twitter_data,sort_list):
    """(Twitterverse dictionary, list of str) -> str
    Using the data from the twitter_data generate a string fora ach user in the sor_list that
    includes all the user's information
    >>> twitter_data = {'tomCruise': {'following': ['katieH'], 'name': 'Tom Cruise', \
    'bio': 'Official TomCruise.com crew tweets.', \
    'web': 'http://www.tomcruise.com','location': 'Los Angeles, CA'}, \
    'katieH': {'following': [], 'name': 'Katie Holmes','bio': '', \
    'web': 'www.tomkat.com', 'location': ''}}
    >>> sort_list = ['tomCruise']
    >>> print(generate_long_format(twitter_data,sort_list).strip())
    ----------
    tomCruise
    name: Tom Cruise
    location: Los Angeles, CA
    website: http://www.tomcruise.com
    bio:
    Official TomCruise.com crew tweets.
    following: ['katieH']
    ----------
    """
    long_format = '----------\n'
    for user in sort_list:
        long_format += user + '\n'
        long_format += 'name: '+ twitter_data[user]['name'] + '\n'
        long_format += 'location: '+ twitter_data[user]['location'] + '\n'
        long_format += 'website: '+ twitter_data[user]['web'] + '\n'
        long_format += 'bio:\n'+ twitter_data[user]['bio'] + '\n'
        long_format += 'following: '+ str(twitter_data[user]['following']) + '\n'
        long_format += '----------\n'
    return long_format

def get_present_string(twitter_data,filter_results,query_data):
    """ (Twitterverse dictionary, list of str, presentation specification dictionary) -> str
    Perform the specific present operation from the query_data and combining with the data from
    twitter_data to sort user_names in the search_result to generate a new 
    str that all the user_names sorterd as the requirement

    >>> twitter_data = {'tomCruise': {'following': ['katieH'], 'name': 'Tom Cruise', \
    'bio': 'Official TomCruise.com crew tweets.', \
    'web': 'http://www.tomcruise.com','location': 'Los Angeles, CA'}}
    >>> filter_results = ['tomCruise']
    >>> query_data = {'sort-by': 'username', 'format': 'long'}
    >>> print(get_present_string(twitter_data, filter_results, query_data).strip())
    ----------
    tomCruise
    name: Tom Cruise
    location: Los Angeles, CA
    website: http://www.tomcruise.com
    bio:
    Official TomCruise.com crew tweets.
    following: ['katieH']
    ----------
    """    
    sort_by = query_data['sort-by']
    sort_list = filter_results
    if sort_by == 'username':
        tweet_sort(twitter_data, sort_list, username_first)
    elif sort_by =='name':
        tweet_sort(twitter_data, sort_list, name_first)
    elif sort_by == 'popularity':
        tweet_sort(twitter_data, sort_list, more_popular)
    format_by = query_data['format']
    if format_by == 'short':
        return str(sort_list)
    else:
        return generate_long_format(twitter_data,sort_list)

if __name__ == "__main__":
    import doctest
    doctest.testmod()