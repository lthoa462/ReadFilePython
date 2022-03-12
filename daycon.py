f = open('tsp1.txt', 'r')
list = f.readlines()
arr = []
for i in list:
    so = 0
    for k in i:
        if k != " " and k != "\n":
            so = so*10+int(k)
        else:
            arr.append(so)
            so = 0
result = 1
for i in range(len(arr)):
    f = []
    f[i] = 0
    for j in range(i):
        if arr[j] < arr[i]: f[i] = max(f[i], f[j]+1)
    result = max(result, f[i])
print(result)
