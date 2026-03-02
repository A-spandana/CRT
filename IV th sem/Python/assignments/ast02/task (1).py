def even_odd(n: int) -> str:
   if n % 2 != 0:
      return "weird"
   elif n % 2 == 0 and 2 <= n <= 5:
      return "not weird"
   elif n % 2 == 0 and 6 <= n <= 20:
      return "weird"
   elif n % 2 == 0 and n > 20:
      return "not weird"


if __name__ == '__main__':
    n = int(input())
    print(even_odd(n))
