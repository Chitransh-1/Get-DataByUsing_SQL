
import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
import tablevariable
from mysql.connector import Error
import DataRepo as repo
from dateutil.parser import parse
from tkinter import ttk, messagebox
errrrConect = 'Error connecting '



def insert_defaultM(dataa, database):
    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database=database)
    mycursor = myDbs.cursor(buffered=True)

    querry = "insert into dafault(ID,datee,nm,tf,defN,def1,def2,def3,def4,head,frmId,hostID)" \
             " values(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s)"

    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()

def insert_printSetting(dataa):

    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database='settingg')
    mycursor = myDbs.cursor(buffered=True)

    querry = "insert into printSetting(datee,name,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,frmId,hostID)" \
             " values(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"

    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()


def update_identry(dataa, idd):

    dataBseN = tablevariable.databaseName
    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database=dataBseN)
    mycursor = myDbs.cursor(buffered=True)
    querry = """update ide Set datee=%s, whyv=%s, grt=%s, srt=%s, aaaa=%s, met=%s, yr=%s, amt=%s,
       prty=%s, dttm=%s, comm=%s, head2=%s Where t_ent = """ + idd
    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()


def gstMaintain(dataa, codeeee):

    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database='addac')
    mycursor = myDbs.cursor(buffered=True)

    querry = """update gst Set saledatee=%s, saleent=%s, saleNum=%s, saleWT=%s Where cd = '""" + codeeee + "'"
    print('dataaaa ', dataa)
    print('querry ', querry)
    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()


def insert_identry(dataa):

    dataBseN = tablevariable.databaseName
    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database=dataBseN)
    mycursor = myDbs.cursor(buffered=True)

    querry = "insert into ide values(%s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"

    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()


def get_columnList(tableName, databaseN, forWht):

    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database=databaseN)
    mycursor = myDbs.cursor(buffered=True)
    # qurry = "Select *  from  " + tableName
    qurry = "Select *  from  " + tableName

    mycursor.execute(qurry)
    columns = mycursor.description
    result = []
    for value in range(len(mycursor.description)):
        # tmp = {}
        # for (index, column) in enumerate(value):
        #     tmp[columns[index][0]] = column
        if forWht == "list":
            result.append(mycursor.description[value][0])
        else:
            result.append(mycursor.description[value][0] + "=%s")

    return result
def update_fulldataa(id, data,fldsary, tableNm, dbName):
    strstr = ""
    for st in fldsary:
        if strstr =='':
            strstr = st + '=%s'
        else:
            strstr = strstr + "," + st + '=%s'
    print('strstrsss',strstr)        
    pass
 #querry = """update gst Set saledatee=%s, saleent=%s, saleNum=%s, saleWT=%s Where cd = '""" + codeeee + "'"
def update_dataa(ques, ans, ques2, ans2, colvN, upda, tableNm, dbName):
    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database=dbName)
    mycursor = myDbs.cursor(buffered=True)

    querry = "update " + tableNm + " Set " + colvN + "=" + \
        str(upda) + " Where " + ques + " = '" + ans + "' and frmId = '" + \
        str(tablevariable.firmId) + "' and hostID = '" + \
        str(tablevariable.hostID) + "'"
    if ques2:
        querry = "update " + tableNm + " Set " + colvN + "='" + \
            str(upda) + "' Where " + ques + " = '" + ans + "' and " + ques2 + " = '" + ans2 + "' and frmId = '" + \
            str(tablevariable.firmId) + "' and hostID = '" + \
            str(tablevariable.hostID) + "'"
    if ques in ['hostID', 'frmId']:
        querry = "update " + tableNm + " Set " + colvN + "=" + \
            str(upda) + " Where " + ques + " = '" + ans + "'"
    print('qqqqq', querry)
    mycursor.execute(querry)
    myDbs.commit()
    mycursor.close()


def update_account3(nm, wht, colvN, updaaata):

    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database='addd')
    mycursor = myDbs.cursor(buffered=True)

    querry = "update accountt Set " + colvN + "=" + \
        str(updaaata) + " Where nm = '" + nm + "' and wht ='" + wht + "'"
    if colvN == "ref":
        querry = "update accountt Set " + colvN + "='" + updaaata + \
            "' Where nm = '" + nm + "' and wht ='" + wht + "'"

    mycursor.execute(querry)
    myDbs.commit()
    mycursor.close()


def update_printSetting(dataa, idd):

    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database='settingg')
    mycursor = myDbs.cursor(buffered=True)

    querry = """update printSetting Set datee=%s,name=%s,L1=%s,L2=%s,L3=%s,L4=%s,L5=%s,
    L6=%s,L7=%s,L8=%s,L9=%s,L10=%s,L11=%s,L12=%s,L13=%s,L14=%s,L15=%s,L16=%s,frmId=%s,hostID=%s Where ID = """ + idd

    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()


def update_default(dataa, idd, dataName, wht):

    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database=dataName)
    mycursor = myDbs.cursor(buffered=True)

    if wht == 'lblprt':
        querry = """update dafault Set tf=%s,defN=%s,def1=%s,def2=%s,def3=%s,
                def4=%s Where ID = """ + idd
    else:
        querry = """update dafault Set tf=%s,defN=%s,def1=%s,def2=%s,def3=%s,
            def4=%s,head=%s Where ID = """ + idd

    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()


def insert_prty(dataa):

    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database='addac')
    mycursor = myDbs.cursor(buffered=True)
    print('dataa', len(dataa), dataa)
    querry = "insert into prty values(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"
    # querry = "insert into printSetting(datee,name,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,frmId,hostID)" \
    #          " values(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"

    mycursor.execute(querry, dataa)
    lID = mycursor.lastrowid
    myDbs.commit()
    mycursor.close()
    return lID


def update_prty(dataa, idd):
    print('ASW', dataa)
    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database='addac')
    mycursor = myDbs.cursor(buffered=True)
    querry = "update  prty Set datee=%s,nm=%s,adrs=%s,ref=%s,mob=%s,mob2=%s,tel=%s,tel2=%s,city=%s,Vil=%s,St=%s,id1=%s," \
             "id2=%s,gst=%s,grp=%s,num=%s,frmId=%s,hostID=%s Where ID = " + idd

    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()
    
def get_list_contain(ques, ans, ques2, ans2,fldNN,containV, orderby, fldN, tableName, databaseName):

    lstrr = 0
    var2 = []
    if not databaseName:
        databaseName = tablevariable.databaseName
    if databaseName == "null":

        databaseName = tablevariable.databaseName

    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=databaseName)
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select * from " + tableName + " Where " + ques + " = '" + ans + \
            "' and " + ques2 + " = '" + ans2 + "' and hostID = '" + tablevariable.hostID + "'"
        if ques2 == "null":
            qurry = "Select * from " + tableName + " Where " + ques + \
                " = '" + ans + "' and hostID = '" + tablevariable.hostID + "'"
        if orderby != "":
            qurry = qurry + " Order by " + orderby
        print("queryy", qurry)
        mycursor.execute(qurry)
        records = mycursor.fetchall()
        for row in records:
            if containV in row[fldNN]: 
                var2.append((row[fldN]))
        print("rowww", var2)

        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL J", e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()

            return var2


    
def insert_treehead(dataa):
    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database='settingg')
    mycursor = myDbs.cursor(buffered=True)
    querry = "insert into treehead(project,whtt,sno,head,aall_head,widthh,visibled,align,aaal,bbbl" \
             ",cccl,headv,printt_ind,frmID,hostID)" \
        " values(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s,%s)"

    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()

def insert_txtsetting(dataa):
    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database='settingg')
    print("length", len(dataa))
    mycursor = myDbs.cursor(buffered=True)
    querry = "insert into txtsetting(datee,txt_lab,sno,indexx,hi,widthh,lefttX,topY,previousInd,tabInd" \
             ",headIndex,headCaption,visi,enable,colourr,project,def1,def2,alig,def3,frmId,hostID)" \
        " values(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s,%s,%s, %s, %s)"

    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()
def update_txtsetting(dataa, idd, dataName, wht):

    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database=dataName)
    mycursor = myDbs.cursor(buffered=True)
   
    print('DDDDDD  :',dataa)
    querry = """update txtsetting Set sno=%s,indexx=%s,hi=%s,widthh=%s,lefttX=%s,topY=%s
                ,previousInd=%s,tabInd=%s,headIndex=%s,headCaption=%s,visi=%s,enable=%s,colourr=%s,project=%s,def1=%s,def2=%s Where ID = """ + idd

    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()

def insert_accountt(dataa, database):
    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database=database)
    mycursor = myDbs.cursor(buffered=True)

    querry = "insert into accountt(datee,nm,typ,rs,gfn,sfn,ref,wht,info,num" \
             ",hindi,comm,headd,headddd,sno,frmId,hostID)" \
             " values(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s,%s)"

    mycursor.execute(querry, dataa)
    lID = mycursor.lastrowid
    myDbs.commit()
    mycursor.close()
    return lID

