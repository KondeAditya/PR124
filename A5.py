str1=input("Enter String: ")
occur2=str1.split()
index1=[]

for i in occur2:
    if i not in index1:
        index1.append(i)
    else:
        continue

def l_word():
    currm=0
    gm=0
    lst=[]
    for i in str1:
        if (i!=" "):
            currm=currm+1
            lst.append(i)
        else:
            if(currm>gm):
                gm=currm
                temp=lst
            currm=0
            lst=[]
    print("Longest word: ","".join(temp)," of length: ",gm)

def palin():
    if(str1==str1[::-1]):
        print("The string is palindrome")
    else:
        print("The string is not palindrome")

def cfreq():
    occur1=input("ENter the charcter to find the number of occurance: ")
    for i in str1:
        max1=0
        for j in range(0,len(str1)):
            if(str1[j]!=" " and str1[j]==occur1):
                max1=max1+1
            else:
                continue
    print("the letter ",occur1," is occurred ",max1," times.")

def i_sub():
    substr=input("ENter the substring: ")
    for i in range(len(str1)-len(substr)+1):
        if str1[i:i+len(substr)]==substr:
            print(substr," is present at ",i)
            break
        else:
            print("Substring not present.")

def o_wrd():
    for i in index1:
        max=0
        for j in occur2:
            if(i==j):
                max=max+1
            else:
                continue
        print(i, "is repeated ",max," times.")

flag=0
while flag==0:
    print("1. Display word with longest word: \n")
    print("2. The occurence of word in the string is: \n")
    print("3. Check whether is string is palindrome or not: \n")
    print("4. Display index of first appearance of the substring: \n")
    print("5. Occurrence of each word in the given string: \n")
    print("6. Exit")
    ch=int(input("ENter Your CHoice: "))

    if ch==1:
        print(l_word())
    elif ch==2:
        print(cfreq())
    elif ch==3:
        print(palin())
    elif ch==4:
        print(i_sub())
    elif ch==5:
        print(o_wrd())
    elif ch==6:
        flag=1
        exit()
        