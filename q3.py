def is_prime(n):
    for i in range(2,n):
        if (n%i)==0:
            return False
            break
    else: #in for else statements the else statement is executed if the for loop is terminated by a break statement not by naturally finishing its iterations
        return True
N=int(input("Enter the number to which you want to find prime numbers: "))
for i in range(2,(N+1)):
    if is_prime(i):
        print(i, end=' ')