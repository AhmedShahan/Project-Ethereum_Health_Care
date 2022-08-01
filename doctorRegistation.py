from PySimpleGUI import *
import query as q
import ValidationWithAdd as valid

def predict_text(input, lista):
    pattern = re.compile('.*' + input + '.*')
    return [w for w in lista if re.match(pattern, w)]
   
def mainCode():
    theme("DarkGreen4")
    theme_button_color("black")
    theme_input_background_color("white")
    theme_input_text_color("#001D3C")
    colpersonal=[
        [Text("Name",size=(15,1),font=("Times & new roman","12","italic","bold")),InputText("Enter Name Here",font=("times & new roman",12,"italic"),size=(30,1),justification="center")],
        [Text("Date of Birth",size=(15,1),font=("Times & new roman","12","italic","bold")),
        CalendarButton("Date of Birth",target="depart",format="%d-%m-%Y",size=(14,1)),
        Input(key="depart",size=(20,1),default_text="01-03-2022"),
        ],
        [Text("Gender",size=(15,1),font=("Times & new roman","12","italic","bold")),Radio("Male","g-1",font=("Times & new roman","12","italic")),Radio("Female","g-1",font=("Times & new roman","12","italic"))],
        [Text("NID Number",size=(15,1),font=("Times & new roman","12","italic","bold")),InputText("Enter NID Here",font=("times & new roman",12,"italic"),size=(30,1),justification="center")],
        [Text("Passport Number",size=(15,1),font=("Times & new roman","12","italic","bold")),InputText("Enter Passport Number Here",font=("times & new roman",12,"italic"),size=(30,1),justification="center")],
        [Text("Mobile Number",size=(15,1),font=("Times & new roman","12","italic","bold")),InputText("Enter Mobile Number Here",font=("times & new roman",12,"italic"),size=(30,1),justification="center")],
        [Text("Email Address",size=(15,1),font=("Times & new roman","12","italic","bold")),InputText("Enter Email address Here",font=("times & new roman",12,"italic"),size=(30,1),justification="center")],
        [Text("Present Address",size=(15,1),font=("Times & new roman","12","italic","bold")),Multiline("Enter Email address Here",font=("times & new roman",12,"italic"),size=(30,3),justification="center")],
        [Text("Parmanent Address",size=(15,1),font=("Times & new roman","12","italic","bold")),Multiline("Enter Email address Here",font=("times & new roman",12,"italic"),size=(30,3),justification="center")],
        
        
        [Text('Blood Group', font=('Monotype Corsiva', 15), justification='left')], 
        [Radio('O (+Ve)', 'blood', size=(12, 1)), Radio('O (-Ve)', 'blood', default=True, size=(12, 1))],  
        [Radio('A (+Ve)', 'blood', size=(12, 1)), Radio('A (-Ve)', 'blood', size=(12, 1))],      
        [Radio('B (+Ve)', 'blood', size=(12, 1)), Radio('B (-Ve)', 'blood', size=(12, 1))],      
        [Radio('AB (+Ve)', 'blood', size=(12, 1)), Radio('AB (-Ve)', 'blood', size=(12, 1))],
    ]    
    specialist=q.retriveSpecialist()
    outsp = list(itertools.chain(*specialist))
    degree = q.retriveDegree()
    outdegree = list(itertools.chain(*degree))
    
    colmedicalHis=[
        [Text("BMDC Registration No",size=(17,1),font=("Times & new roman","12","italic","bold")),InputText("BMDC Reg",font=("times & new roman",12,"italic"),size=(10,1),justification="center")],
        
        [Text('Specialist IN',size=(10,1),font=("Times & new roman","12","italic","bold")), Text('', key='_OUTPUT_'),In(key='_INPUT_',size=(15,1))],
        [Text("\t"*2),Listbox(specialist,  size=(15,5), key='_COMBO_',select_mode="multiple"),Button("+ ADD +",key="add1"),Button("+ Remove +",key="remove")],
        
        
        
        [Text("Medical College Details",font=("Monotype Corsiva",17,"bold"),text_color="Yellow")],
        [Text("Select Your Degree",font=("Times & new roman","12","italic","bold"),size=(17,1)),Combo(values=outdegree,key="degreeCombo",size=(15,1)),Button("+ ADD +",key="add2")],
        [Text("Name of The Medical",size=(17,1),font=("Times & new roman","12","italic","bold")),InputText(key="medicalName",size=(30,1))],
        [Text("Medical Location",size=(17,1),font=("Times & new roman","12","italic","bold")),InputText(key="medicalLoc",size=(30,1))],
        [Text('Year of Passing',size=(17,1),font=("Times & new roman","12","italic","bold")),InputText(key="passyear",size=(15,1))],
        [Text("\t"*2),Button("ADD ANOTHER DEGREE",key="addanother")],
        
        [Text("Consultation Location",font=("Monotype Corsiva",17,"bold"),text_color="Yellow")],
        [Text("Name of The Medical / Digonostic Center",size=(33,1),font=("Times & new roman","12","italic","bold"))],
        [InputText(key="medicalName",size=(56,1))],
        
        [Text("Location",size=(10,1),font=("Times & new roman","12","italic","bold")),
        InputText(key="medicalName",size=(40,1))],
        [Text("Zip Code",size=(10,1),font=("Times & new roman","12","italic","bold")),InputText(key="zip",size=(40,1))],
    ]

    
    frame1=[
        [
            Column(colpersonal)
        ],
    ]
    frame2=[
        [
            Column(colmedicalHis)
        ],
        [
            Text("\t"*2),
            ReadFormButton('', button_color="#044343",image_filename="submit.png", image_size=(150, 50), image_subsample=2, border_width=0,key="submit"),
            
        ]
    ]
    col1=[
        [Image("doc22.png")],
    ]
    col2=[
        [
            Frame("Personal Information",frame1,font=("Monotype Corsiva",17),title_color="yellow"),
            Frame("Medical History",frame2,font=("Monotype Corsiva",17),title_color="yellow"),
        ],
        
    ]
    
    addDegreeArray=[]
    headings=['Degree','Medical','Year of Passing']
    
    
    
    
    layout=[
        [Image("eth444.png",size=(480,120)),Text("Fill Up the Doctor Details",font=("Jokerman",40,"underline"),size=(20,1),justification="c")],
        [Column(col2,element_justification="c"),Column(col1,element_justification="l")],
    ]

    doc = Window('Doctor Login', size=(1200,750),location=(100,10),return_keyboard_events=True).Layout(layout)
    
    combo_elem = doc.Element('_COMBO_')
    combo_elem2 = doc.Element('degreeCombo')
    
    while True:             # Event Loop
        event, values = doc.Read()
        values
        if event == WIN_CLOSED:
            break
        