def fetch_databases():
    try:
        conn = mysql.connector.connect(
            host="localhost", 
            user="root",  
            password=""
        )
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        conn.close()
        return [db[0] for db in databases]
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", str(e))
        return []

def fetch_tables(database_name):
    try:
        conn = mysql.connector.connect(
            host="localhost", 
            user="root",  
            password="",  
            database=database_name
        )
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        conn.close()
        return [table[0] for table in tables]
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", str(e))
        return []

def fetch_columns(database_name, table_name):
    try:
        conn = mysql.connector.connect(
            host="localhost", 
            user="root",  
            password="",  
            database=database_name
        )
        cursor = conn.cursor()
        cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        columns = cursor.fetchall()
        conn.close()
        return [column[0] for column in columns]
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", str(e))
        return []


def deleteData33(ques, ans, ques2, ans2, ques3, ans3, tableName, dbaseName):
    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=dbaseName)
        mycursor = myDbs.cursor(buffered=True)
        qurry = "DELETE  from " + tableName + " Where " + ques + \
            " = '" + ans + "' and " + ques2 + " = '" + ans2 + "' and " + ques3 + " = '" + ans3 + "'"
        if ques2 == "null":
            qurry = "DELETE  from " + tableName + " Where " + ques + " = '" + ans + "'"
        if ques == "All" and ques2 == "All":
            qurry = "DELETE  from " + tableName
        mycursor.execute(qurry)
        myDbs.commit()
        mycursor.close()

    except Error as e:
        print(errrrConect + "MySQL A", e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()





def deleteData(ques, ans, ques2, ans2, tableName, dbaseName):
    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=dbaseName)
        mycursor = myDbs.cursor(buffered=True)
        qurry = "DELETE  from " + tableName + " Where " + ques + \
            " = '" + ans + "' and " + ques2 + " = '" + ans2 + "'"
        if ques2 == "null":
            qurry = "DELETE  from " + tableName + " Where " + ques + " = '" + ans + "'"
        if ques == "All" and ques2 == "All":
            qurry = "DELETE  from " + tableName
        print('qqqqq',qurry)
        mycursor.execute(qurry)
        myDbs.commit()
        mycursor.close()

    except Error as e:
        print(errrrConect + "MySQL A", e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()


def getTempppp(wht):
    checkInAccc = []
    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database="settingg")
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select *  from  tempppp Where wht = '" + wht + "'"
        mycursor.execute(qurry)
        records = mycursor.fetchall()
        if len(records) == 1:
            for row in records:

                for i in range(15):
                    checkInAccc.append(row[i])
        mycursor.execute(qurry)
        mycursor.close()
    except Error as e:

        print(errrrConect + "tempppp B", e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()
        return checkInAccc


def checkMob(mob):
    checkInAccc = []
    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database="addac")
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select *  from  prty Where mob = '" + mob + "'"

        mycursor.execute(qurry)
        records = mycursor.fetchall()
        if len(records) == 1:
            for row in records:
                checkInAccc = [row[2], row[3], row[14], row[0]]
                # for i in range(20):
                #     checkInAccc.append(row[i])
        mycursor.execute(qurry)
        mycursor.close()
    except Error as e:

        print(errrrConect + "prty C", e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()
        return checkInAccc


def getXYHW_txtSet(project, def1, def2):
    checkInAccc = []
    # qurry = "Select *  from  txtsetting Where project = '" + project + "' and  def1 = '" + def1 + \
    #         "' and  indexx = " + str(indexx) + " and hostID = '" + tablevariable.hostID + "'"

    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database="settingg")
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select *  from  txtsetting Where project = '" + project + "' and  def1 = '" + def1 + \
                "' and  def2 = '" + def2 + "' and hostID = '" + tablevariable.hostID + "'"

        print("qqww", qurry)
        mycursor.execute(qurry)
        records = mycursor.fetchall()
        if len(records) == 1:
            for row in records:

                yy = row[8]
                if row[12] == "GWt" or row[12] == "StWt" or row[12] == "StNm" or row[12] == "StRs":
                    yy = -80
                checkInAccc = [row[5], row[6], row[7], yy, row[12]]
                # aaa=row[5]
                # for i in range(20):
                #     checkInAccc.append(row[i])
        mycursor.execute(qurry)
        mycursor.close()
    except Error as e:

        print(errrrConect + "txtsetting D" +
              " : " + tablevariable.printError, e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()
        return checkInAccc


def getXYHW_ByHead(project, def1, head):
    getXYHW_ByHeadV = []
    # qurry = "Select *  from  txtsetting Where project = '" + project + "' and  def1 = '" + def1 + \
    #         "' and  indexx = " + str(indexx) + " and hostID = '" + tablevariable.hostID + "'"

    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database="settingg")
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select *  from  txtsetting Where project = '" + project + "' and  def1 = '" + def1 + \
                "' and  headCaption = '" + head + "' and hostID = '" + tablevariable.hostID + "'"

        mycursor.execute(qurry)
        records = mycursor.fetchall()
        if len(records) == 1:
            for row in records:

                yy = row[8]
                if row[9] == 20:
                    yy = -80
                getXYHW_ByHeadV = [row[5], row[6], row[7], row[8], row[19]]
                # aaa=row[5]
                # for i in range(20):
                #     checkInAccc.append(row[i])
        mycursor.execute(qurry)
        mycursor.close()
    except Error as e:

        print(errrrConect + "txtsetting D" +
              " : " + tablevariable.printError, e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()
        return getXYHW_ByHeadV


def checkInAcc(name):
    checkInAccc = 0
    if name != "":
        try:
            myDbs = mysql.connector.connect(
                host='localhost', user='root', password='', database=tablevariable.databaseName)
            mycursor = myDbs.cursor(buffered=True)
            qurry = "Select *  from  accountt Where nm = '" + name + "'"
            mycursor.execute(qurry)
            records = mycursor.fetchall()
            if len(records) == 1:
                for row in records:

                    checkInAccc = row[0]
            mycursor.execute(qurry)
            mycursor.close()
        except Error as e:

            print(errrrConect + "accountt F", e)
        finally:
            # closing database connection.
            if (myDbs.is_connected()):
                myDbs.close()
    return checkInAccc


def insert_tempppp(dataa):
    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database='settingg')
    mycursor = myDbs.cursor(buffered=True)
    print('dataadataa',dataa)
    querry = """insert into tempppp(ID,wht,datee,datee2,txt1,txt2,txt3,txt4,int1a,int2a,int3a,int4a,num1,num2,num3,num4)
            values(%s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"""
    print (querry)
    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()

def insert_summeryT(dataa):
    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database='addac')
    mycursor = myDbs.cursor(buffered=True)
    print('lelelelel ',len(dataa))
    querry = "insert into summeryt values(%s,%s, %s, %s, %s,%s,%s, %s, %s, %s,%s,%s)"

    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()



def insert_itemCode(dataa, database):

    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database=database)
    mycursor = myDbs.cursor(buffered=True)

    querry = "insert into itemcode(datee,nm,typ,pcs,lessWt,wtv,fn,mk,rate,rs,fixCode,pri,met,pc_it,headd,headddd,hindi,frmId,hostID)" \
             " values(%s, %s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()


def update_Stock(dataa, database, idd):

    dataBseN = tablevariable.databaseName
    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database=database)
    mycursor = myDbs.cursor(buffered=True)

    querry = """update itemcode Set datee=%s, pcs=%s, lessWt=%s, wtv=%s, fn=%s, mk=%s, rate=%s, rs=%s Where ID = """ + idd
    print("quryyy", querry)
    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()


def insert_AAll_allFld(dataa, database):
    if database == "":
        database = tablevariable.databaseName
    qustMarkk = """VALUES ("""
    for a in range(47):  # total fiels se 1 kam
        qustMarkk = qustMarkk + "%s,"
    qustMarkk = qustMarkk + "%s)"

    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database=database)
    mycursor = myDbs.cursor(buffered=True)

    querry = "insert into AAll(datee,item,prtname,met,wt,rtrs,rtfn,rscr," \
             "rsdb,fncr,fndb,why,code,tch,ves,mak,makunit,make,detail,mcd,AccTyp" \
             ",ent, pri,suf,crdr,num, comm,entryno, totalent,pcs, wttt,stwt,st_name," \
             "strs,gwt,item_fn,sgst,cgst,igst,t_entno, wastage,metal_rs,hm_ch," \
             " type2,proMet,huid,frmId,hostID) " + qustMarkk

    # querry = "insert into itemcode(datee,nm,typ,pcs,wtv,fn,mk,mkUnit,rs,fixCode,pri,met,headd,headddd,hindi,frmId,hostID)" \
    #          " values(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()


