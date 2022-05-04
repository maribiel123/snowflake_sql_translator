"""Running the translation of SQL UDH scripts into the Snowflake dialect """
import argparse
import logging
import logging.config

import yaml
from translator.sql_translator import SqlTranslator
import sqlparse
from sqlparse.tokens import Keyword, DML

def main():
    """
    entry point to run translation job
    1) Open migration file 
    2) Iterate over SQL statement
    3) Translate each SQL statement
    4) Write translated to file
    5) 
    """
    # Loading configuration, parsing YAML file
    # config_path = 'C:/python/snowflake_sql_translator/configs/sql_translator_config.yml'
    # config = yaml.safe_load(open(config_path))
    
    sql = """SELECT MAX(A), getdate, CASE WHEN A is TRUE then 'A' END FROM t_tab WHERE 1 = 1;"""
 
    translator = SqlTranslator(sql=sql)
    sql_str = translator.sql()
    print(sql_str)
    
if __name__ == '__main__':
    main()