# Ethereum Healh Care Database SQL Command With Explanation

### Creating Ethereum Database
```mysql
CREATE DATABASE ethereum;
```

### Creating AdminLog Table Version I
```mysql
CREATE TABLE adminlog
(
    userId varchar(20),
    pass varchar (20),
    
    PRIMARY KEY (userID, pass)
);
````
Why userId and pass both are in Primary key?
There is no scope without creating a Admin without UserID and Password. 
You cannot log in without password. Along with both username & password should be one for one user. 
But there is a problem, userId & pass 2 makes the fileds Unique. 
Example: userName= shahan@201   pass=840223    (This is allowed)</br>
BUT      userName= shahan@201   pass=shahan    (This is not allowed)

<i>__So version II fixed it__</i>
### Creating AdminLog Table Version II
```mysql
CREATE TABLE adminlog
(
    userId varchar(20) PRIMARY KEY,
    pass varchar (20) NOT NULL,
);
````
### Creating AdministrationLog Table
```mysql
CREATE TABLE AdministrationLog
(
    administrationID varchar(20),
    administrationPass varchar(20),
    
    PRIMARY KEY (administrationID, administrationPass)
);
````
### Creating specialist Table
```mysql
CREATE TABLE Specialist(
    SpID int(3) AUTO_INCREMENT,
    SpList varchar(20) UNIQUE,
    PRIMARY KEY (SpID)
    );
````

### Creating Medical Degree Table
```mysql
CREATE TABLE medicalDegree(
    MedID int(3) AUTO_INCREMENT,
    DegreeList varchar(30) UNIQUE,
    Locations varchar(100),
    Zip_Code int(5),
    PRIMARY KEY (MedID)
    );
````

### To modify any column type
```mysql
ALTER TABLE table_name
CHANGE old_filed_Name New_Field_Name datatype;
````


## Table of Patient Info
```sql
create table patientInfo
( ID varchar(30) PRIMARY KEY, 
   Name varchar(20),
   DeathOfBirth varchar(20),
   Gender varchar(20),
   Age varchar (20),
   NID varchar(20),
   MobileNo int(20),
   Email varchar(20),
   PresentAddress varchar(30),
   PermanentAddress varchar(30),
   BloodGroup Varchar (30)
 );
 ```

## Table of doctor Info
```sql
create table DoctorInfo                  
(  BMDCReg varchar(30) PRIMARY KEY, 
   Name varchar(20),
   DeathOfBirth varchar(20),
   Gender varchar(20),
   NID varchar(20),
   Passport varchar(20),
   MobileNo int(20),
   Email varchar(20),
   PresentAddress varchar(30),
   PermanentAddress varchar(30),
   BloodGroup Varchar (30)
 );

``` 

## Table of Health Details
```sql
Create table HealthDetails
( Disease varchar(30),
  DiseaseId varchar(30) PRIMARY KEY AUTO_INCREMENT
 );
 ```

 ## Table of Paitent Log
 ```sql
 
Create table PatientLog
( PatientUser varchar(30),
  PatientId varchar(30) PRIMARY KEY AUTO_INCREMENT
 );

 ```
## PatientHealth Table 
 CREATE TABLE PatientHealth(
    DiseasID int(3),
    PatientID int(3),
    PRIMARY KEY(DiseasID,PatientID),
    FOREIGN KEY (DiseasID) REFERENCES healthdetails(DiseaseId) ON DELETE CASCADE, 
    FOREIGN KEY (PatientID) REFERENCES patientinfo(ID) ON DELETE CASCADE
);
