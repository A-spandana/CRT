import array
arr = array.array('i', [])
print(arr,type(arr))
arr.append(10)
arr.append(20)
print(arr)
arr.append(12)
'''
list:
1. use []vto create a list
2. list is mutable
3. list allows duplicate values
4. list is heterogenous
5. list is indexed

li = [12,25.4,6+5j,"hello",12,25.4]
print(li,type(li))
print(li[3])
print(li[3:6:1])
print(li[::-1])
print(len(li))
li.append(100)
print(li)
'''
n = input("enter a number:")
print(len(n))
