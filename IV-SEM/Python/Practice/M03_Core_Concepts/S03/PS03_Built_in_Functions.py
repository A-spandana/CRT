#count even numbers(using filter())
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(len(even_numbers))
print(even_numbers)
#removing duplicates (using set())
a = [10,20,25,48,10,55,48]
print(set(a))
#sum of digits (using sum())
n = 12345
res = sum(int(digit) for digit in str(n))
print(res)

#sort words alphabetically (using sorted())
a = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(a)
print(sorted_words)
#common elements (using set())
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
res = set(list1) & set(list2)
print(tuple(res))
#