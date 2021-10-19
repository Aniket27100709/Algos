a = input().split(" ")
w = float(a[0])
i = float(a[1])
if w <= i-0.5 and w % 5 == 0:
    output = i-w-0.5
    print("{:.2f}".format(output))
else:
    print("{:.2f}".format(i))
