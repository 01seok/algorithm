n=list(map(int,input().split()))
print(sum(i*i for i in n)%10)