########################################################################        
## This is the section of Specialist
########################################################################
        #Adding Specialist in the list box
        elif event=="add1":
            add=popup_get_text("Enter :")
            if add==None:
                continue
            elif add in outsp:
                popup_auto_close("Already in the list")
            else:
                outsp.append(add)
                doc["_COMBO_"].update(outsp)
                q.addSpecialist(add)
                popup_auto_close("Added")
        
        # Removing Specialist From the list box        
        elif event=="remove":
            rem=popup_get_text("Enter to remove")
            if rem==None:
                continue
            elif rem not in outsp:
                popup_auto_close("Degree is not in the list")
            else:
                q.removeSpecialist(rem)
                outsp.remove(rem)
                doc["_COMBO_"].update(outsp)
                
 ###################################################################################
            # This section works multiple Medical College Degree Detaills
 ###################################################################################        
        elif event=="addanother":
            DegreeArray=[
                values["degreeCombo"],
                values["medicalName"],
                values["passyear"],
            ]
            
            addDegreeArray.append(DegreeArray)
            popup_auto_close("Added")
            valid.create(addDegreeArray,headings)
#######################################################################################
        elif event == "submit":
            for i in range(2000):
                popup_animated("android.gif",no_titlebar=True,background_color="black",location=(600,100),time_between_frames=60)
            popup_animated(None)
            Popup("Successfully Created Your Profile",font=("Monotype Corsiva",20),title="Unauthorized")
            
##########################################################################################
            # This is the section of Medical Degree Combo Box
##########################################################################################       
        #This is adding medical degree
        elif event== "add2":
            addDegree=popup_get_text("Enter :")
            if addDegree==None:
                continue
            elif addDegree in outdegree:
                popup_auto_close("Already in the list")
            else:
                outdegree.append(addDegree)
                doc['degreeCombo'].update(values=outdegree)
                q.addDegree(addDegree)
                popup_auto_close("Added")              


        # autofill the SPecialist
        in_val = values['_INPUT_']
        prediction_list = predict_text(str(in_val), outsp)
        combo_elem.Update(values=prediction_list)
    # valid.velidation(values)
    doc.Close()

