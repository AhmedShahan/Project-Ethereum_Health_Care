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
        
        
############################(Doctor Personal Info)###################################################
    ## BMDC_Reg Dname DOB Gender NID Passport Mobile Email PresentAddress ParmanentAddress BloodGroup
    def AddDocPersonalInfo(DocPerInfo):
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
        mycourser.execute("INSERT INTO doctorinfo VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,Dob,Gender,nid,passport,mobile,email,presentadd,parmanentadd,bloodgroup))
        connection.commit()
############################ (Doctor Specialist)###################################################
    def findSpecialistID(Specialist):
        mycourser.execute("SELECT SpID FROM specialist WHERE SpList=%s",(Specialist,))
        result=mycourser.fetchall()
        return result
        
    def DocSpecialist(AllValues):
        BMDC=113
        Specialist=AllValues["_COMBO_"]
        SpecialistInList = list(itertools.chain(*Specialist))
        #print("Finding Original List",SpecialistInList)
        MyArray=[]
        
        for i in range(0,len(Specialist)):
            res1=findSpecialistID(SpecialistInList[i])
            for j in range(0,len(res1)):
                res2=res1[j]
                #res3=list(itertools.chain(*res2))
                MyArray.append(res2)
        #print(MyArray)
        SPID=list(itertools.chain(*MyArray))
        #print(SPID)
        length=len(SPID)
        #print(length)
        for k in range(0,length):
            yoyo=SPID[k]
            mycourser.execute("INSERT INTO docspecialist VALUES(%s,%s)",(BMDC,yoyo))
        connection.commit()           
            

        # for i in range(0,len(Specialist)):
        #     res=findSpecialistID(Specialist[i])
        #     res=list(itertools.chain(*Specialist))
        #     print(res)
        #for i in range(0,len(Specialist)):
            # SPID=findSpecialistID(SpecialistInList[i])
            # print(BMDC)
            # print(SPID)
            # mycourser.execute("INSERT INTO docspecialist1 VALUES(%s,%s)",(BMDC,SPID))
            # connection.commit()
        