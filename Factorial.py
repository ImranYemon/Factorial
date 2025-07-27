'''
Factorial (0)= 1 
Factorial (1)= 1 
Factorial (2)= 2*1 
Factorial (3)= 3*2*1 
Factorial (4)= 4*3*2*1 
Factorial (5)= 5*4*3*2*1 
Factorial (n)= n*(n-1)*(n-2)*.........2*1
Factorial (n)= n*Factorial(n-1)

'''

def Factorial(n):
    if (n==1 or n==0):
        return 1
    return n*Factorial(n-1)

n= int(input("enter your number : "))
print(f"the factorial of this number is : {Factorial(n)}")


