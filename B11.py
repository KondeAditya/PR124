def int_roll():
    lst=[]
    n=int(input("ENter The number of roll: "))
    for i in range(n):
        roll=int(input("ENter the Roll numbers: "))
        lst.append(roll)
    return lst

def printR(lst):
    for i in lst:
        print(i,end=" ")
    print("\n")

def lin_search(lst,srch):
    pos=0
    for i in lst:
        pos +=1
        if i==srch:
            print(f"Roll {srch} found at position {pos}\n")
        else:
            print("Not Found")
    return "\n"

def senti_s(lst,srch):
    lst1=lst
    last=lst[-1]
    lst1[-1]=srch
    pos=0
    if last==srch:
        print(f"Roll {srch} found at position {len(lst)}\n")
    else:
        for i in lst1[:-1]:
            pos+=1
            if i==srch:
                print(f"Roll {srch} found at position {pos}\n")
            else:
                print("not FOund")
        return "\n"

def bin_srch(arr,x,low,high):
    lst=arr
    while low <= high:
        mid=low+(high-low)//2
        if lst[mid]==x:
            print(f"Roll {x} at pos {mid+1}")
            break
        elif lst[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return "\n"

def fib_srch(lst,srch):
    size=len(lst)
    strt=-1
    f0,f1,f2=0,1,1
    while f2<size:
        f0=f1
        f1=f2
        f2=f1+f0
    
    while f2>1:
        index=min(strt+f0,size-1)
        if lst[index]<srch:
            f2=f1
            f1=f0
            f0=f2-f1
            strt=index
        elif lst[index]>srch:
            f2=f0
            f1=f1-f0
            f0=f2-f1
        else:
            return f"Found at {index+1}"
    if f1 and (lst[size-1]==srch):
        return f"Found at {size}"
    return "\n"

roll=[]
def menu():
    fff=0
    while(fff==0):
        print("\n1.Sorted\n2.Unsorted\n3.Exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            menu2()
        elif ch==2:
            menu1()
        else:
            fff=1
            exit()
    
def menu1():
    f=0
    while(f==0):
        print("\n1.Input\n2.Display\n3.Linear\n4.Sentinel\n5.Exit\n")
        ch1=int(input("Enter your choice: "))
        if ch1==1:
            roll=int_roll()
        elif ch1==2:
            printR(roll)
        elif ch1==3:
            srch=int(input("Enter roll to search: "))
            print(lin_search(roll,srch))
        elif ch1==4:
            srch=int(input("Enter roll to search: "))
            print(senti_s(roll,srch))
        else:
            f=1
            menu()

def menu2():
    fl=0
    while(fl==0):
        print("\n1.Input\n2.Display\n3.Binary\n4.Fibonacci\n5.Exit\n")
        ch2=int(input("Enter your choice: "))
        if ch2==1:
            roll=int_roll()
        elif ch2==2:
            printR(roll)
        elif ch2==3:
            srch=int(input("Enter roll to search: "))
            print(bin_srch(roll,srch,0,len(roll)-1))
        elif ch2==4:
            srch=int(input("Enter roll to search: "))
            print(fib_srch(roll,srch))
        else:
            fl=1
            menu()

menu()