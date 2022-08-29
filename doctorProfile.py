from PySimpleGUI import *
import query as q
import ValidationWithAdd as valid
import doctor as d

def predict_text(input, lista):
    pattern = re.compile('.*' + input + '.*')
    return [w for w in lista if re.match(pattern, w)]
## All the images
backimg="static/images/back2.png"
docimg="static/images/doc.png"
doc22img="static/images/doc22.png"
ethimg="static/images/eth444.png"
mygif="static/images/my1.gif"
submitimg="static/images/submit.png"

    # Updating from query






def mainCode():
    ActiveId=d.Active[0]
    
#================Retrive and Show in the Input Box ===============
    DoctorInfo=q.RetrivDoctorInfo(ActiveId)
    DoctorInfoList=list(itertools.chain(*DoctorInfo))
    print(DoctorInfoList)
    nameee=DoctorInfoList[0]
    dateOf=DoctorInfoList[1]
   
   
   
    '''
    gender=DoctorInfoList[2],
    male=False
    fem=False
    if gender=="Male":
        male=True
    if gender==('Female',) or gender=="Female":
        fem=True
    '''
    Nid=DoctorInfoList[3]
    Passport=DoctorInfoList[4]
    Mobile=DoctorInfoList[5]
    Email=DoctorInfoList[6]
    PreAdd=DoctorInfoList[7]
    PermanAdd=DoctorInfoList[8]
    #bgroup=DoctorInfoList[9]
    
    theme("DarkGreen4")
    theme_button_color("black")
    theme_input_background_color("white")
    theme_input_text_color("#001D3C")
    colpersonal=[
        [Text("Name", size=(15,1),font=("Times & new roman","12","italic","bold")),InputText(default_text=nameee,key="name",font=("times & new roman",12,"italic"),size=(30,1),justification="center")],
        [Text("Date of Birth",size=(15,1),font=("Times & new roman","12","italic","bold")),
        CalendarButton("Date of Birth",target="DateOfBirth",format="%Y-%m-%d",size=(14,1)),
        Input(default_text=dateOf,key="DateOfBirth",size=(20,1)),
        ],
        [Text("Gender",size=(15,1),font=("Times & new roman","12","italic","bold")),Radio("Male","g-1",font=("Times & new roman","12","italic")),Radio("Female","g-1",font=("Times & new roman","12","italic"))],
        [Text("NID Number",size=(15,1),font=("Times & new roman","12","italic","bold")),InputText(key="nid",default_text=Nid,font=("times & new roman",12,"italic"),size=(30,1),justification="center")],
        [Text("Passport Number",size=(15,1),font=("Times & new roman","12","italic","bold")),InputText(key="passport",default_text=Passport,font=("times & new roman",12,"italic"),size=(30,1),justification="center")],
        [Text("Mobile Number",size=(15,1),font=("Times & new roman","12","italic","bold")),InputText(key="mobile",default_text=Mobile,font=("times & new roman",12,"italic"),size=(30,1),justification="center")],
        [Text("Email Address",size=(15,1),font=("Times & new roman","12","italic","bold")),InputText(key="email",default_text=Email,font=("times & new roman",12,"italic"),size=(30,1),justification="center")],
        [Text("Present Address",size=(15,1),font=("Times & new roman","12","italic","bold")),Multiline(key="present",default_text=PreAdd,font=("times & new roman",12,"italic"),size=(30,3),justification="center")],
        [Text("Parmanent Address",size=(15,1),font=("Times & new roman","12","italic","bold")),Multiline(key="parmanent",default_text=PermanAdd,font=("times & new roman",12,"italic"),size=(30,3),justification="center")],
        
        
        [Text('Blood Group', font=('Monotype Corsiva', 15), justification='left')], 
        [Radio('O (+Ve)', 'blood',size=(12, 1)), Radio('O (-Ve)', 'blood',size=(12, 1))],  
        [Radio('A (+Ve)', 'blood', size=(12, 1)), Radio('A (-Ve)', 'blood', size=(12, 1))],      
        [Radio('B (+Ve)', 'blood', size=(12, 1)), Radio('B (-Ve)', 'blood', size=(12, 1))],      
        [Radio('AB (+Ve)', 'blood', size=(12, 1)), Radio('AB (-Ve)', 'blood', size=(12, 1))],
    ]    
    specialist=q.retriveSpecialist()
    outsp = list(itertools.chain(*specialist))
    degree = q.retriveDegree()
    outdegree = list(itertools.chain(*degree))
    
    colmedicalHis=[
        [Text("Last Medical College Details",font=("Monotype Corsiva",17,"bold"),text_color="Yellow")],
        [Text("Select Your Degree",font=("Times & new roman","12","italic","bold"),size=(17,1)),Combo(values=outdegree,key="degreeCombo",size=(15,1)),Button("+ ADD +",key="add2")],
        [Text("Name of The Medical",size=(17,1),font=("Times & new roman","12","italic","bold")),InputText(size=(30,1))],
        [Text("Medical Location",size=(17,1),font=("Times & new roman","12","italic","bold")),InputText(size=(30,1))],
        [Text('Year of Passing',size=(17,1),font=("Times & new roman","12","italic","bold")),InputText(size=(15,1))],
        
        [Text("Consultation Location",font=("Monotype Corsiva",17,"bold"),text_color="Yellow")],
        [Text("Name of The Medical / Digonostic Center",size=(33,1),font=("Times & new roman","12","italic","bold"))],
        [InputText(size=(56,1))],
        
        [Text("Location",size=(10,1),font=("Times & new roman","12","italic","bold")),
        InputText(size=(40,1))],
        [Text("Zip Code",size=(10,1),font=("Times & new roman","12","italic","bold")),InputText(size=(40,1))],
        [Text('Specialist IN',size=(10,1),font=("Times & new roman","12","italic","bold")), Text('', key='_OUTPUT_'),In(key='_INPUT_',size=(15,1))],
        [Text("\t"*2),Listbox(specialist,size=(15,5), key='_COMBO_',select_mode="multiple"),Button("+ ADD +",key="add1"),Button("+ Remove +",key="remove")],
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
            ReadFormButton('', button_color="#044343",image_filename=backimg, image_size=(150, 50), image_subsample=2, border_width=0,key="back"),
            ReadFormButton('', button_color="#044343",image_filename=submitimg, image_size=(150, 50), image_subsample=2, border_width=0,key="submit"),
            
        ]
    ]
    col1=[
        [Image(doc22img)],
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
        [Image(ethimg,size=(480,120)),Text("Fill Up the Doctor Details",font=("Jokerman",40,"underline"),size=(20,1),justification="c")],
        [Column(col2,element_justification="c"),Column(col1,element_justification="l")],
    ]

    doc = Window('Doctor Registration Form', size=(1200,750),location=(100,10),return_keyboard_events=True).Layout(layout)
    
    combo_elem = doc.Element('_COMBO_')
    
    while True:             # Event Loop
        event, values = doc.Read()
        if event == WIN_CLOSED:
            break
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
                
        elif event=="remove":
            rem=popup_get_text("Enter degree to remove")
            if rem==None:
                continue
            elif rem not in outsp:
                popup_auto_close("Degree is not in the list")
            else:
                #rem in outsp
                outsp.remove(rem)
                doc["_COMBO_"].update(outsp)
                q.removeSpecialist(rem)
         
        elif event=="addanother":
            DegreeArray=[
                values["degreeCombo"],
                values["medicalName"],
                values["passyear"],
            ]
            
            addDegreeArray.append(DegreeArray)
            popup_auto_close("Added")
            valid.create(addDegreeArray,headings)
