n = int(input())
arr = list(map(int, input().split()))

def count(x):
    cnt =0
    while x%2==0:
        x = x//2
        cnt +=1
    return cnt

res = min(count(x) for x in arr)
print(res)
