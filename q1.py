n=int(input("Enter number of integers you want to have in the list: "))
numbers=[]
numbers=list(map(int,input("Enter integers seperated by a single space: ").split()))
if len(numbers)!=n:
    print("Number of integers entered in the list is not equal to the number of integers wanted")
else:    
    high=0 #to store index of current highest element
    low=0 #to store index of current lowest element
    total=0 #to store sum of all integers
    evesum=0 #to store number of even numbers
    oddsum=0 #to store number of odd numbers
    revnumbers=[] #to store the numbers in reverse
    for i in range(0,n):
        if numbers[i]>numbers[high]:
            high=i #for subpart 1
        if numbers[i]<numbers[low]:
            low=i #for subpart 2
        total+=numbers[i] #for subpart 3
        if (numbers[i]%2)==0:
            evesum+=1
        else:
            oddsum+=1
        revnumbers.append(numbers[n-i-1])

    print("Largest element: ",numbers[high])
    print("Smallest element: ",numbers[low])
    print("Total sum of elements: ",total)
    print("Number of even elements: ",evesum)
    print("Number of odd elements: ",oddsum)
    print("Reversed list:",end=' ')
    for i in range(0,n):
        print(revnumbers[i],end= ' ')