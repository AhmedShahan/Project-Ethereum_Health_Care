from PySimpleGUI import *
import query as q
#import administration1 as ad1
# import doctorRegistation as doctorreg


def adminis():
    theme("DarkGreen4")
    theme_button_color("black")


    frame1=[
        [Button("Register a Doctor",size=(15,1),font=("Times & New Roman",15,"italic"),key="regdoc"),
        Button("See Doctor Details",size=(15,1),font=("Times & New Roman",15,"italic"),key="docDetail"),
        Button("Update Information",size=(15,1),font=("Times & New Roman",15,"italic"),key="UpdateDoc")],
    ]
    frame2=[
        [Button("Register a Patient",size=(15,1),font=("Times & New Roman",15,"italic"),key="regPat"),
        Button("See Patient Details",size=(15,1),font=("Times & New Roman",15,"italic"),key="patDetail"),
        Button("Update Information",size=(15,1),font=("Times & New Roman",15,"italic"),key="dpdatePat")],
    ]
    frame4=[
        [Button("Post a Notice",size=(15,1),font=("Times & New Roman",15,"italic"),key="pnotice"),
        Button("See Notice Board",size=(15,1),font=("Times & New Roman",15,"italic"),key="snotice")],
    ]
    frame3=[
        [Button("Test & Images",size=(15,1),font=("Times & New Roman",15,"italic"),key="test"),
        Button("Answer FAQ",size=(15,1),font=("Times & New Roman",15,"italic"),key="faq"),
        Button("Register Administration",size=(20,1),font=("Times & New Roman",15,"italic"),key="faq"),
        ],
    ]

    col1=[[Image("imageadmin22.png")]]
    col2=[
        [Frame("Doctor Section",frame1,font=("Monotype Corsiva",15),title_color="yellow")],
        [Frame("Patient Section",frame2,font=("Monotype Corsiva",15),title_color="yellow")],
        [Frame("Notice Section",frame3,font=("Monotype Corsiva",15),title_color="yellow")],
        [Frame("Other Section",frame4,font=("Monotype Corsiva",15),title_color="yellow")],
        [Text("")],
        [ReadFormButton('', button_color="#044343",image_filename="static/images/back2.png", image_size=(150, 50), image_subsample=2, border_width=0,key="back"),]
        
    ]
    layout=[
        [Text("\t\t\t"),Image("image/eth3.png")],
        [Text("***************************************************************"*10)],
        [Column(col1,element_justification="c"),Column(col2,element_justification="c")],

    ]

    doc=Window("Doctor Login",layout,size=(1000,600),location=(300,100))


    while True:
        event,value=doc.read()
        if event==WIN_CLOSED:
            break
        elif event=="back":
            pop=popup_ok_cancel("You will be loged Out!!!")
            if pop=="OK":
                doc.close()
                #ad1.proctorview()
        # elif event== "regdoc":
        #     doc.close()
        #     doctorreg.mainCode()
if q.ConnectORNOT():
    adminis()
else:
    popup_auto_close("Database is Not Connected",background_color="#007ACC",font=("Monotype Corsiva",20))