def insert_gst_seleced(dataa, project, listtt):
    print('COCOCOCG', len(dataa), dataa)
    print('COCOCOCG2', listtt)

    qustMarkk = """VALUES ("""
    for a in range(len(dataa)-1):  # total fiels se 1 kam
        qustMarkk = qustMarkk + "%s,"
    qustMarkk = qustMarkk + "%s)"

    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database='addac')
    mycursor = myDbs.cursor(buffered=True)

    querry = "insert into gst(" + listtt + ") " + qustMarkk

    # querry = "insert into itemcode(datee,nm,typ,pcs,wtv,fn,mk,mkUnit,rs,fixCode,pri,met,headd,headddd,hindi,frmId,hostID)" \
    #          " values(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()


def insert_account_seleced(dataa, databaseN, listtt):
    print('COCOCOCG', len(dataa), dataa)
    print('COCOCOCG2', listtt)

    qustMarkk = """VALUES ("""
    for a in range(len(dataa)-1):  # total fiels se 1 kam
        qustMarkk = qustMarkk + "%s,"
    qustMarkk = qustMarkk + "%s)"

    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database=databaseN)
    mycursor = myDbs.cursor(buffered=True)

    querry = "insert into accountt(" + listtt + ") " + qustMarkk

    # querry = "insert into itemcode(datee,nm,typ,pcs,wtv,fn,mk,mkUnit,rs,fixCode,pri,met,headd,headddd,hindi,frmId,hostID)" \
    #          " values(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()


def insert_seleced(dataa, databaseN, listtt, tblName):
    print('COCOCOCG', len(dataa), dataa)
    print('COCOCOCG2', listtt)
    print('COCOCOCG2', tblName,databaseN)

    qustMarkk = """VALUES ("""
    for a in range(len(dataa)-1):  # total fiels se 1 kam
        qustMarkk = qustMarkk + "%s,"
    qustMarkk = qustMarkk + "%s)"

    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database=databaseN)
    mycursor = myDbs.cursor(buffered=True)

    querry = "insert into " + tblName + "(" + listtt + ") " + qustMarkk

    # querry = "insert into itemcode(datee,nm,typ,pcs,wtv,fn,mk,mkUnit,rs,fixCode,pri,met,headd,headddd,hindi,frmId,hostID)" \
    #          " values(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    mycursor.execute(querry, dataa)
    myDbs.commit()
    mycursor.close()


def insert_seleced2(dataa, database, project, listtt, tableName):
    print('COCOCOC', len(dataa), dataa)
    print('COCOCOC2', listtt)

    if database == "":
        database = tablevariable.databaseName
    qustMarkk = """VALUES ("""
    for a in range(len(dataa)-1):  # total fiels se 1 kam
        qustMarkk = qustMarkk + "%s,"
    qustMarkk = qustMarkk + "%s)"

    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database=database)
    mycursor = myDbs.cursor(buffered=True)
    if project == "Sale":

        # querry = "insert into aall(pcs, pri, item, suf, wt, rtrs, mak, makunit, make, mcd,"\
        #     "rscr, rsdb, gwt, stwt, strs, st_name, crdr, AccTyp, sgst, cgst,"\
        #          "igst, hm_ch,code, met,  type2,huid,metal_rs, datee, prtname, why,"\
        #          "detail, entryno,totalent, t_entno, frmId, hostID) " + qustMarkk
        querry = "insert into " + tableName + "(" + listtt + ") " + qustMarkk

    # querry = "insert into itemcode(datee,nm,typ,pcs,wtv,fn,mk,mkUnit,rs,fixCode,pri,met,headd,headddd,hindi,frmId,hostID)" \
    #          " values(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    mycursor.execute(querry, dataa)
    lstId = mycursor.lastrowid
    myDbs.commit()
    mycursor.close()
    return lstId


def closeAllFirm(hstID):
    
    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database='settingm')
    mycursor = myDbs.cursor(buffered=True)

    qurry = "UPDATE " + tablevariable.dafaultV + \
        " SET defN = 2 Where hostID = " + str(hstID) + " and def1 = 'FirmName'"
    print("jeje",qurry)
    mycursor.execute(qurry)
    myDbs.commit()
    mycursor.close()


def openFirm(idd):

    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database='settingm')
    mycursor = myDbs.cursor(buffered=True)

    qurry = "UPDATE " + tablevariable.dafaultV + " SET defN = 1 Where hostID = " + \
        tablevariable.hostID + " and def1 = 'FirmName' and frmId = " + str(idd)

    mycursor.execute(qurry)
    myDbs.commit()
    mycursor.close()


def openFirmData(wht):
    if wht == 'ID':
        fld = 0
    if wht == 'sdate':
        fld = 6
    if wht == 'edate':
        fld = 7
    return get_settingM('def1', 'FirmName', 'defN', str(fld), '', 0)


def get_hostID():
    lstrr = 0
    try:

        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database='settingm')
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select * from dafault Where def1 = 'hostID'"

        mycursor.execute(qurry)
        records = mycursor.fetchall()
        for row in records:

            lstrr = row[11]

        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL G", e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()
            return lstrr
            print("MySQL connection is closed Now E")


def defaultG(deffff):
    lstrr = []
    qurry = "Select * from dafault Where nm = '" + deffff + "' and frmId = " + \
        str(tablevariable.firmId) + "' and hostID = '" + \
        str(tablevariable.hostID) + "'"
    
    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database='settingg')
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select * from dafault Where nm = '" + deffff + "' and frmId = " + \
            str(tablevariable.firmId) + " and hostID = '" + \
            str(tablevariable.hostID) + "'"

        mycursor.execute(qurry)
        records = mycursor.fetchall()
        print('qqqq',qurry)
        #print("recordd", records)
        for row in records:

            for colV in range(15):

                if colV > 2 and colV < 10:
                    lstrr.append(row[colV])
            print('aaaaaaaas :', lstrr)
        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL L", e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()
            return lstrr


def printingSetting(deffff, uptoV):
    lstrr = []
    qurry = "Select * from printsetting Where name = '" + deffff + "' and frmId = " + \
        str(tablevariable.firmId) + "' and hostID = '" + \
        str(tablevariable.hostID) + "'"
    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database='settingg')
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select * from printsetting Where name = '" + deffff + "' and frmId = '" + \
            str(tablevariable.firmId) + "' and hostID = '" + \
            str(tablevariable.hostID) + "'"

        mycursor.execute(qurry)
        records = mycursor.fetchall()
        for row in records:
            for colV in range(uptoV):

                if colV > 1 and colV < uptoV+1:
                    lstrr.append(row[colV])

        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL L", e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()
            return lstrr


# def printingSet(deffff, uptoV):
#     lstrr = []
#     qurry = "Select * from printsetting Where name = '" + deffff + "' and frmId = " + \
#         str(tablevariable.firmId) + "' and hostID = '" + \
#         str(tablevariable.hostID) + "'"
#     try:
#         myDbs = mysql.connector.connect(
#             host='localhost', user='root', password='', database='settingg')
#         mycursor = myDbs.cursor(buffered=True)
#         qurry = "Select * from printset Where nm = '" + deffff + "' and frmId = '" + \
#             str(tablevariable.firmId) + "' and hostID = '" + \
#             str(tablevariable.hostID) + "'"

#         mycursor.execute(qurry)
#         records = mycursor.fetchall()
#         for row in records:
#             for colV in range(uptoV):

#                 if colV > 1 and colV < uptoV+1:
#                     lstrr.append(row[colV])

#         mycursor.close()
#     except Error as e:
#         print(errrrConect + "MySQL L", e)
#     finally:
#         # closing database connection.
#         if (myDbs.is_connected()):
#             myDbs.close()
#             return lstrr


def getByAAllSale(totalentS, AccTypS, crdrS, databaseN):
    allData = []
    lstrr = []
    qurry = "SELECT  * from aall Where totalent  = " + str(totalentS) + " and AccTyp = '" + AccTypS + \
        "' and crdr = '" + crdrS + "' and frmId = '" + str(tablevariable.firmIdS) + \
            "' and hostID = '" + tablevariable.hostID + "'"

    if not databaseN:
        databaseN = tablevariable.databaseName
    print('qurry11', tablevariable.hostID, databaseN, AccTypS)
    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database='addd')
        mycursor = myDbs.cursor(buffered=True)
        if AccTypS == "All":
            qurry = "SELECT  * from AAll Where totalent  = '" + str(totalentS) + "' and frmId = '" + \
                tablevariable.firmIdS + "' and hostID = '" + tablevariable.hostID + "'"
        else:

            qurry = "SELECT  * from AAll Where totalent  = '" + str(totalentS) + "' and AccTyp = '" + AccTypS + \
                    "' and crdr = '" + crdrS + "' and frmId = " + tablevariable.firmIdS + \
                " and hostID = '" + tablevariable.hostID + "'"
            # qurry = "SELECT  * from aall where totalent  = " + totalentS + " and hostID = '" + \
            #     tablevariable.hostID + "'"
        print('qurry44')
        mycursor.execute(qurry)
        records = mycursor.fetchall()
        for row in records:
            if AccTypS == "All":
                allData.app(row)
            else:
                for colV in range(40):
                    lstrr.append(row[colV])

        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL L", e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()
            if AccTypS == "All":
                return allData
            else:
                return lstrr


