# Star-Wars-Analytics
Projects and Other Items related to Data Analytics

This repo is for showing my Star Wars Analytics - a series of Data Analysis modules to test out "generic" Python Analyis modules
It's star wars because the test datasets are based on different flavors of Star Wars data


## Custom Functions ##

**cleanString**

Purpose:
Cleans up a given input string, including making everything lowercase

Module Dependencies:
- None

**createStopWords**

Purpose: 
Creates a list of words that should be removed from a given list prior to text analysis.
The "adds" parameter is for a string of words that should be added to the default stopwords corpus. 
This is for building customized stopwords lists    
    
Module Dependencies:
- from nltk.corpus import stopwords

**fileDataLoad**

Purpose:
Loads data from an Excel or CSV file into a Pandas Dataframe - CSV file import ignores the sheetname parameter
The function determines Excel or CSV import by file extension. If the extenstion is XLSX then 
it treats the file as Excel, if it is CSV, then it treats the file as a CSV file.
    
Module Dependencies:
- Pandas

**WarehouseDataExtract**

Purpose:
This function is to specifically connect to the AMS Data Warehouse and returns a pandas dataframe
    
WH_USER should be a string containing the userid including METNET in the following format "\METNET\userid"
WH_PW should be a string containing the METNET password
sql should be a string containing the SQL code that is to be executed. It is recommended that the SQL statement be tested prior to use in this function
    
Module Dependencies:
- Pandas
- pymssql
- json (if the user credentials should be read from a json file prior to passing to the function)
