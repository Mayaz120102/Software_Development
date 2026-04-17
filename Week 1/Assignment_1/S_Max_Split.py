s = input().strip()
cnt =0
bal =0
cur =[]
new_str = []

for ch in s:
    cur.append(ch)
    
    if ch == 'R':
        bal += 1
    else:
        bal -=1
    
    if bal ==0:
        new_str.append(cur)
        cur = []
        cnt += 1

print(cnt)

for s in new_str:
    for ch in s:
        print(ch, end='')
    print()