def get_settingM(ques, ans, ques2, ans2, orderby, fld):
    lstrr = 0
    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database='settingm')
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select * from dafault Where " + ques + " = '" + ans + "' and " + \
            ques2 + " = '" + ans2 + "' and hostID = '" + tablevariable.hostID + "'"
        if ques2 == "null":
            qurry = "Select * from dafault Where " + ques + " = '" + \
                ans + "' and hostID = '" + tablevariable.hostID + "'"
        if orderby != "":
            qurry = qurry + " Order by " + orderby

        mycursor.execute(qurry)
        records = mycursor.fetchall()
        print("ddd", qurry)
        for row in records:

            lstrr = row[fld]

        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL H", e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()
            return lstrr


def get_entSet(txt_lab, def1, project, fld, orderby, tableName, databaseName):
    pass


def get_BtnSideSet(txt_lab, def1, def2Lik, fld, orderby, tableName, databaseName):
    lstrr = 0
    var2 = []
    if databaseName == "null":
        databaseName = tablevariable.databaseName

    try:
        anss = ""
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=databaseName)
        mycursor = myDbs.cursor(buffered=True)
        # qurry = "Select * from " + tableName + " Where txt_lab = '" + txt_lab + \
        #     "' and  def1 = '" + def1 + "' and  def2 Like '%" + \
        #         def2Lik + "%' and hostID = '" + tablevariable.hostID + "'"
        # qurry = "Select * from " + tableName + " Where txt_lab = '" + txt_lab + \
        #     "' and  def1 = '" + def1 + "' and  def2 Like %s and hostID = '" + \
        #         tablevariable.hostID + "'"
        # anss = ("%" + def2Lik + "%", "%All%")
        # anss = "('All','" + def2Lik + "')"
        # print("myTuple", anss)
        # qurry = "Select * from " + tableName + " Where txt_lab = '" + txt_lab + \
        #     "' and  def1 = '" + def1 + "' and  def2 in %s and hostID = '" + \
        #     tablevariable.hostID + "'"

        qurry = "SELECT * FROM " + tableName + \
            " Where txt_lab = '" + txt_lab + \
            "' and  def1 = '" + def1 + "' and  frmId = '" + tablevariable.firmIdS + "'  and hostID = '" + \
                tablevariable.hostID + \
            "' and project IN ('All','" + def2Lik + "') and visi = 1"
        # qurry = "SELECT * FROM " + tableName + \
        #     " WHERE def2 IN %s"

        if def2Lik == "null":
            qurry = "Select * from " + tableName + " Where txt_lab = '" + txt_lab + \
                "' and  def1 = '" + def1 + "' and hostID = '" + tablevariable.hostID + "'"
            anss = ""
        if orderby != "":
            qurry = qurry + " Order by " + orderby
        if anss == "":
            mycursor.execute(qurry)
        else:
            mycursor.execute(qurry, anss)

        records = mycursor.fetchall()
        for row in records:

            var2.append((row[fld]))

        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL J", e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()

            return var2


def get_list(ques, ans, ques2, ans2, orderby, fld, tableName, databaseName):

    lstrr = 0
    var2 = []
    print("ddddd", databaseName)
    if not databaseName:
        databaseName = tablevariable.databaseName
    if databaseName == "null":

        databaseName = tablevariable.databaseName

    try:
        print("dddd1", tablevariable.hostID)
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=databaseName)
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select * from " + tableName + " Where " + ques + " = '" + ans + \
            "' and " + ques2 + " = '" + ans2 + "' and hostID = '" + tablevariable.hostID + "'"
        if ques2 == "null":
            qurry = "Select * from " + tableName + " Where " + ques + \
                " = '" + ans + "' and hostID = '" + tablevariable.hostID + "'"
        if orderby != "":
            qurry = qurry + " Order by " + orderby
        print("dddd2")
        print("qurrryy",qurry)
        mycursor.execute(qurry)
        records = mycursor.fetchall()
       # print('Recccccc ',records)
        for row in records:
            var2.append((row[fld]))

        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL J", e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()

            return var2


def get_list33(ques, ans, ques2, ans2, ques3, ans3, orderby, fld, tableName, databaseName):

    lstrr = 0
    var2 = []
    if not databaseName:
        databaseName = tablevariable.databaseName
    if databaseName == "null":

        databaseName = tablevariable.databaseName

    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=databaseName)
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select * from " + tableName + " Where " + ques + " = '" + ans + \
            "' and " + ques2 + " = '" + ans2 + "' and " + ques3 + " = '" + \
                ans3 + "' and hostID = '" + tablevariable.hostID + "'"

        if orderby != "":
            qurry = qurry + " Order by " + orderby

        mycursor.execute(qurry)
        records = mycursor.fetchall()
        print("qurryyy", qurry)
        for row in records:

            var2.append((row[fld]))

        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL J", e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()

            return var2


def get_itemtyp(n1, Itemm):
    if Itemm not in ['*', '+', '-']:
        yy = ""
        n2_whtt = getTyp(n1)
        print('CRCRCRCRC5', n2_whtt + "/" + Itemm)
        if n2_whtt == "Prefix":
            yye = item_EntDetail(Itemm, "Group Item", '', '')
            yy = yye["typ"]
            return yy


def get_Ratelist(numm):
    lstrr = 0
    var2 = []

    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database="addac")
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select * from " + "rates" + " Where name = 'Rate' and  frmId  = '" + \
            str(tablevariable.firmId) + "' and hostID = '" + \
            str(tablevariable.hostID) + "' Order by snot"
        print('ququququq', qurry, numm)
        mycursor.execute(qurry)
        records = mycursor.fetchall()
        for row in records:
            if numm == 3:
                var2.append(([row[2], row[4], row[0]]))

            if numm == 6:
                if row[0] == 2:
                    rr=0
                    for jj in row:
                        print('YYYY',rr,jj)
                        rr +=1
                var2.append(
                    ([row[2], row[3], row[9], row[12], row[4], row[7], row[6], row[6], row[13], row[11]]))

        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL K", e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()

            return var2


def get_ide(ques, ans, ques2, ans2, fld):

    #dataBseN = tablevariable.databaseName
    ansssss = ""
    ansssssI = 0
    var2 = []
    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=tablevariable.databaseName)
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select * from ide Where " + ques + " = '" + ans + "' and " + \
            ques2 + " = '" + ans2 + "' and hostID = '" + tablevariable.hostID + \
            "' and frmId = '" + tablevariable.firmIdS + "'"
        if ques2 == "null":
            qurry = "Select * from ide Where " + ques + " = '" + \
                ans + "' and hostID = '" + tablevariable.hostID + \
                "' and frmId = '" + tablevariable.firmIdS + "'"
        if ques == "last":
            qurry = "Select * from ide Order By dttm DESC LIMIT 1"
        if ques == "newBilNo":

            qurry = "Select * from ide Where whyv = '" + tablevariable.projectCur + "' and frmId = '" + \
                tablevariable.firmIdS + "' and hostID = '" + \
                tablevariable.hostID + "' Order By ent DESC LIMIT 1"
        if ques == "newEntNo":
            qurry = "Select * from ide Where frmId = '" + \
                tablevariable.firmIdS + "' and hostID = '" + \
                tablevariable.hostID + "' Order By t_ent DESC LIMIT 1"

        mycursor.execute(qurry)
        records = mycursor.fetchall()

        if len(records) == 0:
            if ques == "last":
                tablevariable.grt_ide = "48000"
                tablevariable.srt_ide = "670"
                tablevariable.datee_ide = "1-1-20"
                tablevariable.dttm_ide = "1-1-20"
                return "48000"
                print(tablevariable.dttm_ide)
            if ques == "newBilNo":
                tablevariable.newBilNo = 1
                return 1
            if ques == "newEntNo":
                tablevariable.newT_ent = 1
                return 1

        for row in records:
            if ans2 == "full":
                var2 = row
                return var2
            if ques == "last":
                tablevariable.grt_ide = row[3]
                tablevariable.srt_ide = row[4]
                tablevariable.datee_ide = str(row[1])
                tablevariable.dttm_ide = str(row[11])
                return ""
                print(row[11])
            if ques == "newBilNo":
                tablevariable.newBilNo = int(row[9]) + 1
                return int(row[9]) + 1
            if ques == "newEntNo":
                tablevariable.newT_ent = int(row[10]) + 1
                return int(row[10]) + 1
        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL", e)

    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()


