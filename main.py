
f = open('tsp1.txt', 'r')
list = f.readlines()
arr = []
for i in list:
    so = 0
    for k in i:
        if (k!=" " and k!="\n"):
            so=so*10+int(k)
        else:
            arr.append(so)
            so=0
print(arr);






