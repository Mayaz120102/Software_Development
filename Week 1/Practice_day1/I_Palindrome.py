n = input().strip()

reverse = str(int(n[::-1]))

print(reverse)

if reverse == n:
    print("YES")
else:
    print("NO")