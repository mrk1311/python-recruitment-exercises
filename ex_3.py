x1 = 1
y1 = 1
x2 = 8
y2 = 2


if x1 == x2 or y1 == y2:
    print("YES")
elif x1-x2 == y1-y2 or x2-x1 == y2-y1 or x1-x2 == y1-y2 or x2-x1 == y1-y2:
    print("YES")
else:
    print("NO")