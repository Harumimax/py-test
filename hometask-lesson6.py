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
print(combinator(lst))

# task 5
def my_summa(arg1, arg2, *args):
    print(" ".join([arg1] + [arg2] + list(args)))

my_summa('1', '2', '3', four='4', five='5')
