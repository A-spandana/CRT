'''
sample input: 1234
sample output: 4

sample input: 455786
sample output: 6

sample input: 45
sample output: 2
'''
'''num = int(input("enter a number:"))
count = 0
while num > 0:
    count += 1
    num = num//10
print(count)

print(len(str(num)))     sample input: 1234
sample output: 10
'''
'''s = 0 
temp = num                 
while num > 0:
    s += (num % 10)
    num = num//10
print(s)

print(sum(map(int,str(temp))))'''
'''sample input : 12345
sample output : 2 3
input: 5588
output:2 2

n = int(input())
even = 0
odd = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:             
        even += 1
    else:                
        odd += 1
    n //= 10
print(even,odd)

input: 546
output:6
input: 783
output: 9
'''
n = int(input())
while n > 9:
    n = sum(map(int,str(n)))
print(n)



