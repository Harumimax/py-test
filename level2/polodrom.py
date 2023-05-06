"""Написать программу, которая считывает строку, проверяет, является ли она палиндромом,
и выводит сообщение о результате проверки.
 При этом, использовать функции reverse и рекурсию."""

"""Функция reversed() возвращает обратный итератор, то есть возвращает итератор, 
который перебирает элементы оригинала в обратном порядке.
Функция reversed() не создает копию и не изменяет оригинал последовательности.
"""
def check_palindrome(word):
    #print(word)
    #print(word[0]," ", word[-1])
    if len(word) <= 1:
        return True
    elif len(word) > 3 and word[0] == word[-1]:
        return check_palindrome(word[1:-1])
    elif len(word) <= 3 and word[0] == word[-1]:
        return True
    else:
        return False

print(check_palindrome(""))

def test_check_palindrome():
    assert check_palindrome("racecar") == True
    assert check_palindrome("hello") == False
    assert check_palindrome("level") == True
    assert check_palindrome("") == True
    assert check_palindrome("a") == True
    assert check_palindrome("ab") == False
    print("All test_check_palindrome passed!")

test_check_palindrome()

print(check_palindrome("ab"))
print(check_palindrome("racecar"))
print(check_palindrome("hello"))
print(check_palindrome("level"))