#==================================================================================================================
                                ##SUBMIT SECTION
#===============================================================================================================
        elif event == "submit":
            result= valid.checkValidationDoctor(values)
            if result[0]:
                for i in range(1000):
                    popup_animated(mygif,no_titlebar=True,background_color="black",location=(600,100),time_between_frames=60)
                popup_animated(None)
                
                Popup("Successfully Created Your Profile",font=("Monotype Corsiva",20),title="Unauthorized")                
                q.UpdateDocPersonalInfo(values,ActiveId)
                q.DeleteSpecialistList(ActiveId)
                q.DocSpecialist(values,ActiveId)
                #q.DocMedicalHis(values,ActiveId)
            else:
                for i in range(1000):
                    popup_animated(mygif,no_titlebar=True,background_color="black",location=(600,100),time_between_frames=25)
                popup_animated(None)
                pop=result[1]
                popup_ok(pop,background_color="black",font=("Times & New Roman",15,"italic"))
                
                
#===============================================================================================
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

        elif event=="back":
            res=popup_ok_cancel("Your All the Inserted Data will Be Removed")
            if res=="OK":
                d.Active=[]
                print(d.Active)
                doc.close()
                d.doctor()
        
        
        
        # autofill the SPecialist
        in_val = values['_INPUT_']
        prediction_list = predict_text(str(in_val), outsp)
        combo_elem.Update(values=prediction_list)
    
        #===================================================

    doc.Close()
    