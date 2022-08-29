from PySimpleGUI import *
import query as q

specialist=q.retriveSpecialist()
outsp = list(itertools.chain(*specialist))


theme("PythonPlus")
theme_button_color("Black")
ethimg="static/images/eth444.png"

def predict_text(input, lista):
    pattern = re.compile('.*' + input + '.*')
    return [w for w in lista if re.match(pattern, w)]

col1=[
    [Text("Search Your Doctor",font=("Jokerman",30,"underline"),size=(40,1),justification="c")],
    [Text('Specialist IN',size=(10,1),font=("Times & new roman","12","italic","bold")), Text('', key='_OUTPUT_'),In(key='_INPUT_',size=(15,1))],
    [Text("\t"*2),Listbox(specialist,size=(15,5), key='_COMBO_',select_mode="single",background_color="White",text_color="Black")], 
]
col2=[
    [Text("Select Gender If You Want")],
    [Radio("Male","G1"),Radio("Female","G1"),Radio("None","G1",default=True)]
]

lay=[
    [Text("\t"),Image(ethimg)],
    [Column(col1)],
    [Column(col2)],
    [Text("\t"*3),Button("Submit",key="submit")]
]

win=Window("Search Your Doctor",layout=lay,size=(700,500))

combo_elem = win.Element('_COMBO_')
while True:             # Event Loop
    event,values = win.Read()
    if event == WIN_CLOSED:
        break
    elif event=="submit":
        if values["_COMBO_"]==[]:
            popup("Please Select a Specialist")
        else:
            DocList=q.SearchDoctor(values)
            onnokichu = list(itertools.chain(*DocList))

            Printlist="Your Doctor List is \n"
            length=len(DocList)
            for i in range (0,length):
                Printlist=Printlist+onnokichu[i]+"\n"
            popup(Printlist,font=("monotype Corsiva",20))
        
    
    
    

    # autofill the SPecialist
    in_val = values['_INPUT_']
    prediction_list = predict_text(str(in_val), outsp)
    combo_elem.Update(values=prediction_list)

