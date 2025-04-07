def sum_n(n):
    total = 0
    for num in n:
       total += num
    return total

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 86]
result = sum_n(numbers)

print(sum_n(numbers))
