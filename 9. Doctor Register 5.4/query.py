from turtle import Turtle
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
    ## BMDC_Reg Dname DOB Gender NID Passport Mobile Email PresentAddress ParmanentAddress BloodGroup
    def AddDocPersonalInfo(DocPerInfo):
        BMDCreg=DocPerInfo["bmdc"]
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
        mycourser.execute("INSERT INTO doctorinfo VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(BMDCreg,name,Dob,Gender,nid,passport,mobile,email,presentadd,parmanentadd,bloodgroup))
        connection.commit()
