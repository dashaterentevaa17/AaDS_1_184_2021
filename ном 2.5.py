#5
a={'tiger', 0, 'leopard', 'elephant', 2, 7}
b={1, 'camel', 'elephant', 2, 9}
c=[]
for i in a:
    for j in b:
        if i==j :
            c.append(i)

print(c)

print(a.intersection(b))

# Написать функцию, принимающую два параметра: 1-ый параметр -> множество,
# 2-ой -> список и возвращающую значение False, если хотя бы один из элементов
# списка не содержится в множестве, иначе возвращающая True.