def list(n):
    list = []
    for i in range(1,n+1):
        if i%2 == 1:
            list = [1,*list]
        elif i%2 == 0:
            list = [0,*list]
    return(list)

n = int(input())
for k in range(1,n+1):
    for a in list(k):
        print(a,end='')
    print()