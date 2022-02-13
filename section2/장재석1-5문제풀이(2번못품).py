#K번째 약수
import sys
# sys.stdin=open("input.txt", "r")
# n, k=map(int, input().split())
n= 5
k= 3
sum = 0
for i in range(1,n+1):
    if n%i == 0:
        sum += 1
        if sum == k:
            print(k)
            break
if sum != k:
    print(-1)
    
#K번째 큰수
sys.stdin=open("input.txt", "r")
n, k=map(int, input().split())
a=list(map(int, input().split()))

a.sort(reverse=True)
count, sum = 0, 0
for i in a:
    count += 1
    sum += i
    if count == k:
        print(sum)
        break
        
        
        
#대표값
# sys.stdin=open("input.txt", "r")
# n=int(input())
# a=list(map(int, input().split()))
average=sum(a)/n
average=average+0.5
average=int(average)
difference = 55555
count = 0

for i in a:
    count += 1
    k = abs(average - i)
    if difference > k:
        difference = k
        output = [i]
    elif difference == k:
        output.append(k)
print(output)




# sys.stdin=open("input.txt", "r")
# n, m=map(int, input().split())
n, m = 6,5
count=[0]*(n+m+3)
max=0
for i in range(1, n+1):
    for j in range(1, m+1):
        count[i+j]=count[i+j]+1

for i in range(n+m+1):
    if count[i]>max:
        max=count[i]
    
for i in range(n+m+1):
    if count[i]==max:
        print(i, end=' ')
