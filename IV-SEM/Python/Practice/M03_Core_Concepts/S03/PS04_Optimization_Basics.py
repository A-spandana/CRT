a = [10,20,30,40,50]
target = 30
for i in range(len(a)):
    if a[i] == target:
        print("Ele found")

a = [10,20,30,40,50]
if 30 in a:
    print("Ele found")

#sum of ele in list
a = [10,20,30,40,50]
s = 0
for i in range(len(a)):
    s += a[i]
print(s)

a = [10,20,30,40,50]
print(sum(a))

a = [2,7,11,15]
target = 9
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == target:
            print( i,j) 

a = [2,7,11,15]
target = 9
d = {}
for i in range(len(a)):
    Res = target - a[i]
    if Res in d:
        print(d[Res], i)
    d[a[Res]] = i   
        