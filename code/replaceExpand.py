import re

positive=0
negative=1
neutral=2
total=3




def removeNonEnglishWords(tweet,token):
    """remove the non-english or better non-ascii characters
    takes as input a list of words in tweet and a list of corresponding tokens, 
    not using tokens now but may use in future
    and return the modified list of token and words"""

    newTweet=[]
    newToken=[]
    for i in range(len(tweet)):
        chk=re.match(r'([a-zA-z0-9 \+\?\.\*\^\$\(\)\[\]\{\}\|\\/:;\'\"><,.#@!~`%&-_=])+$',tweet[i])
        if chk:
            newTweet.append(tweet[i])
            newToken.append(token[i])
    return newTweet, newToken




def removeStopWords(tweet, token, stopWordsDict):    
    """remove the stop words ,
    takes as input a list of words in tweet ,a list of corresponding tokens and a stopWords Dictonary, 
    and return the modified list of token and words"""

    newTweet=[]
    newToken=[]
    for i in range(len(tweet)):
        if stopWordsDict[tweet[i].lower()] == 0:
            newTweet.append(tweet[i])
            newToken.append(token[i])
    return newTweet, newToken




def replaceEmoticons(emoticonsDict,tweet,token):
    """replaces the emoticons present in tweet with its polarity
    takes as input a emoticons dict which has emoticons as key and polarity as value
    and a list which contains words in tweet and return list of words in tweet after replacement"""
    
    for i in range(len(tweet)):
        if tweet[i] in emoticonsDict:
            tweet[i]=emoticonsDict[tweet[i]]
            token[i]='E'
    return tweet,token




def expandAcronym(acronymDict,tweet,token):
    """expand the Acronym present in tweet 
    takes as input a acronym dict which has acronym as key and abbreviation as value,
    a list which contains words in tweet and a list of token and return list of words in tweet after expansion and tokens"""
    
    newTweet=[]
    newToken=[]
    for i in range(len(tweet)):
        word=tweet[i].lower()
        if word in acronymDict:
            newTweet+=acronymDict[word].split()
            newToken+=[token[i]]*len(acronymDict[word].split())
        else:
            newTweet+=[tweet[i]]
            newToken+=[token[i]]
    return newTweet, newToken




def replaceUrl(tweet, token):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement 
    www.*.* ->'URL' """
    for i in range(len(tweet)):
        if token[i]=='U':
            tweet[i]='U'
    return tweet




def replaceHashtag(tweet, token):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement 
    #*** - > # """
    for i in range(len(tweet)):
        if token[i]=='#' or tweet[i].startswith('#'):
            token[i]='#'
            tweet[i]=tweet[i][1:]
    return tweet,token




def replaceTarget(tweet, token):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement 
    @**** -> @ """
    for i in range(len(tweet)):
        if token[i]=='@' or tweet[i].startswith('@'):
            token[i]='@'
            tweet[i]=tweet[i][1:]
    return tweet,token



def replaceRepetition(tweet):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement 
       eg coooooooool -> coool """
    for i in range(len(tweet)):
        x=list(tweet[i])
        if len(x)>3:
            for j in range(3,len(x)):
                if(x[j-3].lower()==x[j-2].lower()==x[j-1].lower()==x[j].lower()):
                    x[j-3]=''
            tweet[i]=''.join(x)

    return tweet




def replaceNegation(tweet):
    """takes as input a list which contains words in tweet and return list of words in tweet after replacement of "not","no","n't","~"
       eg isn't -> negation 
       not -> negation """
    
   
    for i in range(len(tweet)):
        if(tweet[i].lower()=="no" or tweet[i].lower()=="not" or tweet[i][0].lower()=="~" or tweet[i].lower().count("n't")>0):
            tweet[i]='negation'

    return tweet




def preprocesingTweet(tweet, token, stopWords, emoticonsDict, acronymDict):
    """preprocess the tweet """
    tweet, token = removeNonEnglishWords(tweet, token)
    tweet, token = expandAcronym(acronymDict,tweet,token)
    tweet = replaceNegation(tweet)
    tweet, token = removeStopWords(tweet, token, stopWords)
    tweet,token = replaceEmoticons(emoticonsDict, tweet,token)
    tweet = replaceRepetition(tweet)
    tweet = replaceUrl (tweet, token)
    tweet,token = replaceHashtag (tweet, token)
    tweet,token = replaceTarget (tweet, token)

    return tweet,token
