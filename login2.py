from PySimpleGUI import *
from view import *
from query import *


def adminlog():
    theme("Black")
    theme_input_background_color("white")
    theme_input_text_color("Black")
    login="login.png"    
    layout=[
        
        [
            Text("ADMIN LOGIN",size=(30,1),justification="center",font=("Jokerman",30,"italic","underline")),
        ],
            [
            Text("\t"),
            Image('admin.png',size=(360,192)),
            ],
            [
            Text("\t"),
            Image('user.png'),
            InputText("shahan@202",size=(30,1),justification="center",font=("Monotype Corsiva",15),key="user"),
            ],
            [
            Text("\t"),
            Image('pass.png'),
            #Text("Password ",size=(10,1),font=("Monotype Corsiva",20)),
            InputText(size=(30,1),password_char=("*"),justification="center",font=("Monotype Corsiva",15),default_text="12345",key="Password"),
            ],     
            [
                Text("\t\t\t\n\n\n\n\n"),
                ReadFormButton('', button_color="black",image_filename=login, image_size=(170, 50), image_subsample=2, border_width=0,key="login"),
            ],     
            [
                Text("1. Only the authorized can log into this software.\n2. Please Logout after using the software.\n3. This all information is based on website update.",size=(100,8),font=("Monotype Corsiva",15)),
            ]   
    ]



    login=Window("Admin Login",layout,size=(500,570),location=(500,100))


    while True:
        event,value=login.read()
        if event==WIN_CLOSED:
            break
        elif event=="login":
            res=adminq(value)
            if res:
                for i in range(1500):
                    popup_animated("my1.gif",no_titlebar=True,background_color="black",location=(570,250),time_between_frames=25)
                popup_animated(None)
                Popup("Welcome\nYou ar successfylly logedin",font=("Monotype Corsiva",20),title="Authorized")
                login.close()
                view()
                
            else:
                for i in range(1500):
                    popup_animated("my1.gif",no_titlebar=True,background_color="black",location=(570,250),time_between_frames=25)
                popup_animated(None)
                Popup("SORRY\nYou NOT an Authorized Person.",font=("Monotype Corsiva",20),title="Unauthorized")