def get_by_id(idd, tblName, database):
    lstrr = 0
    accDetailA = []
    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=database)
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select * from " + tblName + " Where ID = '" + str(idd) + "' and  frmId  = '" + \
            str(tablevariable.firmId) + "' and hostID = '" + \
            str(tablevariable.hostID) + "'"
        mycursor.execute(qurry)
        records = mycursor.fetchall()
        for row in records:
            for ro in range(len(row)):
                accDetailA.append(row[ro])

        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL K", e)
    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()

            return accDetailA
        


def priDetail(namet, wht,databaseN):
    var2 = {}
    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=databaseN)
        mycursor = myDbs.cursor(buffered=True)

        qurry = "Select * from  rates  Where namet = '" + namet + "' and name = '" + wht + "' and " \
            "hostID = '" + tablevariable.hostID + \
            "' and frmId = '" + tablevariable.firmIdS + "'"
        print('qua   ',qurry)
        mycursor.execute(qurry)
        records = mycursor.fetchall()
        for row in records:

            if row[6] == None:
                ss = 0
            else:
                ss = round(row[6])

            var2 = row# {"wht": row[8], "typ": row[3], "sfn": ss, "ref": row[7]}
            print('var2',row)
        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL", e)

    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()
            return var2



def getTyp(nm):
    var2 = {}
    typppp = ""
    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=tablevariable.databaseName)
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select * from  accountt  Where nm = '" + nm + "' and wht != 'Rate' and " \
            "hostID = '" + tablevariable.hostID + \
            "' and frmId = '" + tablevariable.firmIdS + "'"

        mycursor.execute(qurry)
        records = mycursor.fetchall()
        for row in records:
            if row[8] in ['RateTW']:
                typppp = 'Prefix'
            else:
                typppp = row[8]

        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL", e)

    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()
            return typppp


def item_EntDetail(itemV, pri, metal, dataBName):
    if not dataBName:
        dataBName = tablevariable.databaseName
    var2 = {}
    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=dataBName)
        mycursor = myDbs.cursor(buffered=True)
        print("AAD :", itemV + "/" + pri)
        qurry = "Select * from  itemcode  Where nm = '" + itemV + "' and pri ='" + pri +  \
            "' and hostID = '" + tablevariable.hostID + \
            "' and frmId = '" + tablevariable.firmIdS + "'"
        if metal:
            qurry = "Select * from  itemcode  Where nm = '" + itemV + "' and pri ='" + pri +  \
                "' and met = '" + metal + "' and hostID = '" + tablevariable.hostID + \
                "' and frmId = '" + tablevariable.firmIdS + "'"

        mycursor.execute(qurry)
        records = mycursor.fetchall()
        for row in records:

            var2 = {"fxCd": row[11], "typ": row[3], "wt": float(
                row[5]), "lc": row[14], "hindi": row[16]}

        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL", e)

    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()
            return var2


def get_dataaaa(ques, ans, ques2, ans2, fld, tableName, databaseName, typ):
    ansssss = ""
    ansssssI = 0

    var2 = []
    if databaseName == "null":
        databaseName = tablevariable.databaseName
    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=databaseName)
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select * from " + tableName + " Where " + ques + " = '" + ans + \
            "' and " + ques2 + " = '" + ans2 + "' and hostID = '" + tablevariable.hostID + "'"
        if ques2 == "null":
            qurry = "Select * from " + tableName + " Where " + ques + " = '" + \
                ans + "' and hostID = '" + tablevariable.hostID + "'"
        if ans2 == "newCode":
            qurry = "Select * from gst Where item = '" + ques + \
                    "' and met = '" + ans + "' and hostID = '" + tablevariable.hostID + "' Order by cdno DESC LIMIT 1"
                    
       # print('Fixxxxxx   : ' , qurry)
        mycursor.execute(qurry)
        records = mycursor.fetchall()
        print("dssa", qurry)
        for row in records:
            if typ == "s1":
                ansssss = row[fld]
                break
            if typ == "s":

                ansssss = row[fld]
            if typ == "i":
                ansssssI = row[fld]
            
        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL", e)

    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()

            if typ in ["s", 's1']:
                return ansssss
            if typ == "i":
                return ansssssI
            return "null"


def get_dataaaaFull(ques, ans, ques2, ans2, tableName, databaseName):
    ansssss = ""
    ansssssI = 0

    var2 = []
    if databaseName == "null":
        databaseName = tablevariable.databaseName
    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=databaseName)
        mycursor = myDbs.cursor(buffered=True)
        qurry = "Select * from " + tableName + " Where " + ques + " = '" + ans + \
            "' and " + ques2 + " = '" + ans2 + "' and hostID = '" + tablevariable.hostID + "'"
        if ques2 == "null":
            qurry = "Select * from " + tableName + " Where " + ques + " = '" + \
                ans + "' and hostID = '" + tablevariable.hostID + "'"
        mycursor.execute(qurry)
        records = mycursor.fetchall()
        for row in records:
            var2 = row

        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL", e)

    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()

            return var2


def openLana(nameV, num, wht):
    if num in [1, 3]:
        databaseName = 'addd'
    if num == 2:
        databaseName = 'apru'
    ansssssI = 0
    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=databaseName)
        mycursor = myDbs.cursor(buffered=True)
        qurry = "SELECT  " + wht + " from accountt Where nm = %s and wht = 'Ledger' and frmId = '" + tablevariable.firmIdS + \
            "' and hostID = '" + tablevariable.hostID + "'"

        ansss = (nameV,)

        mycursor.execute(qurry, ansss)
        rowD = mycursor.fetchall()[0]
        ansssssI = repo.toFloat(rowD[0])
        mycursor.close()
    except Error as e:
        print(errrrConect + "MySQL sumAAll", e)

    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()

            # if ansssssI == None:
            #     ansssssI = 0
            # ansssssI = float(ansssssI)
            return ansssssI


def accSumByAAll(nameV, dt1, dt2, wht, num, openLanaB, rndOf):
    ansssssI = 0
    if num in [1, 2, 3]:
        ansssssI = float(accSumByAAll22(nameV, dt1, dt2, wht, num))
    elif num == 31:
        ansssssI = float(accSumByAAll22(
            nameV, dt1, dt2, wht, 1)) + float(accSumByAAll22(nameV, dt1, dt2, wht, 3))

    elif num == 32:
        ansssssI = float(accSumByAAll22(
            nameV, dt1, dt2, wht, 2)) + float(accSumByAAll22(nameV, dt1, dt2, wht, 3))

    if openLanaB == True:
        if num == 31:
            num = 3
        if num == 32:
            num = 2

        opop = openLana(nameV, num, wht)

        ansssssI += float(opop)

    return repo.rem_0(str(round(ansssssI, rndOf)))


def accSumByAAll22(nameV, dt1, dt2, wht, num):
    ansssss = ""
    ansssssI22 = 0

    if num in [1, 3, 4]:
        databaseName = 'addd'
    if num == 2:
        databaseName = 'apru'
    if wht == 'rs':
        fld = 'rscr'
        fld2 = 'rsdb'
    if wht == 'sfn' or wht == 'gfn':
        fld = 'fncr'
        fld2 = 'fndb'

    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=databaseName)
        mycursor = myDbs.cursor(buffered=True)
        qurry = "SELECT  Sum(" + fld + "),Sum(" + fld2 + ") from AAll Where item = %s and frmId = '" + tablevariable.firmIdS + \
            "' and hostID = '" + tablevariable.hostID + "'"
        ansss = (nameV,)
        if num in [1, 3, ]:
            qurry = qurry + " and num = '" + str(num) + "'"
        if wht == 'sfn':
            qurry = qurry + " and proMet = 'Silver'"
        if wht == 'gfn':
            qurry = qurry + " and proMet = 'Gold'"
        if isdate(dt2):
            if not isdate(dt1):
                dt1 = openFirmData('sdate')
        if isdate(dt1):
            if not isdate(dt2):
                dt2 = repo.todayDate('dd-mm-yy')
            qurry = qurry + " and datee between %s and %s"
            dtt1 = repo.dateConvert(dt1, "yyyy-mm-dd")
            dtt2 = repo.dateConvert(dt2, "yyyy-mm-dd")
            ansss = (nameV, dtt1, dtt2)

        # qurry = "SELECT  Sum(" + fld + "),Sum(" + fld2 + ") from AAll Where item = '" + nameV + "' and " + ques2 + " = '" + \
        # qurry = "SELECT  Sum(%s),Sum(%s) from AAll Where item = %s and frmId = '" + tablevariable.firmIdS + \
        #         "' and hostID = '" + tablevariable.hostID + "'"
        # # qurry = "SELECT  Sum(" + fld + "),Sum(" + fld2 + ") from AAll Where item = '" + nameV + "' and " + ques2 + " = '" + \
        #     ans2 + "' and frmId = '" + tablevariable.firmIdS + \
        #         "' and hostID = '" + tablevariable.hostID + "'"
        # if ques2 == "null":
        #     qurry = "SELECT  Sum(" + fld + ") from AAll Where " + ques + " = '" + ans + "' and frmId = '" + \

        #         tablevariable.firmIdS + "' and hostID = '" + tablevariable.hostID + "'"

        # ansss = ('rscr', 'rsdb', 'Ashish Jan')

        mycursor.execute(qurry, ansss)
        rowD = mycursor.fetchall()[0]
        ansssssI22 = repo.toFloat(rowD[1])-repo.toFloat(rowD[0])
        mycursor.close()

    except Error as e:
        print(errrrConect + "MySQL sumAAll", e)

    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()

            if ansssssI22 == None:
                ansssssI22 = 0
            ansssssI22 = float(ansssssI22)
            return ansssssI22


