n = int(input())

arr = list(map(int, input().split()))
freq ={}

for x in arr:
    if x in freq:
        freq[x] +=1
    else:
        freq[x] =1

remove=0

for num in freq:
    cnt = freq[num]
    if cnt<num:
        remove +=cnt
    else:
        remove +=(cnt - num)

print(remove)