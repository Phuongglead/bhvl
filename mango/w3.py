import math
n = int(input())
# YOUR CODE HERE
a = 0
if n == 0 or n == 1:
    print("not prime")
elif n>=2:
    for i in range(2,n):
        if n%i == 0:
            a += 1
    if a>=1:
        print("not prime")
    else:
        print("prime")
        
               



        