from PySimpleGUI import *
from query import *
import view as v



def doctor():
    theme("PythonPlus")
    theme_input_background_color("white")
    theme_input_text_color("Black")

    login="login.png"
    back="back.gif"
    frame=[
        [
        Text("Dr User ID",size=(10,1),font=("Monotype Corsiva",20)),
        InputText("Hello Dr. Enter Your Doctor ID",size=(30,1),justification="center",font=("Monotype Corsiva",15),key="docuser"),
        ],
        [
        Text("Password ",size=(10,1),font=("Monotype Corsiva",20)),
        InputText(size=(30,1),password_char=("*"),justification="center",font=("Monotype Corsiva",15),default_text="Password",key="docpass"),
        ],
        [
            Text("\n\n\n\n\n"),
            ReadFormButton('', button_color="#001d3c",image_filename=back, image_size=(300, 80), image_subsample=2, border_width=0,key="back"),
            ReadFormButton('', button_color="#001d3c",image_filename=login, image_size=(170, 50), image_subsample=2, border_width=0,key="login"),
        ],
        [
            Text("1. Only the authorized can log into this software.\n2. Please Logout after using the software.\n3. This all information is based on website update.",size=(50,5),font=("Monotype Corsiva",15)),
        ]
    ]
    layout=[
        [Text("\t    "),Image("eth2.png")],
        [
            Frame("Sign in as a Doctor",frame,font=("Monotype Corsiva",20,"bold"),title_color="Yellow"),
            Image("docor.png",size=(200,500)),
        ],   
        ]



    doc=Window("Doctor Login",layout,size=(700,570),location=(500,100))


    while True:
        event,value=doc.read()
        if event==WIN_CLOSED:
            break
        elif event=="login":
            res=doctorq(value)
            if res:
                for i in range(1500):
                    popup_animated("my.gif",no_titlebar=True,background_color="black",location=(630,200),time_between_frames=30)
                popup_animated(None)
                Popup("Welcome\nYou ar successfylly logedin",font=("Monotype Corsiva",20),title="Authorized")            
                
            else:
                for i in range(1500):
                    popup_animated("my.gif",no_titlebar=True,background_color="black",location=(630,200),time_between_frames=30)
                popup_animated(None)
                Popup("SORRY\nYou NOT an Authorized Person.",font=("Monotype Corsiva",20),title="Unauthorized")

        elif event=="back":
            doc.close()
            v.view()