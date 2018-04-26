#!user/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
#other lib and toke to use
from tokensSQL import *
from tokensNotification import *
from notifications import *
from read_xls import *
import pypyodbc as pyodbc
import pymssql
import urllib2, base64
import simplejson as json
import unicodedata
import sys
reload(sys)


################################################################################
##                                                                            ##
##                              Main                                          ##
##                                                                            ##
################################################################################

#Here Json with all accoutn of bank an box
AccountsJson = '{"Person":['
AccountsJson += '{"Table":"AA2367045623Bnx","Sheet":"2367045623Banamex","URL":"H://Dropbox//Personal//Dropbox (Personal)//Tesoreria//3.-Bnk//2367045623Banamex-1-A.xlsm","Dates":"2018-01-01"},' + '\n'
AccountsJson += '{"Table":"AA2367057222Bnx","Sheet":"Hoja1","URL":"H://Dropbox//Personal//Dropbox (Personal)//Tesoreria//3.-Bnk//2367057222Banamex-1B.xls","Dates":"2018-01-01"},' + '\n'
AccountsJson += '{"Table":"AAActinver","Sheet":"Hoja1","URL":"H://Dropbox//Personal//Dropbox (Personal)//Tesoreria//3.-Bnk//Activer-1B.xlsm","Dates":"2018-01-01"},' + '\n'
AccountsJson += '{"Table":"AA22000015322Stder","Sheet":"Hoja1","URL":"H://Dropbox//Personal//Dropbox (Personal)//Tesoreria//3.-Bnk//22000015322Stder-1B.xlsm","Dates":"2018-01-01"}' + '\n'
AccountsJson += ']}'
data = json.loads(AccountsJson,strict=False)
print('====== >> Procensado')
for value in data['Person']:
    readXls(str(value['URL']),str(value['Table']),str(value['Dates']),str(value['Sheet']))
    print('Procesnado :' + str(value['Table']))
