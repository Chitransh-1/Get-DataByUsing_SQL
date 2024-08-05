
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import datetime
#from datetime import datetime
import calendar
import sys
import os
import MysqlDBHelper as dbss
from datetime import timedelta as td
import pyodbc
import tablevariable as tbb
def get_val_database(sqlV,fldnuv,filev):
    print('dddc ',tbb.passWWC,sqlV)
    if filev=='setCC':
           openCC()
    
    try:

        cursor.execute(sqlV)
        getDataAccessAr = ""
        for row in cursor.fetchall():
            print(row)
            getDataAccessAr=row[fldnuv]
        
        return getDataAccessAr
    except pyodbc.Error as e:
        print("Error Not Con", e)
        return "b"
def openCC():
    global conn
   
    conn = pyodbc.connect(
                "Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
                "Dbq=" + tbb.settttC + ";"
                "PWD=" + tbb.passWWC + ";"
                )
    global cursor
    
    cursor = conn.cursor()

def getFirmDir(firmNameV):
    openCC()
    sqlV = f"Select * From Defalts Where c = 'Dir {firmNameV}'"
    try:

        cursor.execute(sqlV)
        
        for row in cursor.fetchall():
            if row[0]=='Add Dir':
               tbb.addData = row[3]
            elif row[0]=='Apru Dir':
               tbb.apruData= row[3]
            elif row[0]=='Stock Dir':
               tbb.stockData= row[3]
            elif row[0]=='adrs Dir':
               tbb.adrsDataData= row[3]
            
    except pyodbc.Error as e:
        print("Error Not Con", e)
        return "b"

    
def update_database(fldv,upansv,tblV,filev,quuuv,anssv,quuuv2,anssv2):
    print(quuuv2,' quuuv2')
    if filev=='setCC':
        conn = pyodbc.connect(
                "Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
                "Dbq=" + tbb.settttC + ";"
                "PWD=" + tbb.passWWC + ";"
                )
        
        cursor = conn.cursor()
        sqlV = f'''UPDATE [{tblV}] SET [{fldv}] = ? WHERE [{quuuv}] = ?'''
        dataa = (upansv,anssv)   
        if quuuv2:
            sqlV = f'''UPDATE [{tblV}] SET [{fldv}] = ? WHERE [{quuuv}] = ? and [{quuuv2}] = ?'''
            dataa = (upansv,anssv,anssv2)   
            
     
             
        print(dataa,sqlV)
        cursor.execute(sqlV,dataa)
        conn.commit()

def list_database(sqlV,fldnuv,filev):
    print('ddd ',tbb.passWWC)
    if filev=='setCC':
        openCC()
    try:

        cursor.execute(sqlV)
        getDataAccessAr = []
        for row in cursor.fetchall():
            getDataAccessAr.append(row[fldnuv])
            print(row)
            
        return getDataAccessAr
    except pyodbc.Error as e:
        print("Error Not Con", e)
        return "b"

def removeDecimalFlote(numm):
    numm = round(numm, 3)
    ssss = ""

    vvvv = str(numm)
    print(len(vvvv), numm)
    if vvvv[len(vvvv)-3:len(vvvv)] == "000":
        ssss = vvvv[0:len(vvvv)-4]
    elif vvvv[len(vvvv) - 2:len(vvvv)] == "00":
        ssss = vvvv[0:len(vvvv) - 2]

    elif vvvv[len(vvvv) - 1:len(vvvv)] == "0":
        ssss = vvvv[0:len(vvvv) - 1]

    return ssss


def valval(strrrr):
    lenn = len(strrrr)
    c = 0
    d = 0
    for i in range(lenn):
        b = i+1
        if toFloat(strrrr[0:b]) != 0:
            c = b
    if c > 0:
        print(strrrr[0:c], "LL")
        d = float(strrrr[0:c])
    return d


def rem_0(strnu):
    s = strnu
    if '.0' in strnu:
        newNumWithout0 = strnu[0:len(s) - 2]
    else:
        newNumWithout0 = strnu
    return newNumWithout0

def isNumberRR(num):
    try:
        float(num)
    except ValueError:
        return False
    else:
        return True
def toFloat(num):
    if num == None:
        return 0
    numm = 0
    try:
        numm = float(num)
    except ValueError:
        return numm
    else:
        return numm
    # if num.isnumeric() == True:
    #     print("YYYYYYY",num)
    # else:
    #     print("NNNNN",num)


def nmWi(widgetV):
    widgetVV = widgetV.split("!")
    lennnn = len(widgetVV)-1
    widwid = widgetVV[lennnn]
    wiwi = widwid.split(".")
    return(wiwi[1])


