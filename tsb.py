import array as arr
from sys import maxsize
from itertools import permutations



# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s, V):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)
    return min_path

def readfile():
    f = open('tsp1.txt', 'r')
    list = f.readlines()
    n = int(list[0])
    i = 1
    data = []
    while i <= n:
        temp = []
        so = 0
        for k in list[i]:
            if k != " " and k != "\n":
                so = so * 10 + int(k)
            else:
                temp.append(so)
                so = 0
        data.append(temp)
        i = i + 1
    return data

if __name__ == "__main__":
    # matrix representation of graph
    graph = readfile()
    s = 0
    print(travellingSalesmanProblem(graph, s, 20))
















