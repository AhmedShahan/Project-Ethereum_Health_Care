from PySimpleGUI import *
from doctor import *
import login2 as log
import patient as pt
import administration1 as ad


def view():
    theme("PythonPlus")
    theme_input_background_color("white")
    theme_input_text_color("Black")
    theme_button_color("black")

    

    frame=[     
        [
            Button("Administration",size=(20,1),font=("Monotype Corsiva",20),key="proctor")
        ],  
        [
            Button("Doctor",size=(20,1),font=("Monotype Corsiva",20),key="doctor")
        ],  
        [
            Button("Patient",size=(20,1),font=("Monotype Corsiva",20),key="patient")
        ],  
        [
            Button("Notice Board",size=(20,1),font=("Monotype Corsiva",20),key="notice")
        ],  
        [
            Button("Search Your Doctor",size=(20,1),font=("Monotype Corsiva",20),key="searchDoc")
        ],  
        [
            Button("Test & Imaging",size=(20,1),font=("Monotype Corsiva",20),key="test")
        ],  
        [
            Button("FAQ",size=(20,1),font=("Monotype Corsiva",20),key="faq")
        ],  
    ]

    layout=[
        [Text("\t"),Frame("Select Your Module",frame,font=("Monotype Corsiva",20))],
        [
            Text("\t\t       "),
            ReadFormButton('', button_color="#001d3c",image_filename="static/images/logout.png", image_size=(120, 50), image_subsample=2, border_width=0,key="logout"),
        ]
    ]

    view=Window("View Lavel",layout,size=(500,600))


    while True:
        event, value= view.read()
        
        if event=="Close" or event==WINDOW_CLOSED:
            break
        elif event=="proctor":
            view.close()
            ad.proctorview()
        elif event=="doctor":
            view.close()
            doctor()
        elif event=="logout":
            res=popup_ok_cancel("YOU WILL BE LOGED OUT\n!!!")
            if res=="OK":
                view.close()
                log.adminlog()
        elif event=="patient":
            view.close()
            pt.patientwindow()
            
            
            
            
            