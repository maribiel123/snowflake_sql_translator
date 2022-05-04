"""
Conversion rules for migrating Redshift SQL dialect to Snowflake
"""
from typing import List
from translator.translate_token import TranslateToken


def redshift_to_snowflake(token: TranslateToken) -> None:
    try:
        if token.is_function():
            if token.matches('date'):
                token.set('TO_DATE')
            elif token.matches('getdate'):
                token.set('current_timestamp')
            elif token.matches('date_diff'):
                token.set('datediff')
            elif token.matches('datepart'):
                token.set('date_part')
            elif token.startswith('convert_timezone'):
                token.remove_sequential_children("'utc'", ',')
        elif token.is_literal():
            if token.matches("'utc'"):
                token.set("'UTC'")
        elif token.matches('#'):
            token.set('num')
        elif token.is_case():
            print('It is Case', token)
            if token.matches('IS'):
                token.set("=")
                print("Mathes is")
        # elif token.is_identifierList():
        #     print('is_identifierList {}'.format(token))
        elif token.is_identifier():
            # print('It is identifier', token)
            if len(token.children) < 5 and token.contains('__'):
                token.replace('__', ':')

    except ValueError as e:
        print(token.get_statement())
        raise e