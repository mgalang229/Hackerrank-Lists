list1 = []
for i in range(int(input())):
    s, *d = input().split()
    d = list(map(int, d))
    if s == "print":
        print(list1)
    else:
        getattr(list1, s)(*d)

