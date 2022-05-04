"""Connector and methods accessing Snowflake"""
import os
import snowflake


class SnowflakeConnector():
    """
    Class for inetracting with Snowflake
    """
    def __init__(self, snowflake_user: str, snowflake_password: str, account: str, warehouse: str, database: str, schema):
        """
        Constructor for SnowflakeConnector

        :param
        """
      
        self.account = account
        self.warehouse = warehouse
        self.database = database
        # AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
        # AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

        self._connect = snowflake.connector.connect(user = os.environ[snowflake_user], 
                                                   password = os.environ[snowflake_password],
                                                   account = account,
                                                   warehouse = warehouse,
                                                   database = database
                                                   )
        self._cursor = self._connect.cursor()

    def execute_sql(self, sql_statement):
        
        try:
            results = self._cursor.execute(sql_statement).fetchone() # cur.execute_async() for an asynchronous Query
        finally:
            self._cursor.close()
        
        return results





