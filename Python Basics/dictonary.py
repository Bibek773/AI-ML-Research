def add():
    global count 
    
    name=input("Enter the name of Student: ")
    roll=int(input("Enter your roll no."))
    faculty=input("Enter Your Faculty")
    s={ 
        "name":name,
        "ROLL":roll,
        "faculty":faculty
    }
    student.append(s)
    print("Successfully added student")
    print(count)
    count += 1
def display():
    for i in range(count):
        print(f'Name:{student[i]["name"]} \nRoll:{student[i]["ROLL"]} \nFaculty: {student[i]["faculty"]}\n')
    
def search():
   
    a=int(input("Enter the the roll no you want to search"))
    for i in range(count):
        if a==student[i]["ROLL"]:
            print(student[i]["name"])
def update():
    w=int(input("Enter the rollno you have incorrectly entered"))
    for i in range(count):
         if w==student[i]["ROLL"]:
            while(1):
                x=input("Enter what you have incorrectly entered \n1.Name\n2.rollno\n3.faculty")
                if x==1:
                    student[i]["name"]=input("Enter correct Name\n")
                    break
                elif x==2:
                    student[i]["roll"]=int(input("Enter correct Roll\n"))
                    break
                elif x==3:
                    student[i]["roll"]=input("Enter correct Faculty\n")
                    break
                else:
                    print("Enter correct value:")
                    break
def delete():
   y=int(input("Enter the rollno you have incorrectly entered"))
   for i in range(count):
         if y==student[i]["ROLL"]:
            student.pop(i)
student=[]
count = 0
while(1):
    choice=int(input("Enter your choice\n 1. add student\n 2. display student list\n 3. search student\n 4. update \n 5. delete\n 6. exit"))
    if choice==1:
        add()
    elif choice==2:
        display()
    elif choice==3:
        search()
    elif choice==4:
        update()
    elif choice==5:
        delete
    elif choice==6:
        print("Exiting the program")
        break
    else:
        print("invalid choice")