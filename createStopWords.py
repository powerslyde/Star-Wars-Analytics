def createStopWords(adds):
    """ 
    Purpose: 
    Creates a list of words that should be removed from a given list prior to text analysis.
    The "adds" parameter is for a string of words that should be added to the default stopwords corpus. 
    This is for building customized stopwords lists    
    
    Module Dependencies:
    - from nltk.corpus import stopwords
    """
    #define the Stop words used
    stopWords = (stopwords.words('english'))
    #add in words that should be added to the stopwords list. This will remove these words from the input list
    remove_words = adds
    stopWords.extend(remove_words)
    return stopWords