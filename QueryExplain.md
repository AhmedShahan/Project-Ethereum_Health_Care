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




