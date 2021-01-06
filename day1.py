#largest continuous sum

def sum(l,n):
    sum = 0
    for i in range(0,N):
        if(sum<sum+l[i]):
            sum+=l[i]
        else:
            break
    print(sum)

N = int(input())
a = [int(input()) for i in range(0,N)]
sum(a,N)
