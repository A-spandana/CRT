'''li = [1,2,3,4,5]
res = []
for i in li:
    if i % 2 == 0:
        res.append(i)
print(res)

li1 = ['a','b','c']
res = ""
for ch in li1:
    res += ch
print(res)
print("".join(li1))'''
'''intermediate patterns
1.pyramid
n = 4
output:
    *
   * *
  * * * 
 * * * *
  
n = int(input())
for i in range(1,n+1):
    print(" "*(n - i) + "* "*i)'''
    
'''2.inverted pyramid
n = 4
output :
 * * * *
  * * *
   * *
    * 
n = int(input())
for i in range(n,0,-1):
    print(" "*(n - i) + " * "*i)'''

'''3.diamond
n = 4 
output:
       *
      * *
     * * *
    * * * *
     * * *
      * *
       *
n = int(input())
for i in range(1,n+1):
    print(" "*(n - i) + "* "*i)
for i in range(n-1,0,-1):
    print(" "*(n -i) + "* "*i)'''
    
'''4. 1
    1  2
   1  2  3
 1  2  3  4
n = int(input())
for i in range(1, n+1):
    print(" "*(n - i)+ " ".join([str(j) for j in range(1, i + 1)]))

for i in range(1, n+1):
    print(" "*(n - i)+" ".join([str(i) for j in range(1, i + 1)]))'''

'''A
   B C
   D E F
   G H I J
   
n = int(input())
val = 65
for i in range(n):
    for j in range(i + 1):
        print(chr(val),end =" ")
        val += 1
    print()'''


   



