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