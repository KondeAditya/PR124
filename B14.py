mks=[]
def i_mks():
    n=int(input("Enter NO. of students: "))
    for i in range(n):
        perc=float(input("Enter percentage of roll : "))
        mks.append(perc)
    print("Marks are ",mks)

def bub_s():
    for i in range(len(mks)):
        for j in range(len(mks)-i-1):
            if mks[j]>mks[j+1]:
                mks[j],mks[j+1]=mks[j+1],mks[j]
    print("Marks sorted in ascending order using Bubble sort : ",mks)
def sel_s():
    for i in range(len(mks)):
        min_i=i
        for j in range(i+1,len(mks)):
            if mks[j]<mks[min_i]:
                min_i=j
        mks[i],mks[min_i]=mks[min_i],mks[i]
    print("Marks sorted in ascending order using Selection sort : ",mks)

def top5():
    rev=mks[::-1]
    print("Top 5 percentage: ",rev[:5])

def choose_optn():
	while True:
		print("Choose an option from the menu below:")
		print("1 -> Input marks")
		print("2 -> Selection Sorting")
		print("3 -> Bubble Sorting")
		print("4 -> Display top 5")
		print("5 -> Exit")
		optn=int(input("Choose an option (1-5):\t"))
		
		if optn==1:
			i_mks()
		elif optn==2:
			sel_s()
		elif optn==3:
			bub_s()
		elif optn==4:
			top5()
		else:
			print("\nPlease choose a valid option (1-5).\n")
			choose_optn()
choose_optn()