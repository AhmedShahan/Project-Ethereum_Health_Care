from PySimpleGUI import *

import view as view


def patientwindow():
    theme("PythonPlus")
    theme_input_background_color("white")
    theme_input_text_color("Black")
    signup="static/images/signup.png"
    signin="static/images/signin.png"
    back="static/images/back.gif"

    frame=[
        [
        ReadFormButton('', button_color="#001d3c",image_filename=signup, image_size=(300, 80), image_subsample=2, border_width=0,key="signup")],
        [ReadFormButton('', button_color="#001d3c",image_filename=signin, image_size=(300, 80), image_subsample=2, border_width=0,key="signin"),
        ],
        [ReadFormButton('', button_color="#001d3c",image_filename=back, image_size=(300, 80), image_subsample=2, border_width=0,key="back")],
    ]

    layout=[
        [Text("\t"),Image("static/images/eth3.png")],
        [Text("***************************************************************"*10)],
        [Image("static/images/patient.png"),
        Frame("Sign as Patient",frame,font=("Jokerman",30),title_color="yellow")
        
        ], 
        ]



    doc=Window("Doctor Login",layout,size=(700,620),location=(500,100))


    while True:
        event,value=doc.read()
        if event==WIN_CLOSED:
            break
        elif event=="back":
            doc.close()
            view.view()
