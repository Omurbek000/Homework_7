# Тапшырма:
# 1. Берилген сан канча цифрадан турарын табат ошону табуу.


# def count_digits(number):

#     return len(str(number))


# if __name__ == "__main__":
#     number = int(input("Сан киргизиңиз: "))
#     print(f"Сан {number}")
#     print(f"цифрадан турат {count_digits(number)}")


# Берилген сандын цифраларынын суммасын табуу 
# sum_of_digits(5324) -> 14

# def sum_of_digits(number):
#     total = 0
#     while number > 0:
#         digit = number % 10
#         total += digit
#         number //= 10
#     return total
  
# if __name__ == "__main__":
#     number = int(input("Сан киргизиңиз: "))
#     print(f"Сан {number}")
#     print(f"цифралардын суммасы {sum_of_digits(number)}")