import imp
from PySimpleGUI import *
import view as view
import query as q
import administration2 as ad2

def proctorview():

    theme("PythonPlus")
    theme_input_background_color("white")
    theme_input_text_color("Black")


    frame=[
        [Image("static/images/user.png"),Input("Please Enter Administration User",font=("monotype Corsiva",15),justification="center",key="procuser")],
        [Image("static/images/pass.png"),InputText(password_char=("*"),justification="center",font=("Monotype Corsiva",15),default_text="12345",key="procpass")],
        [Text("\n")],
        [ReadFormButton('', button_color="#001d3c",image_filename="static/images/back 3.png", image_size=(200, 40), image_subsample=2, border_width=0,key="back"),
        ReadFormButton('', button_color="#001d3c",image_filename="static/images/next 3.png", image_size=(200, 40), image_subsample=2, border_width=0,key="next")],
        [Text("\n")],
    ]

    layout=[
        [Text("\t"),Image("static/images/eth3.png")],
        [Text("***************************************************************"*10)],
        [Image("static/images/adminis.png"),
        Frame("Sign as ADMINISTRATION",frame,font=("Jokerman",20),title_color="yellow")
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
        elif event=="next":
            res=q.Administration(value)
            if res:
                for i in range(1500):
                    popup_animated("static/images/my.gif",no_titlebar=True,background_color="black",location=(630,200),time_between_frames=30)
                popup_animated(None)
                Popup("Welcome\nYou ar successfylly logedin",font=("Monotype Corsiva",20),title="Authorized")
                doc.close()
                ad2.adminis()
            else:
                for i in range(1500):
                    popup_animated("static/images/my.gif",no_titlebar=True,background_color="black",location=(630,200),time_between_frames=30)
                popup_animated(None)
                Popup("SORRY\nYou NOT an Authorized Person.",font=("Monotype Corsiva",20),title="Unauthorized")