def isdate(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


def sumAAll(ques, ans, ques2, ans2, fld, databaseName):
    ansssss = ""
    ansssssI = 0

    sumAAllI = 0
    if databaseName == "null":
        databaseName = tablevariable.databaseName

    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=databaseName)
        mycursor = myDbs.cursor(buffered=True)
        qurry = "SELECT  Sum(" + fld + ") from aall Where " + ques + " = '" + ans + "' and " + ques2 + " = '" + \
            ans2 + "' and frmId = '" + tablevariable.firmIdS + \
            "' and hostID = '" + tablevariable.hostID + "'"
        if ques2 == "null":
            qurry = "SELECT  Sum(" + fld + ") from aall Where " + ques + " = '" + ans + "' and frmId = '" + \
                tablevariable.firmIdS + "' and hostID = '" + tablevariable.hostID + "'"

        mycursor.execute(qurry)
        sumAAllI = mycursor.fetchall()[0][0]

        mycursor.close()

    except Error as e:
        print(errrrConect + "MySQL sumAAll", e)

    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()

            if sumAAllI == None:
                sumAAllI = 0
            sumAAllI = float(sumAAllI)
            return sumAAllI


def sumAAll33(ques, ans, ques2, ans2, fld, databaseName, num):
    ansssss = ""
    ansssssI = 0

    sumAAllI = 0
    if databaseName == "null":
        databaseName = tablevariable.databaseName

    try:
        myDbs = mysql.connector.connect(
            host='localhost', user='root', password='', database=databaseName)
        mycursor = myDbs.cursor(buffered=True)
        qurry = "SELECT  Sum(" + fld + ") from AAll Where " + ques + " = '" + ans + "' and " + ques2 + " = '" + \
            ans2 + "' and num = '" + num + "' and frmId = '" + tablevariable.firmIdS + \
            "' and hostID = '" + tablevariable.hostID + "'"

        mycursor.execute(qurry)
        sumAAllI = mycursor.fetchall()[0][0]

        mycursor.close()

    except Error as e:
        print(errrrConect + "MySQL sumAAll", e)

    finally:
        # closing database connection.
        if (myDbs.is_connected()):
            myDbs.close()

            if sumAAllI == None:
                sumAAllI = 0
            sumAAllI = float(sumAAllI)
            return sumAAllI

def databaseList(wht,databaseName):
    if wht =='DATABASES':
        client = mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd=""
                                     )
    if wht == 'TABLES':
        client = mysql.connector.connect(
            host='localhost', user='root', passwd='', database=databaseName)
        
    mycursor = client.cursor()
    mycursor.execute("SHOW " + wht)

    firstDatabase = False

    listlist = []
    for x in mycursor:
            listlist.append(x[0])
    print('LPLPLP ',listlist)
    return listlist
    mycursor.close()
  
def checkdatabase():
    client = mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd=""
                                     )
    mycursor = client.cursor()

    mycursor.execute("SHOW DATABASES")

    firstDatabase = False
    for x in mycursor:

        if x[0] == "settingm":

            firstDatabase = True
    mycursor.close()
    if firstDatabase == False:

        createdatabase()

        return True

    return False


def createdatabase():

    # 21296570

    mydb = mysql.connector.connect(host='localhost', user='root', passwd='')
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE  IF NOT EXISTS  addd")
    mycursor.execute("CREATE DATABASE  IF NOT EXISTS  apru")
    mycursor.execute("CREATE DATABASE  IF NOT EXISTS  settingg")
    mycursor.execute("CREATE DATABASE  IF NOT EXISTS  wholename")
    mycursor.execute("CREATE DATABASE  IF NOT EXISTS  addac")
    mycursor.execute("CREATE DATABASE  IF NOT EXISTS  settingm")
    createTable("addd")
    createTable("apru")
    createTable("settingg")
    createTable("settingm")
    createTable("wholename")
    createTable("addac")
    mycursor.close()
   # connectDB()


def addColoumn(databaseName, table_name, fld, qurry, afterr):
    try:
        dbbbb = mysql.connector.connect(
            host='localhost', user='root', passwd='', database=databaseName)
        mycursor = dbbbb.cursor()
        mycursor.execute("ALTER TABLE " + table_name + " ADD " +
                         fld + " " + qurry + " NOT NULL After " + afterr)

    except Error as e:
        print("Coloumn Exist")


def createTableOne(databaseName, tblN):
    dbbbb = mysql.connector.connect(
        host='localhost', user='root', passwd='', database=databaseName)
    mycursor = dbbbb.cursor()
    if databaseName == "addac":
        if tblN == "datess":
            quarryy = "CREATE TABLE  IF NOT EXISTS  datess(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
                "datee DATE," \
                "wht VARCHAR(10)," \
                "head VARCHAR(10)," \
                "acc INT" \
                ")"
        if tblN == "rates":
            quarryy = "CREATE TABLE  IF NOT EXISTS  rates(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
                "metalt VARCHAR(10)," \
                "namet VARCHAR(100)," \
                "snot INT," \
                "rtt DECIMAL(10,2)," \
                "rtut VARCHAR(10)," \
                "mkt DECIMAL(10,2)," \
                "mkut VARCHAR(10)," \
                "hsnt VARCHAR(10)," \
                "gstt DECIMAL(10,2)," \
                "pert DECIMAL(10,2)," \
                "name VARCHAR(50)," \
                "short VARCHAR(50)," \
                "head VARCHAR(50)," \
                "head2 VARCHAR(50)," \
                "datee DATE," \
                "frmId INT," \
                "hostID VARCHAR(10)" \
                ")"
             
    if databaseName == "addd" or databaseName == "apru" or databaseName == "addac":
        if tblN == 'lesswt':
            quarryy = "CREATE TABLE  IF NOT EXISTS  lesswt(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
                "allNum INT ," \
                "name VARCHAR(50)," \
                "pcs INT ," \
                "wt DECIMAL(10,3), " \
                "rt INT ," \
                "unit VARCHAR(5)," \
                "rs INT ," \
                "less VARCHAR(5)," \
                "qua VARCHAR(50)," \
                "oriOrCh VARCHAR(5)," \
                "t_ent_no INT," \
                "num INT," \
                "datee DATE," \
                "frmId INT ," \
                "hostID VARCHAR(10)" \
                ")"
            mycursor.execute(quarryy)
        if tblN == "AAll":
            quarryy = "CREATE TABLE  IF NOT EXISTS  AAll(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
                "datee DATE," \
                "item VARCHAR(100)," \
                "prtname VARCHAR(100)," \
                "met VARCHAR(20)," \
                "wt DECIMAL(10,3), " \
                "rtrs DECIMAL(10,1), " \
                "rtfn DECIMAL(10,1), " \
                "rscr DECIMAL(10,1), " \
                "rsdb DECIMAL(10,1), " \
                "fncr DECIMAL(10,3), " \
                "fndb DECIMAL(10,3), " \
                "why VARCHAR(40)," \
                "code VARCHAR(40)," \
                "tch DECIMAL(10,2), " \
                "ves DECIMAL(10,3), " \
                "mak DECIMAL(10,1), " \
                "makunit VARCHAR(40)," \
                "make DECIMAL(10,1), " \
                "detail VARCHAR(40)," \
                "mcd VARCHAR(40)," \
                "AccTyp VARCHAR(40)," \
                "ent INT ," \
                "pri VARCHAR(40)," \
                "suf VARCHAR(40)," \
                "crdr VARCHAR(40)," \
                "num INT ," \
                "comm VARCHAR(200)," \
                "entryno INT ," \
                "totalent DECIMAL(10,0), " \
                "pcs INT, " \
                "wttt DECIMAL(10,3), " \
                "stwt DECIMAL(10,3), " \
                "st_name VARCHAR(40)," \
                "strs DECIMAL(10,1), " \
                "gwt DECIMAL(10,3), " \
                "item_fn DECIMAL(10,3), " \
                "sgst DECIMAL(10,2), " \
                "cgst DECIMAL(10,2), " \
                "igst DECIMAL(10,2), " \
                "t_entno INT, " \
                "wastage DECIMAL(10,3) ," \
                "metal_rs DECIMAL(10,2), " \
                "hm_ch INT, " \
                "type2 VARCHAR(100)," \
                "proMet VARCHAR(10)," \
                "huid VARCHAR(40)," \
                "frmId INT ," \
                "hostID VARCHAR(10)" \
                ")"

    mycursor.execute(quarryy)
    mycursor.close()


