# Custom Analytic Functions #
# Jon Puryear #
# This is a compliation of Custom Functions built to perform various data cleansing and acquisition tasks

def cleanString(incomingString):
    """ 
    Purpose:
    Cleans up a given input string, including making everything lowercase
    
    Module Dependencies:
     - None
     """
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

def fileDataLoad(filename, sheetname):
    """
    Purpose:
    Loads data from an Excel or CSV file into a Pandas Dataframe - CSV file import ignores the sheetname parameter
    The function determines Excel or CSV import by file extension. If the extenstion is XLSX then 
    it treats the file as Excel, if it is CSV, then it treats the file as a CSV file.
    
    Module Dependencies:
    - Pandas
    """
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
    """
    Purpose:
    This function is to specifically connect to the AMS Data Warehouse and returns a pandas dataframe
    
    WH_USER should be a string containing the userid including METNET in the following format "\METNET\userid"
    WH_PW should be a string containing the METNET password
    sql should be a string containing the SQL code that is to be executed. It is recommended that the SQL statement be tested
    prior to use in this function
    
    Module Dependencies:
    - Pandas
    - pymssql
    - json (if the user credentials should be read from a json file prior to passing to the function)
    
    """
    AMS_WH = 'AV-RISCDCSQL555\SQL555'
    conn = pym.connect(server = AMS_WH, user = WH_USER, password = WH_PW)
    input_DF = pd.read_sql(sql, conn)
    conn.close()
    return input_DF



