N = int(input())
a = [int(input()) for i in range(0,N)]
count = maxi = 0
for i in range(0,N):
    if(a[i] == 0):
        count = 0
    else:
        count+=1
        maxi = max(maxi,count)
print(maxi)