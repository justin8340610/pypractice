num = range(5,0,-1)
print(num)

num2 = list(range(5,0,-1))
print(num2)

a = [1,2,3]
total = 0
for el in a:
    total+=el
total2 = sum(a)
print(total,total2,sep="\n")

b = range(5,0,-1)
# b = (5,4,3,2,1)
total3 = sum(b)
print(total3)

strA = "Stone"
strA = list(strA)
strA[0] = "Y"
print(strA)
print(''.join(strA)) #把東西用join前的東西連起來(這裡是list to string)
