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
# if __name__ == "__main__":
#     main()
