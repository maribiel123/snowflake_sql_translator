import argparse
import logging
import logging.config

import yaml
from translator.sql_translator import SqlTranslator
import sqlparse
from sqlparse.sql import Comparison, Function, Identifier, IdentifierList, Statement, Token, Case
from sqlparse.tokens import Keyword, DML

def main():
    
    sql = """SELECT MAX(A), getdate, 
              CASE 
				WHEN original_due_date >= 1 THEN 1 ELSE 2 END,
              CASE 
                WHEN pr.pr_status in ('Approved','Closed','Approved - In CAPA','Approved - In Effectiveness Check')  THEN 1 ELSE 2 END AS FFF
              FROM t_tab WHERE 1 = 1;"""

    sql_1 = """SELECT 
				pr.division AS division,
				mi.original_due_date AS original_due_date,
				pr.PR_ID AS PR_ID,
				CASE WHEN pr.pr_status in ('Approved','Closed','Approved - In CAPA','Approved - In Effectiveness Check') THEN 1 END AS EEE,
                pr.dd
				FROM MI_ACTION_ITEM mi
				INNER JOIN PR PR on MI.pr_id = pr.pr_id 
				WHERE action_type_mir_ci IN ('Preventive Action','Corrective Action')
				AND pr.pr_status NOT IN ('Cancelled') 
				AND DATE_TRUNC('month', mi.original_due_date) < DATE_TRUNC('month',current_timestamp())"""
  
    parsed = sqlparse.parse(sql)[0]
    # print(f"Statement type: {parsed.get_type()}")
    # print(type(parsed))
    print('*********************************************************')
    for item in parsed:
        if isinstance(item, IdentifierList):
            for identifier in item.get_identifiers():
                print("identifier from List: ", identifier)
                if isinstance(identifier, Function):
                    print("Function from IdentifierList:", identifier.get_name())
                    # pass
                if isinstance(identifier, Case):
                    # print("Identifier_type: ", type(identifier))
                    print("Case Identifier: ", identifier)
                    print(identifier.get_cases())
                # print("identifier from IdentifierList:", identifier.get_name())
                # yield identifier.get_name()
        elif isinstance(item, Identifier):
            print("Identifier", item)
            # print(item, item.get_name())
        #     yield item.get_name()
        elif item.ttype is Keyword:
            print("Keyword:", item)
        #     # yield item.value

    # print(statements.get_identifiers())
    # _, par = parsed.token_next_by(i=sqlparse.sql.Case)
    # print(par)
    # print(parsed.token_prev(idx=1))

    # [print(f"{item}, {isinstance(item, Token)}") for item in parsed]

    # find 'CASE WHEN ' + ' any_string_form_list ' + 'IS '
    # replace 'CASE WHEN ' + ' any_string_form_list ' + '='
    # 

    # # Start migrating
    # 1) Open file 
    # 2) Iterate over SQL statement
    # 3) Translate each SQL statement
    # 4) Write translated to file


if __name__ == '__main__':
    main()