def dateConvert(datee, formatee):
    print('DDDDDDDD ',datee,formatee)
    dtttt = datee.split("-")
    dddd = dtttt[2]
    if len(dddd) > 2:
        dddd = dddd[:2]
    newDD = ""
    if formatee == "dtformate":
        yyyymmddV = dateConvert(datee, "yyyy-mm-dd")

        Begindate = datetime.datetime.strptime(yyyymmddV, "%Y-%m-%d")
        newDD = Begindate
    if formatee == "dd-mm-yy":
        yy = dtttt[0]
        if len(yy) == 4:
            yyI = int(yy)-2000
            yy = str(yyI)
        newDD = dddd + "-" + dtttt[1] + "-" + yy

    if formatee == "yyyy-mm-dd":
        yyyy = int(dtttt[2])+2000
        newDD = str(yyyy) + "-" + dtttt[1] + "-" + dtttt[0]
    if formatee == "6":
        newDD = dtttt[2] + dtttt[1] + dtttt[0]
    if formatee == "monthN":
        newDD = int(dtttt[1])
    if formatee == "month":
        nn = int(dtttt[1])-1
        mL = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
        newDD = mL[nn]
    if formatee == "monthS":
        nn = int(dtttt[1])-1
        mS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
              'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        newDD = mS[nn]

    if formatee == "day":
        print('DDDDDDDD2 ',datee,formatee)
        yyyy = int(dtttt[2]) + 2000

        intDay = datetime.date(year=yyyy, month=int(
            dtttt[1]), day=int(dtttt[0])).weekday()
        days = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]

        newDD = days[intDay]
        print('DDDDDDDD ',datee,newDD)
    if formatee == 'sYr':
        if int(dtttt[1]) > 3:
            yyII = dtttt[2]
        else:
            yyIII = int(dtttt[2])-1
            yyII = str(yyIII)
        newDD = "1-4-" + yyII
    if formatee == 'eYr':
        if int(dtttt[1]) < 4:
            yyII = dtttt[2]
        else:
            yyIII = int(dtttt[2])+1
            yyII = str(yyIII)
        newDD = "31-3-" + yyII
    if formatee == 'eDt':
        dtdt = datetime.date(int(dtttt[2]) + 2000, int(dtttt[1])+1,
                             1) - datetime.timedelta(days=1)
        newDD = dateConvert(str(dtdt), "dd-mm-yy")
    if formatee == 'sDt':
        newDD = "1-" + dtttt[1] + "-" + dtttt[2]
    return newDD


def dateCheckk(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d-%m-%y')
        return True
    except ValueError:
       # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return False


def date_addDay(datee, dayy):
    newDate = datee
    yyyymmddV = dateConvert(datee, "yyyy-mm-dd")

    Begindate = datetime.datetime.strptime(yyyymmddV, "%Y-%m-%d")
    newDate = Begindate + td(days=dayy)
    newDate = dateConvert(str(newDate), "dd-mm-yy")
    return newDate


def firstDayMonth(datee):
    sdt =datee.split("-")
    mm=sdt[1]
    yy=sdt[2]

    datee = "01" + "-" + mm + "-" + yy
    return datee
def lastDayMonth(datee):
    sdt =datee.split("-")
    mm=int(sdt[1])
    if len(yy)==4:
        yy=int(sdt[2])
    if len(yy)==2:
        yy=int(sdt[2])+2000
        
    
    dd=calendar.monthrange(yy, mm)[1]
    datee = str(dd) + "-" + mm + "-" + yy
    return datee

def fullDate(datee):
    dateeN = datee
    sdt =datee.split("-")
    if len(sdt)>0:
        if len(sdt[0])==1:
            dd= '0' +sdt[0]
        else:
            dd=sdt[0]
        datee = dd
    if len(sdt)>1:
        if len(sdt[1])==1:
            mm= '0' +sdt[1]
        else:
            mm=sdt[1]
        datee = dd + "-" + mm
    if len(sdt)>2:
        yy=sdt[2]
        datee = dd + "-" + mm + "-" + yy
    
        
    if len(datee.split("-")) == 2:
        dateeN = datee + "-" + todayDate("yy")
    if len(datee.split("-")) == 1:
        dateeN = datee + "-" + todayDate("mm") + "-" + todayDate("yy")
    return dateeN


def todayDate(formatee):
    todayy = datetime.date.today()
    todayyT = datetime.datetime.today()
    dd = str(todayy.day)

    mm = str(todayy.month)
    if len(mm)==1:
        mm="0" + mm
    if len(dd)==1:
        dd="0" + dd
    yyyy = todayy.year
    yy = str(yyyy-2000)
    yyyy = str(todayy.year)
    hh = str(todayyT.hour)

    MMMM = str(todayyT.minute)
    ss = str(todayyT.second)
    newDD = ""
    newdAry = []
    if formatee == "yyyy-mm-dd":
        newDD = yyyy + "-" + mm + "-" + dd

    if formatee == "fullDt":
        newDD = todayyT
    if formatee == "dd,mm,yy,hh,MM":
        newdAry = [dd, mm, yy, hh, MMMM]
    if formatee == "dd-mm-yy":
        newDD = dd + "-" + mm + "-" + yy
    if formatee == "10":
        newDD = yy + mm + dd + hh + MMMM
    if formatee == "6":
        newDD = yy + mm + dd
    if formatee == "time":
        newDD = hh + ":" + MMMM
    if formatee == "yy":
        newDD = yy
    if formatee == "mm":
        newDD = mm

    if formatee == "month":

        mL = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
        newDD = mL[int(mm)]
    if formatee == "monthS":
        mS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
              'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        newDD = mS[int(mm)]
    if formatee == "day":
        eeD = todayy.weekday()
        days = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
        newDD = days[eeD]
    if formatee == "dd,mm,yy,hh,MM":
        return newdAry
    return newDD
