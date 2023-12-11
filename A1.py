"""
Experiment No. 1 :
	In a second year computer engineering class, group A students play cricket, group B students play
	badminton and group C students play football.
	Write a python program using functions to compute following:
	a) List of students who play both cricket and badminton.
	b) List of students who play either cricket or badminton but not both.
	c) Number of students who play neither cricket nor badminton.
	d) Number of students who play cricket and football but not badminton.
(NOTE : While realising the group, duplicate entries should be avoided. Do not use SET built-in functions)
"""

def make_list(grp,stud):
    c=[]
    f=[]
    b=[]
    if grp == "a":
        for i in range(stud):
            c.append(int(input("Enter Roll: ")))
        return c
    elif grp == "b":
        for i in range(stud):
            f.append(int(input("Enter Roll: ")))
        return f
    else:
        for i in range(stud):
            b.append(int(input("Enter Roll: ")))
        return b
    
def dupli(lst):
    st=[]
    for roll in lst:
        if roll not in st:
            st.append(roll)
    return st

def c_b(cric,badm):
    c_b=[]
    for i in cric:
        if i in badm:
            c_b.append(i)
    return c_b

def CoB(cric,badm):
    CoB=[]
    for i in cric:
        if i not in badm:
            CoB.append(i)
    for i in badm:
        if i not in cric:
            CoB.append(i)
    return CoB
def f(cric,badm,footb):
    f=[]
    for i in footb:
        if i not in cric and i not in badm:
            f.append(i)
    return f

def c_f(cric,badm,footb):
    c_f=[]
    for i in cric:
        if i not in badm :
            c_f.append(i)
    for i in footb:
        if i not in badm:
            if i not in cric:
                c_f.append(i)        

    return c_f

def menu():
	print("\n--------------------MENU--------------------")
	print("1. List of students who play both cricket and badminton.")
	print("2. List of students who play either cricket or badminton but not both")
	print("3. Number of students who play neither cricket nor badminton.")
	print("4. Number of students who play cricket and football but not badminton.")
	print("5. EXIT")    

stud = int(input("ENter Number of STudents playing cricket: "))
cric = make_list("A",stud)
cric = dupli(cric)
print("Cricket Group: ",cric)

stud = int(input("ENter Number of STudents playing Football: "))
footb = make_list("B",stud)
footb = dupli(footb)
print("Football Group: ",footb)

stud = int(input("ENter Number of STudents playing badminton: "))
badm = make_list("C",stud)
badm = dupli(badm)
print("Badminton Group: ",badm)

menu()
choice=1
while(choice==1):
    ch=int(input("Enter Your Choice: "))

    if ch==1:
        print(c_b(cric,badm))
    elif ch==2:
        print(CoB(cric,badm))
    elif ch==3:
        print(f(cric,badm,footb))
    elif ch==4:
        print(c_f(cric,badm,footb))
    else:
        print("Enter Valid choice:")
    
    choice=(int(input("Do u want to continue(1/0)")))
