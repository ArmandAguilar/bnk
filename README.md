# Bnk - Validator

> This script read registers of sheet of excel and compare the register of excel  versus the register that be in MSSQL when the scripts detected that some registers don't be in MSSQL do a list and send this list by Email to user administrative.

### Tools used in this project

- Python 2.7.11
- pandas
- pypyodbc
- pymssql
- urllib2
- base64
- simplejson
- unicodedata
- sys

### Descriptions of scripts

**Main** : This file run the main function..

**notification** : This file send email for make notification.

**read_xls** : This file read files xls of main.py , and compare the register in MSSQL in the table speficicate,then send a email with register that you need upload to the system..

**Tokes (tokensNotification,tokensSQL)** : this files have access to Email and MSSQL.



![How is works](https://github.com/ArmandAguilar/bnk/blob/master/Diagrama/Diagrama.png)
