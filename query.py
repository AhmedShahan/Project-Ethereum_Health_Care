from PySimpleGUI import *
import mysql.connector
from mysql.connector import Error

def ConnectORNOT():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='ethereum',
                                            user='root',
                                            password='')
        if connection.is_connected():
            return True
            query(connection)
        else:
            return False
    except Error as e:
        print("Error while connecting to MySQL", e)


if ConnectORNOT():
    connection = mysql.connector.connect(host='localhost',
                                            database='ethereum',
                                            user='root',
                                            password='')
    mycourser=connection.cursor()
    
    #This section for Specialist
    def addSpecialist(getSpecialist):
        mycourser.execute("INSERT INTO specialist (SpList) VALUES (%s)",(getSpecialist,))
        connection.commit()
        
    def retriveSpecialist():
        mycourser.execute("SELECT SpList FROM specialist")
        result=mycourser.fetchall()
        return result
    
    
    # This section for medical History
    def retriveDegree():
        mycourser.execute("SELECT degreeList FROM medicaldegree")
        result=mycourser.fetchall()
        return result
    
    def addDegree(getDegree):        
        mycourser.execute("INSERT INTO medicaldegree (degreeList) VALUES (%s)",(getDegree,))
        connection.commit()
    def removeSpecialist(specialist):
        mycourser.execute("DELETE FROM specialist WHERE SpList=%s",(specialist,))
        connection.commit()
      
      
    def retirveAdminis():
        mycourser.execute("SELECT administrationID FROM administrationlog")
        result=mycourser.fetchall()
        return result

    def AddAdministrator(NewAdmin,password):
        mycourser.execute("INSERT INTO administrationlog VALUES (%s,%s)",(NewAdmin,password))
        connection.commit()
        
    def retriveBMDC():
        mycourser.execute("SELECT BMDC_Reg FROM doctorinfo")
        result=mycourser.fetchall()
        return result

    def AddDocID(GETBMDC,GETPASS):
        mycourser.execute("INSERT INTO doctorinfo (BMDC_Reg,Docpass) VALUES (%s,%s)",(GETBMDC,GETPASS))
        connection.commit()
        
        
    def doctorq(value):
        docuser=value["docuser"]
        docpass=value["docpass"]
        mycourser.execute("SELECT BMDC_Reg, Docpass FROM doctorinfo WHERE BMDC_Reg=%s AND Docpass=%s",(docuser,docpass))
        result=mycourser.fetchall()
        if result==[]:
            return False
        else:
            return True
    def adminq(value):
        username=value["user"]
        Pass=value["Password"]
        mycourser.execute("SELECT userId FROM adminlog WHERE userId=%s AND pass=%s",(username,Pass))
        result=mycourser.fetchall()
        if result==[]:
            return False
        else:
            return True
    def Administration(value):
        procuser=value["procuser"]
        procpass=value["procpass"]
        mycourser.execute("SELECT administrationID, administrationPass FROM Administrationlog WHERE administrationID=%s AND administrationPass=%s",(procuser,procpass))
        result=mycourser.fetchall()
        if result==[]:
            return False
        else:
            return True

############################ (Doctor Personal Info) ###################################################
    ## BMDC_Reg Dname DOB Gender NID Passport Mobile Email PresentAddress ParmanentAddress BloodGroup
    def UpdateDocPersonalInfo(DocPerInfo,BMDC):

        name=DocPerInfo["name"]
        Dob=DocPerInfo["DateOfBirth"]
        
        Gender=None
        if DocPerInfo[1]==True:
            Gender="Male"
        elif DocPerInfo[2]==True:
            Gender="Female"
        
        nid=DocPerInfo["nid"]
        passport=DocPerInfo["passport"]
        mobile=DocPerInfo["mobile"]
        email=DocPerInfo["email"]
        presentadd=DocPerInfo["present"]
        parmanentadd=DocPerInfo["parmanent"]
        
        
        bloodgroup=None
        bloodgrouplist=["O(+ve)","O(-ve)","A(+ve)","A(-ve)","B(+ve)","B(-ve)","AB(+ve)","AB(-ve)",]
        c=0
        for i in range(3,11):
            if DocPerInfo[i]:
                bloodgroup=bloodgrouplist[c]
                break
            c=c+1
        # print(name,BMDCreg,Dob,Gender,nid,mobile,passport,email,presentadd,parmanentadd,bloodgroup)
        ## BMDC_Reg Dname DOB Gender NID Passport Mobile Email PresentAddress ParmanentAddress BloodGroup
        mycourser.execute("UPDATE doctorinfo SET Dname=%s, DOB=%s,Gender=%s, NID=%s, Passport=%s, Mobile=%s, Email=%s, PresentAddress=%s, ParmanentAddress=%s, Bloodgroup=%s WHERE BMDC_Reg=%s",(name,Dob,Gender,nid,passport,mobile,email,presentadd,parmanentadd,bloodgroup,BMDC))
        connection.commit()
        
    
    def RetrivDoctorInfo(DocID):
        mycourser.execute("SELECT Dname,DOB,Gender,NID,Passport,Mobile,Email,PresentAddress,PresentAddress,Bloodgroup FROM doctorinfo WHERE BMDC_Reg=%s",(DocID,))
        result=mycourser.fetchall()
        return result
############################ (Doctor Specialist) ###################################################
    def findSpecialistID(Specialist):
        mycourser.execute("SELECT SpID FROM specialist WHERE SpList=%s",(Specialist,))
        result=mycourser.fetchall()
        return result
        
    def DocSpecialist(AllValues,BMDC):
        Specialist=AllValues["_COMBO_"]
        SpecialistInList = list(itertools.chain(*Specialist))
        #print("Finding Original List",SpecialistInList)
        MyArray=[]
        
        for i in range(0,len(Specialist)):
            res1=findSpecialistID(SpecialistInList[i])
            for j in range(0,len(res1)):
                res2=res1[j]
                MyArray.append(res2)
        SPID=list(itertools.chain(*MyArray))
        length=len(SPID)
        for k in range(0,length):
            yoyo=SPID[k]
            mycourser.execute("INSERT INTO docspecialist VALUES(%s,%s)",(BMDC,yoyo))
        connection.commit() 
