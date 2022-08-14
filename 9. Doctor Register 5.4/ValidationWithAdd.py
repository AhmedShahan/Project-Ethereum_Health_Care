from ast import And
from PySimpleGUI import *    
#################################################
      # Form Validation
DocPersonalInfo=[]
def checkValidationDoctor(Allvalues):
    formValue="\tPlease Fillup This\n======================="
    isValied=True                
    if len(Allvalues["name"])==0:
        formValue=formValue + "\n"+ "Name"
        isValied= False
        
    if (Allvalues["DateOfBirth"])==False:
        formValue=formValue + "\n"+ "Date of Birth"
        isValied= False
    # if Allvalues[2]==False and Allvalues[3]==False:
    #     formValue=formValue + "\n"+ "Gender"
    #     isValied= False
    if len(Allvalues["nid"])==0:
        formValue=formValue + "\n"+ "NID"
        isValied= False
    # if len(Allvalues[5])==0:
    #     formValue=formValue + "\n"+ "Passport Number"
    #     isValied= False
    if len(Allvalues["mobile"])==0:
        formValue=formValue + "\n"+ "Mobile Number"
        isValied= False
    # if len(Allvalues[7])==0:
    #     formValue=formValue + "\n"+ "Email Address"
    #     isValied= False
    # ## 8 = present address, 9 = Parmanent address
    # if len(Allvalues[8])==0:
    #     formValue=formValue + "\n"+ "Passport Number"
    #     isValied= False
    ############## Blood Group ##########
    # bloodGroup=0
    # for i in range(10,18):
    #     if Allvalues[i]==True:
    #         bloodGroup=bloodGroup+1
    #         break
    # if bloodGroup==0:
    #     formValue=formValue + "\n"+ "Blood Group"
        
    
    if len(Allvalues["bmdc"])==0:
        formValue=formValue + "\n"+ "BMDC Registration Number"
        isValied= False
        
        
    ##### Specialist IN ===========
    # specialist=0
    # for i in range(len(Allvalues["_COMBO_"])):
    #     if len(Allvalues[i])==0:
    #         bloodGroup=bloodGroup+1
    #         break
    # if bloodGroup==0:
    #     formValue=formValue + "\n"+ "Specialist"
    
    
    result=[isValied,formValue]
    return result