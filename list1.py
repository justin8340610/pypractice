a = [3,"1",4,2]
#1
print(a[2])
#2
print(a[-1])
#3
a.append(5)
print(a)
#4
a[1]=1
print(a)
#5
b = a[2:4]
print(b)
#6
c = a[2:]
print(c)
#7
d = a[1:-1]
print(d)
#8
e = a[2:-1]
print(e)
#9
f = []
for el in a:
    f.append(el)
f[0]=99
print(a,f,sep="\n")
#10
g=[10,20]
a=a+g
print(a)
#11
a[2:3]=[7,8,9]
print(a)