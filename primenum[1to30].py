n=int(input())
for n in range(1,31):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)
