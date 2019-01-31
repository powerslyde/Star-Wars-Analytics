def WarehouseDataExtract(WH_USER, WH_PW, sql):
    r"""
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
