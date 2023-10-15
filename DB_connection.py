# import time
# t1 = time.time()
import configparser
import copy

# from openpyxl import Workbook,load_workbook
# from openpyxl.utils import get_column_letter
# import cx_Oracle
# from pandas import read_sql_query
# import base64
# import multiprocessing
# import datetime
# cx_Oracle.init_oracle_client(lib_dir="/Users/samuruge/Downloads/instantclient_19_8/")
# configpath = f"/Users/samuruge/Documents/Python/config.ini"
# configvalues = configparser.ConfigParser()
# # print("Reading the configurations from file : " + configpath)
# configvalues.read(configpath)
# # print(configvalues.sections())
# # print(configvalues.get('QA','qa_tns_qinv'))
# constr1 = configvalues.get('QA','qa_inv_db_username') + '/' + base64.b64decode(configvalues.get('QA','qa_inv_db_pwd_encrypted')).decode("utf-8") + '@' + configvalues.get('QA','qa_tns_qinv')
# constr2 = configvalues.get('STAGE','stg_inv_db_username') + '/' + base64.b64decode(configvalues.get('STAGE','stg_inv_db_pwd_encrypted')).decode("utf-8") + '@' + configvalues.get('STAGE','stg_tns_stage')
#
# connection1 = cx_Oracle.connect(constr1)
# # connection2 = cx_Oracle.connect(constr2)
# qa_inv_cursor = connection1.cursor()
# # stage_inv_cursor = connection2.cursor()
# # print(time.time()-t1)
# print('connection is done')
# data = qa_inv_cursor.execute(f"select * from sbl_ak_accounts where account_id in('AANA-1JHMMZ','AANA-1KLU3O')").fetchall()
#
# print(data[0])

for num in range(1,51):
    if num % 3 == 0 and num % 5 ==0:
        print(num,' fizzbuzz')
    elif num % 3 == 0 and num % 5 != 0:
        print(num, ' Fizz')
    elif num % 3 != 0 and num % 5 == 0:
        print(num, ' Buzz')
    else:
        print(num)
print('Completed')
