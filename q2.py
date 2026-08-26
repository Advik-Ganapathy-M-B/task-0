original=list(map(int,input("Enter the integers seperated by a single space: ").split()))
def process_list(numbers):
    result=numbers.copy() #making copy of original list
    for ele in result:
        if ele<0: #removing all negatives
            result.remove(ele)
    result.append(0) #appending 0
    result.sort() #sorting the list in ascending order
    return(result) #returning the modified list
result=process_list(original)
print("Original: ", original)
print("Result: ",result)


