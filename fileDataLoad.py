def fileDataLoad(filename, sheetname):
    """
    Purpose:
    Loads data from an Excel or CSV file into a Pandas Dataframe - CSV file import ignores the sheetname parameter
    The function determines Excel or CSV import by file extension. If the extenstion is XLSX then 
    it treats the file as Excel, if it is CSV, then it treats the file as a CSV file.
    
    Module Dependencies:
    - Pandas
    """
    import pandas as pd
    fileDF = []
    if filename[-4:].lower() == 'xlsx':
        fileDF = pd.read_excel(filename, sheet_name=sheetname)
        return fileDF
    elif filename[-3:].lower() == 'csv':
        fileDF = pd.read_csv(filename)
        return fileDF
    else:
        return print('filename not recognized')
