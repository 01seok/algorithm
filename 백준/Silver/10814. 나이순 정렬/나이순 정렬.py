n=int(input())
arr=[]
for _ in range(n):
    a,b=input().split()
    arr.append((int(a),b))
arr.sort(key=lambda x:x[0])
for a,b in arr:
    print(a,b)