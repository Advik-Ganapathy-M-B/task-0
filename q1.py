n=int(input("Enter number of integers you want to have in the list: "))
numbers=[]
numbers=list(map(int,input("Enter integers seperated by a single space: ").split()))
if len(numbers)!=n:
    print("Number of integers entered in the list is not equal to the number of integers wanted")
else:    
    high=0 #to store index of current highest element
    low=0 #to store index of current lowest element
    total=0 #to store sum of all integers
    for i in range(0,n):
        if numbers[i]>numbers[high]:
            high=i #for subpart 1
        if numbers[i]<numbers[low]:
            low=i #for subpart 2
        total+=numbers[i] #for subpart 3

    print("Largest element: ",numbers[high])
    print("Smallest element: ",numbers[low])
    print("Total sum of elements:",total)
