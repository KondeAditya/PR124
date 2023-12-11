def quick_S(arr):
    if len(arr) <= 1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x < pivot]
    middle=[x for x in arr if x == pivot]
    right=[x for x in arr if x > pivot]
    
    return quick_S(left)+middle+quick_S(right)
def top5(arr):
    tp5=quick_S(arr1)
    top_scores = tp5[-5:][::-1]
    return top_scores

arr1=[]
n=int(input("Enter n of ELe: "))
for i in range(n):
    num=float(input(f"Enter {i+1} ele: "))
    arr1.append(num)

print(f"Original array is: {arr1}")
print(f"Sorted array is: {quick_S(arr1)}")
print(f"TOP 5Scores are : {top5(arr1)}")
      
