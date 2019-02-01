def cleanString(incomingString):
    """ 
    Purpose:
    Cleans up a given input string, including making everything lowercase
    
    Module Dependencies:
     - None
    """
    newstring = incomingString
    newstring = newstring.lower()
    newstring = newstring.encode('ascii', 'ignore').decode('latin-1')
    newstring = newstring.replace('!','')
    newstring = newstring.replace('@','')
    newstring = newstring.replace('#','')
    newstring = newstring.replace('%','')
    newstring = newstring.replace('^','')
    newstring = newstring.replace('&','and')
    newstring = newstring.replace('*','')
    newstring = newstring.replace('(','')
    newstring = newstring.replace('$','')
    newstring = newstring.replace(')','')
    newstring = newstring.replace('+','')
    newstring = newstring.replace('=','')
    newstring = newstring.replace('?','')
    newstring = newstring.replace('\'','')
    newstring = newstring.replace('\'','')
    newstring = newstring.replace('{','')
    newstring = newstring.replace('}','')
    newstring = newstring.replace('[','')
    newstring = newstring.replace(']','')
    newstring = newstring.replace('<','')
    newstring = newstring.replace('>','')
    newstring = newstring.replace('~','')
    newstring = newstring.replace('`','')
    newstring = newstring.replace(':','')
    newstring = newstring.replace(';','')
    newstring = newstring.replace('|','')
    newstring = newstring.replace('\\','')
    newstring = newstring.replace('/','')
    newstring = newstring.replace('-','')
    newstring = newstring.replace('_','')
    newstring = newstring.replace(',','')
    newstring = newstring.replace('.','')
    return newstring
