from ast import And
from msilib.schema import tables
from PySimpleGUI import *    
#################################################
      # Form Validation
def checkValidationDoctor(Allvalues):
    formValue="\tPlease Fillup This\n======================="
    isValied=True                
    if len(Allvalues["name"])==0:
        formValue=formValue + "\n"+ "Name"
        isValied= False
        
    if (Allvalues["DateOfBirth"])==False:
        formValue=formValue + "\n"+ "Date of Birth"
        isValied= False
        
        
    if len(Allvalues["nid"])==0:
        formValue=formValue + "\n"+ "NID"
        isValied= False
        
        
    if len(Allvalues["mobile"])==0:
        formValue=formValue + "\n"+ "Mobile Number"
        isValied= False
        
    result=[isValied,formValue]
    return result