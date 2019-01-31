# Custom Analytic Functions #
# Jon Puryear #

def cleanString(incomingString):
    # Purpose: Cleans the input string.
    # Add or remove statements below as necessary depending on how much cleaning needs to be done.
    newstring = incomingString
    #newstring = re.sub('<[^>]*>', '' , newstring)
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
    #newstring = newstring.replace('br','')
    newstring = newstring.replace(',','')
    newstring = newstring.replace('.','')
    return newstring


def createStopWords():
    #define the Stop words used
    stopWords = (stopwords.words('english'))
    #add in words that should be added to the stopwords list. This will remove these words from the input list
    remove_words = ('us/eastern')
    stopWords.extend(remove_words)
    return stopWords

def fileDataLoad(filename, sheetname):
    #load data from an Excel or CSV file
    fileDF = []
    if filename[-4:].lower() == 'xlsx':
        fileDF = pd.read_excel(filename, sheet_name=sheetname)
        return fileDF
    elif filename[-3:].lower() == 'csv':
        fileDF = pd.read_csv(filename)
        return fileDF
    else:
        return print('filename not recognized')

def WarehouseDataExtract(WH_USER, WH_PW, sql):
    AMS_WH = 'AV-RISCDCSQL555\SQL555'
    conn = pym.connect(server = AMS_WH, user = WH_USER, password = WH_PW)
    input_DF = pd.read_sql(sql, conn)
    conn.close()
    return input_DF



