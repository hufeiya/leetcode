# encoding utf-8
#!/usr/bin/python

import MySQLdb,os
db = MySQLdb.connect(host="localhost",user="root",passwd="4242",\
        db="STOCKS",charset="utf8",use_unicode=True)
cursor = db.cursor()
files = os.listdir("/home/hufeiya/practise/stock/shanghaiHistory")
CodeList = [fileName for fileName in files]
for code in CodeList:
    try:
        cursor.execute("""select * from shanghaiHistory where Code=%s""",code[:6])
        result = cursor.fetchall()
        targetLines = []
        for i in xrange(len(result)):
            if i + 2 >= len(result):
                break
            if result[i+1][2] < round(result[i][5]*1.1,2) and \
                    result[i+1][5] == round(result[i][5]*1.1,2) and \
                    result[i+2][2] > result[i+1][5] * 1.05:
                singleLine = []
                singleLine.append(result[i+1][0])
                singleLine.append(result[i+1][1])
                singleLine.append(1)
                if result[i+2][5] < round(result[i+1][5]*1.1,2):
                    singleLine[2] = 0
                targetLines.append(tuple(singleLine))
        print targetLines
    except:
        print "error!"

db.close()