a,b = map(int, input().split())

found = False

for i in range(a, b+1):
    s = str(i)

    ok = True
    for ch in s:
        if ch != '4' and ch != '7':
            ok = False
            break
    if ok:
        print(i, end=' ')
        found = True

if not found:
    print(-1)