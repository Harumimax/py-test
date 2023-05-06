import random

# task 2
def combinator(list):
    result = []
    result.append((list[0], list[1], list[2]))
    result.append((list[0], list[2], list[1]))
    result.append((list[1], list[0], list[2]))
    result.append((list[1], list[2], list[0]))
    result.append((list[2], list[0], list[1]))
    result.append((list[2], list[1], list[0]))
    return result

lst = [11, 22, 33]
#print(combinator(lst))

# task 5 вариант 1
def my_summa(*nums):
    result = 0
    for num in nums:
        result += num
    return result

print(my_summa(1, 2, 3))

# task 5 вариант 2
def my_summa(*nums):
    return sum(nums)

print(my_summa(3, 4, 3))

# task 4 [word.strip() for word in words.split(",")]
random_list = random.sample([i for i in range(100)], random.randint(1, 10))
print(random_list)