def insert_rates(dataa):
    myDbs = mysql.connector.connect(
        host='localhost', user='root', password='', database='addac')
    mycursor = myDbs.cursor(buffered=True)

    querry = "insert into rates(ID, metalt, namet, snot, rtt, rtut, mkt, mkut, hsnt, gstt, pert, name, short, head, head2, datee,frmId,hostID )" \
             " values(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s,%s,%s)"

    mycursor.execute(querry, dataa)
    lID = mycursor.lastrowid
    myDbs.commit()
    mycursor.close()
    return lID
def createTable(databaseName):
    dbbbb = mysql.connector.connect(
        host='localhost', user='root', passwd='', database=databaseName)
    mycursor = dbbbb.cursor()
    if databaseName == "addac":

        quarryy = "CREATE TABLE  IF NOT EXISTS  gst(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
            "item VARCHAR(60)," \
                  "suf VARCHAR(40)," \
                  "cd VARCHAR(20)," \
                  "wt DECIMAL(10.3), " \
                  "mak INT, " \
                  "mkUnit VARCHAR(5)," \
                  "rtPer DECIMAL(10,3), " \
                  "prty VARCHAR(5)," \
                  "cost VARCHAR(15)," \
                  "pri VARCHAR(40)," \
                  "met VARCHAR(20)," \
                  "ent INT, " \
                  "comm VARCHAR(200)," \
                  "cdno INT, " \
                  "wtDiff DECIMAL(10,3), " \
                  "gwt DECIMAL(10,3), " \
                  "stwt DECIMAL(10,3), " \
                  "strs DECIMAL(10,3), " \
                  "stnm VARCHAR(40)," \
                  "wastPer DECIMAL(10,3), " \
                  "west DECIMAL(10,3), " \
                  "hmCh INT, " \
                  "fn DECIMAL(10,3), " \
                  "saleWT DECIMAL(10,3), " \
                  "saleFn DECIMAL(10,3), " \
                  "huid VARCHAR(40)," \
                  "pic VARCHAR(100)," \
                  "comm2 VARCHAR(40)," \
                  "datee DATE," \
                  "saleent INT," \
                  "saleNum INT," \
                  "saledatee DATE," \
                 "frmId INT," \
                  "hostID VARCHAR(10)" \
            ")"

        mycursor.execute(quarryy)
        quarryy = "CREATE TABLE  IF NOT EXISTS  rates(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
                "metalt VARCHAR(10)," \
                "namet VARCHAR(100)," \
                "snot INT," \
                "rtt DECIMAL(10,2)," \
                "rtut VARCHAR(10)," \
                "mkt DECIMAL(10,2)," \
                "mkut VARCHAR(10)," \
                "hsnt VARCHAR(10)," \
                "gstt DECIMAL(10,2)," \
                "pert DECIMAL(10,2)," \
                "name VARCHAR(50)," \
                "short VARCHAR(50)," \
                "head VARCHAR(50)," \
                "head2 VARCHAR(50)," \
                "datee DATE" \
                "frmId INT," \
                "hostID VARCHAR(10)" \
                ")"
        mycursor.execute(quarryy)
            
        quarryy = "CREATE TABLE  IF NOT EXISTS  dast(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
            "item VARCHAR(60)," \
                  "prty VARCHAR(20)," \
                  "pcode VARCHAR(20)," \
                  "cd INT," \
                  "fcode VARCHAR(4)," \
                  "gwt DECIMAL(10,3), " \
                  "gPer DECIMAL(10,3), " \
                  "grt DECIMAL(10,3), " \
                  "grs DECIMAL(10,3), " \
                  "mak INT, " \
                  "mkUnit VARCHAR(5)," \
                  "cer INT," \
                  "dpcs INT," \
                  "dwt DECIMAL(10,3), " \
                  "drt INT, " \
                  "drs INT, " \
                  "stpcs INT," \
                  "stwt DECIMAL(10,3), " \
                  "strt INT, " \
                  "strs INT, " \
                  "cost INT, " \
                  "pprize INT, " \
                  "sprize INT, " \
                  "crdr VARCHAR(5)," \
                  "pri VARCHAR(40)," \
                  "ent INT, " \
                  "comm VARCHAR(200)," \
            "datee DATE," \
                  "saleent INT," \
                  "saleNum INT," \
                  "saledatee DATE," \
                  "frmId INT," \
                  "hostID VARCHAR(10)" \
                  ")"

        mycursor.execute(quarryy)

    if databaseName == "addd" or databaseName == "apru" or databaseName == "addac":

        quarryy = "CREATE TABLE  IF NOT EXISTS  lesswt(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
            "allNum INT ," \
            "name VARCHAR(50)," \
            "pcs INT ," \
            "wt DECIMAL(10,3), " \
            "rt INT ," \
            "unit VARCHAR(5)," \
            "rs INT ," \
            "less VARCHAR(5)," \
            "qua VARCHAR(50)," \
            "oriOrCh VARCHAR(5)," \
            "t_ent_no INT," \
            "num INT," \
            "datee DATE," \
            "frmId INT ," \
            "hostID VARCHAR(10)" \
            ")"
        mycursor.execute(quarryy)
        quarryy = "CREATE TABLE  IF NOT EXISTS  AAll(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
            "datee DATE," \
                  "item VARCHAR(100)," \
                  "prtname VARCHAR(100)," \
                  "met VARCHAR(20)," \
                  "wt DECIMAL(10,3), " \
                  "rtrs DECIMAL(10,1), " \
                  "rtfn DECIMAL(10,1), " \
                  "rscr DECIMAL(10,1), " \
                  "rsdb DECIMAL(10,1), " \
                  "fncr DECIMAL(10,3), " \
                  "fndb DECIMAL(10,3), " \
                  "why VARCHAR(40)," \
                  "code VARCHAR(40)," \
                  "tch DECIMAL(10,2), " \
                  "ves DECIMAL(10,3), " \
                  "mak DECIMAL(10,1), " \
                  "makunit VARCHAR(40)," \
                  "make DECIMAL(10,1), " \
                  "detail VARCHAR(40)," \
                  "mcd VARCHAR(40)," \
                  "AccTyp VARCHAR(40)," \
                  "ent INT ," \
                  "pri VARCHAR(40)," \
                  "suf VARCHAR(40)," \
                  "crdr VARCHAR(40)," \
                  "num INT ," \
                  "comm VARCHAR(200)," \
                  "entryno INT ," \
                  "totalent DECIMAL(10,0), " \
                  "pcs INT, " \
                  "wttt DECIMAL(10,3), " \
                  "stwt DECIMAL(10,3), " \
                  "st_name VARCHAR(40)," \
                  "strs DECIMAL(10,1), " \
                  "gwt DECIMAL(10,3), " \
                  "item_fn DECIMAL(10,3), " \
                  "sgst DECIMAL(10,2), " \
                  "cgst DECIMAL(10,2), " \
                  "igst DECIMAL(10,2), " \
                  "t_entno INT, " \
                  "wastage DECIMAL(10,3) ," \
                  "metal_rs DECIMAL(10,2), " \
                  "hm_ch INT, " \
                  "type2 VARCHAR(100)," \
                  "proMet VARCHAR(10)," \
                  "huid VARCHAR(40)," \
                  "frmId INT ," \
                  "hostID VARCHAR(10)" \
                  ")"

        mycursor.execute(quarryy)
        quarryy = "CREATE TABLE  IF NOT EXISTS  Accountt(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
            "datee DATE," \
                  "nm VARCHAR(200)," \
                  "typ VARCHAR(40)," \
                  "rs DECIMAL(10,2), " \
                  "gfn DECIMAL(10,3), " \
                  "sfn DECIMAL(10,3), " \
                  "ref VARCHAR(40)," \
                  "wht VARCHAR(40)," \
                  "info VARCHAR(40)," \
                  "num INT, " \
                  "hindi VARCHAR(100)," \
                  "comm VARCHAR(100)," \
                  "headd VARCHAR(40)," \
                  "headddd VARCHAR(40)," \
                  "sno INT ," \
                  "frmId INT ," \
                  "hostID VARCHAR(10)" \
                  ")"

        mycursor.execute(quarryy)
        quarryy = "CREATE TABLE  IF NOT EXISTS  itemcode(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
            "datee DATE," \
                  "nm VARCHAR(200)," \
                  "typ VARCHAR(40)," \
                  "pcs INT, " \
                  "lessWt DECIMAL(10,3), " \
                  "wtv DECIMAL(10,3), " \
                  "fn DECIMAL(10,3), " \
                  "mk DECIMAL(10,2), " \
                  "Rate VARCHAR(40)," \
                  "rs DECIMAL(10,2), " \
                  "fixCode VARCHAR(40)," \
                  "pri VARCHAR(40)," \
                  "met VARCHAR(40)," \
                  "pc_it INT, " \
                  "headd VARCHAR(40)," \
                  "headddd VARCHAR(40)," \
                  "hindi VARCHAR(100)," \
                  "frmId INT ," \
                  "hostID VARCHAR(10)" \
                  ")"

        mycursor.execute(quarryy)

        quarryy = "CREATE TABLE  IF NOT EXISTS  ide(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
            "datee DATE," \
                  "whyv VARCHAR(30)," \
                  "grt VARCHAR(10)," \
                  "srt VARCHAR(10)," \
                  "a VARCHAR(10), " \
                  "met VARCHAR(10), " \
                  "yr INT, " \
                  "amt INT, " \
                  "ent INT, " \
                  "t_ent INT, " \
                  "prty VARCHAR(10)," \
                  "dttm DATETIME ," \
                  "comm VARCHAR(200)," \
                  "pro_n INT, " \
                  "head2 VARCHAR(40)," \
                  "frmId INT ," \
                  "hostID VARCHAR(10)" \
                  ")"

        mycursor.execute(quarryy)
        quarryy = "CREATE TABLE  IF NOT EXISTS  prty(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
            "datee DATE," \
                  "nm VARCHAR(100)," \
                  "adrs VARCHAR(200)," \
                  "ref VARCHAR(100)," \
                  "mob VARCHAR(20), " \
                  "mob2 VARCHAR(20), " \
                  "tel VARCHAR(20), " \
                  "eml VARCHAR(30), " \
                  "city VARCHAR(30), " \
                  "Vil VARCHAR(30), " \
                  "St VARCHAR(30), " \
                  "id1 VARCHAR(40), " \
                  "id2 VARCHAR(40), " \
                  "gst VARCHAR(20), " \
                  "typ VARCHAR(20), " \
                  "grp VARCHAR(20), " \
                  "num INT, " \
                  "frmId INT ," \
                  "hostID VARCHAR(10)" \
                  ")"

        mycursor.execute(quarryy)
        quarryy = "CREATE TABLE  IF NOT EXISTS  ordr(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
            "datee DATE," \
                  "prty VARCHAR(100)," \
                  "item VARCHAR(40)," \
                  "met VARCHAR(40)," \
                  "wt  DECIMAL(10,2), " \
                  "rt INT, " \
                  "mak INT, " \
                  "makUnit VARCHAR(5), " \
                  "size VARCHAR(30), " \
                  "calalog VARCHAR(30), " \
                  "page VARCHAR(10), " \
                  "semple VARCHAR(40), " \
                  "disc VARCHAR(200), " \
                  "pri VARCHAR(40), " \
                  "ddatee DATE ," \
                  "kari VARCHAR(20), " \
                  "karidt DATE ," \
                  "receivedt DATE ," \
                  "ent INT," \
                  "ordNo INT," \
                  "whatt VARCHAR(30)," \
                  "amt INT ," \
                  "t_ent INT," \
                  "num INT," \
                  "pic VARCHAR(120)," \
            "frmId INT ," \
                  "hostID VARCHAR(10)" \
            ")"

        mycursor.execute(quarryy)
    if databaseName == "settingm":

        quarryy = "CREATE TABLE  IF NOT EXISTS  dafault(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
            "datee DATE," \
                  "nm VARCHAR(100)," \
                  "tf TINYINT(1)," \
                  "defN INT," \
                  "def1 VARCHAR(200), " \
                  "def2 VARCHAR(200), " \
                  "def3 VARCHAR(200), " \
                  "def4 VARCHAR(20), " \
                  "head VARCHAR(20), " \
                  "frmId INT ," \
                  "hostID VARCHAR(10)" \
                  ")"

        mycursor.execute(quarryy)
    if databaseName == "settingg":
        quarryy = "CREATE TABLE  IF NOT EXISTS  dafault(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
            "datee DATE," \
                  "nm VARCHAR(100)," \
                  "tf TINYINT(1)," \
                  "defN INT," \
                  "def1 VARCHAR(200), " \
                  "def2 VARCHAR(200), " \
                  "def3 VARCHAR(200), " \
                  "def4 VARCHAR(20), " \
                  "head VARCHAR(20), " \
            "frmId INT ," \
                  "hostID VARCHAR(10)" \
                  ")"

        mycursor.execute(quarryy)
        quarryy = "CREATE TABLE  IF NOT EXISTS  txtsetting(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
            "datee DATE," \
                  "txt_lab VARCHAR(10)," \
                  "sno INT," \
                  "indexx INT," \
                  "hi INT," \
                  "widthh INT," \
                  "lefttX INT," \
                  "topY INT," \
                  "previousInd INT," \
                  "tabInd INT," \
                  "headIndex INT," \
                  "headCaption VARCHAR(20)," \
                  "visi TINYINT(1)," \
                  "enable TINYINT(1)," \
                  "colourr VARCHAR(20)," \
                  "project VARCHAR(200), " \
                  "def1 VARCHAR(200), " \
                  "def2 VARCHAR(200) ," \
                  "frmId INT ," \
                  "hostID VARCHAR(10)" \
                  ")"

        mycursor.execute(quarryy)
        quarryy = "CREATE TABLE  IF NOT EXISTS  printSetting(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
            "datee DATE ," \
            "name VARCHAR(200)," \
                  "L1 VARCHAR(200)," \
                  "L2 VARCHAR(20)," \
                  "L3 VARCHAR(20),"\
                  "L4 VARCHAR(20)," \
                  "L5 VARCHAR(20)," \
                  "L6 VARCHAR(20)," \
                  "L7 VARCHAR(20)," \
                  "L8 VARCHAR(30)," \
                  "L9 VARCHAR(20)," \
                  "L10 VARCHAR(20)," \
                  "L11 VARCHAR(20)," \
                  "L12 VARCHAR(20)," \
                  "L13 VARCHAR(20)," \
                  "L14 VARCHAR(20)," \
                  "L15 VARCHAR(20)," \
                  "L16 VARCHAR(20)," \
                  "frmId INT ," \
                  "hostID VARCHAR(10)" \
                  ")"

        mycursor.execute(quarryy)
        quarryy = "CREATE TABLE  IF NOT EXISTS  tempppp(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
            "wht VARCHAR(20)," \
                  "datee DATE," \
                  "datee2 DATE," \
                  "txt1 VARCHAR(250)," \
                  "txt2 VARCHAR(250)," \
                  "txt3 VARCHAR(100)," \
                  "txt4 VARCHAR(100)," \
                  "int1a INT," \
                  "int2a INT," \
                  "int3a INT," \
                  "int4a INT," \
                  "num1  DECIMAL(10,2), " \
                  "num2  DECIMAL(10,2), " \
                  "num3  DECIMAL(10,2), " \
                  "num4  DECIMAL(10,2) " \
            ")"

        mycursor.execute(quarryy)
    if databaseName == "wholename":

        quarryy = "CREATE TABLE  IF NOT EXISTS  TeleNo(ID INT NOT NULL AUTO_INCREMENT  PRIMARY KEY," \
            "datee DATE," \
                  "nm VARCHAR(100)," \
                  "adrs VARCHAR(200)," \
                  "ref VARCHAR(100)," \
                  "mob VARCHAR(20), " \
                  "mob2 VARCHAR(20), " \
                  "tel VARCHAR(20), " \
                  "tel2 VARCHAR(20), " \
                  "city VARCHAR(30), " \
                  "Vil VARCHAR(30), " \
                  "St VARCHAR(30), " \
                  "id1 VARCHAR(40), " \
                  "id2 VARCHAR(40), " \
                  "gst VARCHAR(20), " \
                  "grp VARCHAR(20), " \
                  "num INT, " \
            "frmId INT ," \
                  "hostID VARCHAR(10)" \
            ")"

        mycursor.execute(quarryy)
        mycursor.close()
