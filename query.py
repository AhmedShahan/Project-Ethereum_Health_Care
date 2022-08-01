import mysql.connector
from mysql.connector import Error
def ConnectORNOT():
    try:
        mydb = mysql.connector.connect(host='localhost',
                                            database='ethereum',
                                            user='root',
                                            password='')
        if mydb.is_connected():
            return True
            query(connection)
        else:
            return False
    except Error as e:
        print("Error while connecting to MySQL", e)
if ConnectORNOT():
    mydb = mysql.connector.connect(host='localhost',
                                            database='ethereum',
                                            user='root',
                                            password='')
    mycourser=mydb.cursor()
    def adminq(value):
        username=value["user"]
        Pass=value["Password"]
        mycourser.execute("SELECT userId FROM adminlog WHERE userId=%s AND pass=%s",(username,Pass))
        result=mycourser.fetchall()
        if result==[]:
            return False
        else:
            return True
        
        
    def doctorq(value):
        docuser=value["docuser"]
        docpass=value["docpass"]
        mycourser.execute("SELECT DocUser, DocPass FROM doctorlog WHERE DocUser=%s AND DocPass=%s",(docuser,docpass))
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
    #This section for Specialist
    def addSpecialist(getSpecialist):
        mycourser.execute("INSERT INTO specialist (SpList) VALUES (%s)",(getSpecialist,))
        mydb.commit()
        
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
        mydb.commit()
    
