#1
t = (1, 2, 3)
l = list(t)
l.remove(2)
t = tuple(l)

#2
last_list = ['a', 'b', 'c', 'd']
last_list[-1] = "last"

#3
slist = ['I', 'am', 1, 'list', 'of', 5, 'strings']
oslist = []
for stri in slist:
    if isinstance(stri,str):
        oslist.append(stri)

#4
matrix = []
for i in range(3):
    t_mat = ['x' if x == i else "_" for x in range(3)]
    matrix.append(t_mat)
