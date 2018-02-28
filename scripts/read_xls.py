#!user/bin/python
# -*- coding: utf-8 -*-
#Here import Libs Here
## Here import libs
import pandas as pd
#other lib and toke to use
from tokensSQL import *
from tokensNotification import *
from notifications import *
import pypyodbc as pyodbc
import pymssql


def list_bnk(bkAccount,dateCompare):
    listBnk = []
    k = 0
    sql = 'SELECT [Id_Oper] FROM [SAP].[dbo].[' + str(bkAccount) + '] Where Fecha >= \'' + str(dateCompare) + '\''
    conn = pymssql.connect(host=hostMSSQL,user=userMSSQL,password=passMSSQL,database=dbMSSQL)
    cur = conn.cursor()
    cur.execute(sql)
    for value in cur:
        Id_Opers = value[0]
        listBnk.insert(k,str(Id_Opers))
    conn.commit()
    conn.close()
    return listBnk

def list_xls(xls_url,sheetname):
    dataframeBnk = pd.read_excel(str(xls_url),sheet_name=str(sheetname),na_values='n/a')
    newdataframeBnk = dataframeBnk[dataframeBnk['Fecha'] >= '2018-01-01']
    dataFrameIdOpersXLS = newdataframeBnk['Id_Oper']
    listXLS = dataFrameIdOpersXLS.tolist()
    return listXLS


def readXls(fileX,bkn,dates,sheetname):
    listXLS = list_xls(fileX,sheetname)
    listSQL = list_bnk(bkn,dates)
    i = 0
    message = '################################################################\n'
    message += '\t Registros faltantes de  la cuenta : ' + str(bkn) + '\n'
    message += '################################################################\n'
    #print('Id_opers do not found in SQL SERVER')
    for value in listXLS:
        val = 'Bad'
        for value1 in listSQL:
            if value == value1:
                val = 'Good'
        if val == 'Bad':
            i = 1 + i
            message += str(i) + '.- ' + ' Id_Oper :'+ value + '\n'
            #print (str(i) + '.- ' + ' Id_Oper :'+ value)
    message += "################################################################\n"
    title = 'Cuenta analizada : ' + str(bkn)
    send_notification(title,emailnotification1,message)
    send_notification(title,emailnotification2,message)
################################################################################
##                                                                            ##
##                                  Test Here code                            ##
##                                                                            ##
################################################################################
