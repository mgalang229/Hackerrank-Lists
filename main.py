a = []
for i in range(int(input())):
    temp = [x for x in input().split()]
    if temp[0] == "insert":
        a.insert(int(temp[1]), int(temp[2]))
    elif temp[0] == "print":
        print(a)
    elif temp[0] == "remove":
        a.remove(int(temp[1]))
    elif temp[0] == "append":
        a.append(int(temp[1]))
    elif temp[0] == "sort":
        a.sort()
    elif temp[0] == "pop":
        a.pop()
    elif temp[0] == "reverse":
        a.reverse()
