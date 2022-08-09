from PySimpleGUI import * 
layout =[ 
    
[Text("Welcome to Paitent Form", font=('Arial', 16), size=(500,2), justification= ("center"))],
[Text("Name", size=(15,1)), Input( size=(30,3), background_color= "White")],
[Text("Present Address", size=(15,1)), Input( size=(30,3), background_color= "White")],
[Text("Gender", size=(15,1)),Radio('Male', 'group_id'), Radio('Female', 'group_id')],
[Text("Date of Birth", size=(15,1)), Input( size=(30,3), background_color= "White")],
[Text("Age", size=(15,1)), Input( size=(30,3), background_color= "White")],
[Text("Email",size=(15,1)), Input( size=(30,3), background_color= "White")],
[Text("Phone Number", size=(15,1)), Input( size=(30,3), background_color= "White")]

]


Window("Paitent Registration Form", layout, size=(700, 500) ).read()
