from PySimpleGUI import *
import query as q
import administration1 as ad1
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
        Button("Register Administration",size=(20,1),font=("Times & New Roman",15,"italic"),key="regAdmin"),
        ],
    ]

    col1=[[Image("static/images/admin22.png")]]
    col2=[
        [Frame("Doctor Section",frame1,font=("Monotype Corsiva",15),title_color="yellow")],
        [Frame("Patient Section",frame2,font=("Monotype Corsiva",15),title_color="yellow")],
        [Frame("Notice Section",frame3,font=("Monotype Corsiva",15),title_color="yellow")],
        [Frame("Other Section",frame4,font=("Monotype Corsiva",15),title_color="yellow")],
        [Text("")],
        [ReadFormButton('', button_color="#044343",image_filename="static/images/back2.png", image_size=(150, 50), image_subsample=2, border_width=0,key="back"),]
        
    ]
    layout=[
        [Text("\t\t\t"),Image("static/images/eth3.png")],
        [Text("***************************************************************"*10)],
        [Column(col1,element_justification="c"),Column(col2,element_justification="c")],

    ]

    doc=Window("Doctor Login",layout,size=(1000,600),location=(300,100))

    alltheAdministrator=q.retirveAdminis()
    administrator=list(itertools.chain(*alltheAdministrator))
    
    allBMDC=q.retriveBMDC()
    BMDCLIST = list(itertools.chain(*allBMDC))
    while True:
        event,value=doc.read()
        if event==WIN_CLOSED:
            break
        elif event=="back":
            pop=popup_ok_cancel("You will be loged Out!!!")
            if pop=="OK":
                doc.close()
                ad1.proctorview()
        
        elif event=="regAdmin":
            newUser= popup_get_text("Enter new Administartor UserID:")
            if newUser==None:
                continue
            elif newUser in administrator:
                popup("Already in the Administration list")
                continue
            else:
                newpass= popup_get_text("Enter new Administartor Password:")
                if newpass==None:
                    continue
                else:
                    q.AddAdministrator(newUser,newpass)
                    popup("New Administrator is added")
                    
                    
                
        elif event=="regdoc":
            newUser= popup_get_text("Enter the Doctor BMDC Reg Number: ")
            if newUser==None:
                continue
            elif newUser in BMDCLIST:
                popup("Already in the Doctor List")
                continue
            else:
                newpass= popup_get_text("Enter Doctor Password:")
                if newpass==None:
                    continue
                else:
                    q.AddDocID(newUser,newpass)
                    popup("Doctor Is added")