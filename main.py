import PySimpleGUI as pg
from login2 import*
import query as q



def mainCode():
    close = './close.png'
    next = './next.png'
    pg.theme("PythonPlus")
    pg.theme_background_color("#053e40")
    pg.theme_element_background_color("#053e40")
    pg.theme_element_text_color("#053e40")

    frame=[    
        [
            pg.Image('shaan3.png'),
            pg.Text("Shahan Ahmed\nDepartment of Electrical & Computer Engineer.\nMajor Computer Science & Enineering\nEmail:shahan.ahmed@northsouth.edu\n",
                    size=(50,4),justification="left",font=("monotype Corsiva",15),background_color="#053e40"),
        ], 
        [pg.Text("=====================================================================",background_color="black")],
        [
            
            pg.Image('nabila.png'),
            pg.Text("Nabila Rashid\nDepartment of Electrical & Computer Engineer.\nMajor Computer Science & Enineering\nEmail:nabila.rashid@northsouth.edu",
                    size=(50,4),justification="left",font=("monotype Corsiva",15),background_color="#053e40"),
        ],  
    ]
    layout=[
        
        [
            pg.Image('eth.png',size=(700,140)),
        ],
        [pg.Text("\n\n\n\n",background_color="#053e40")],
        [
        pg.Frame("Developed By",frame,title_color="white",size=(500,400),font=("monotype Corsiva",20)),
        pg.Text("\t",background_color="#053e40"),
        pg.ReadFormButton('', button_color="#053e40",image_filename=close, image_size=(45, 45), image_subsample=2, border_width=0,key="Close"),
        pg.ReadFormButton('', button_color="#053e40",image_filename=next, image_size=(115,45), image_subsample=2, border_width=0,key="next")
        ],
    ]

    win=pg.Window("Admin Login",layout,size=(800,550),location=(500,100))


    while True:
        event,value=win.read()
        
        if event=="Close" or event==pg.WIN_CLOSED:
            break
        elif event=="next":
            win.close()
            adminlog()
        
if q.ConnectORNOT():
    mainCode()
else:
    popup_auto_close("Database is not connected",font=("Monotype Corsiva",20))
    