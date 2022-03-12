f = open('tsp1.txt', 'r')
list = f.readlines()
n = int (list[0])
i = 1
data = []
while i <= n:
    temp = []
    so = 0
    for k in list[i]:
        if k != " " and k != "\n":
            so = so*10+int(k)
        else:
            temp.append(so)
            so = 0
    data.append(temp)
    i = i+1
print (data)