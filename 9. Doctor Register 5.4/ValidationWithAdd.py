from ast import And
from msilib.schema import tables
from PySimpleGUI import *


def create(add_another_degree,headings):
    add_another_degree_Layout=[
        [Table(values=add_another_degree,headings=headings, max_col_width=35,
              auto_size_columns=True,
              display_row_numbers=True,
              justification="center",
              num_rows=10,
              key="table",
              row_height=35,
              tooltip="Adding Degree Table",
              background_color="#214162",
            #   visible_column_map="visible",
              enable_events=True,
              select_mode=TABLE_SELECT_MODE_BROWSE
              )]
    ]

    adding_degree=Window("Added Degree",add_another_degree_Layout,modal=True)
    
    while True:
        event,value=adding_degree.read()
        if event== "Exit" or event== WIN_CLOSED:
            break
    adding_degree.Close()
    
#################################################
      # Form Validation

def checkValidationDoctor(Allvalues,event):
    formValue="\tPlease Fillup This\n======================="
    isValied=True
    
    for key, value in Allvalues.items():
        if isinstance(value, str) or isinstance(value, list):
            if len(value)==0:
                formValue=formValue + "\n"+ str(key)
                isValied= False
    
    # if len(Allvalues[1])==0:
    #     formValue=formValue + "\n"+ "Name"
    #     isValied= False
    # if len(Allvalues["depart"])==0:
    #     formValue=formValue + "\n"+ "Date of Birth"
    #     isValied= False
    # if Allvalues[2]==False and Allvalues[3]==False:
    #     formValue=formValue + "\n"+ "Gender"
    #     isValied= False
    # if len(Allvalues[4])==0:
    #     formValue=formValue + "\n"+ "NID"
    #     isValied= False
    # if len(Allvalues[5])==0:
    #     formValue=formValue + "\n"+ "Passport Number"
    #     isValied= False
    # if len(Allvalues[6])==0:
    #     formValue=formValue + "\n"+ "Mobile Number"
    #     isValied= False
    # if len(Allvalues[7])==0:
    #     formValue=formValue + "\n"+ "Email Address"
    #     isValied= False
    # ## 8 = present address, 9 = Parmanent address
    # if len(Allvalues[8])==0:
    #     formValue=formValue + "\n"+ "Passport Number"
    #     isValied= False
    # ############## Blood Group ##########
    # bloodGroup=0
    # for i in range(10,18):
    #     if Allvalues[i]==True:
    #         bloodGroup=bloodGroup+1
    #         break
    # if bloodGroup==0:
    #     formValue=formValue + "\n"+ "Blood Group"
        
    
    # if len(Allvalues[18])==0:
    #     formValue=formValue + "\n"+ "BMDC Registration Number"
    #     isValied= False
        
        
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