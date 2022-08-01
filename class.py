student=[]

class studentinfo():
    def __init__(self,name, roll, gender):
        self.name=name
        self.roll=roll
        self.gender=gender

while True:
    name=input("Enter Student name: ")
    roll=int(input("Enter Age: "))
    gender=input("Enter the gender: ")
    
    student.append(studentinfo(name,roll,gender))

    more=input("Do you want to add another (y/n)")
    if more=="n":
        break
    
    
for i in range(0,len(student)):
    print(student[i].name)
    print(student[i].roll)
    print(student[i].gender)
    