"""
Translate a SQL string to Snowflake dialect
"""

import sqlparse
from translator.translate_token import TranslateToken
from translator.redshift_to_snowflake import redshift_to_snowflake


class SqlTranslator:

    def __init__(self, sql: str):
        self._sql = self.translate(sql)

    def translate(self, sql: str) -> str:
        statements = sqlparse.parse(sql)
        translate_tokens = [TranslateToken(parsed) for parsed in statements]
        return ''.join([translate_token.translate(redshift_to_snowflake) for translate_token in translate_tokens])

    def sql(self):
        return self._sql

        
