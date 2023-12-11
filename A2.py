"""
Experiment Number 2 :
Write a python program to store marks scored in subject "Fundamentals of Data Structure" by N
students in the class. Write functions to compute following:
						1. The average score of the class.
						2. Highest score and lowest score of the class.
						3. Count of students who were absent for the test.
						4. Display marks with the highest frequency.
"""

def avr(lst):
    t_mks=0
    count=0
    for i in lst:
        if i !="A":
            t_mks+=i
            count+=1
    
    avg=t_mks/count
    return avg

def high_low(lst):
    max=0
    min=100
    for i in lst:
        if i != "A":
            if i > max:
                max=i
    for i in lst:
        if i != "A":
            if i<min:
                min=i
    roll1=lst.index(max)+1
    roll2=lst.index(min)+1
    print("highest: ",max,"ROLL: ",roll1,"Lowest: ",min,"ROLL: ",roll2)

def abst(lst):
    count=0
    for i in lst:
        if i == "A":
            count=count+1
    return count

def freq(lst):
    freq_d={}
    m_i=None
    m_f=0

    for i in lst:
        if i in freq_d:
            freq_d[i] += 1
        else:
            freq_d[i] = 1

    for i,frequ in freq_d.items():
        print(f"{i}:{frequ}")

    for i, frequ in freq_d.items():
        if frequ > m_f:
            m_i=i
            m_f=frequ
    print(f"Highest frequency: {m_i}:{m_f}")

def C_L():
    students=[]
    stud=int(input("ENter n of students: "))
    for i in range(stud):
        mks=input(f"Enter MKS OF Roll no.{i+1}: ")
        if mks!="A":
            students.append(int(mks))
        else:
            students.append(mks)
    return students

def menu():
    print("\n<--------------------------- MENU --------------------------->")
    print("1. Avg score of class.\n2. Highest and lowest score of class.\n3. Number of absent students.\n4.Score Frequency")

mksL=C_L()
ch1=1
while ch1==1:
    menu()
    ch=int(input("Enter your choice: "))
    if ch==1:
        print(avr(mksL))
    elif ch==2:
        print(high_low(mksL))
    elif ch==3:
        print(abst(mksL))
    elif ch==4:
        print(freq(mksL))
    else:
        ch1=int(input("Continue?(1/0)"))
