#from cards.const import NumsList

def get_min_card(deck_list):
    if type(deck_list) != list:
        deck_list = deck_list.return_list()
    index_min_card = len(NumsList)
    result = False
    for current_card in deck_list:
        if index_min_card >= NumsList.index(current_card.num):
            index_min_card = NumsList.index(current_card.num)
            result = current_card
    return result

def get_index_max_card(list_of_card):
    cards_indexes = []
    for current_card in list_of_card:
        cards_indexes.append(NumsList.index(current_card.num))
    max_card_index = max(cards_indexes)
    result = False if cards_indexes.count(max_card_index) > 1 else cards_indexes.index(max_card_index)
    return result


def calc(str):
    list_str = list(str)
    new_list = []
    for current in list_str:
        if current == "+" or current == "-" or current == "/" or current == "*":
            new_list.append(current)
        else:
            new_list.append(int(current))
    print(new_list)
    for i in range(len(new_list)):
        if new_list[i] == "*" or new_list[i] == "/":
            if new_list[i] == "*":
                num = new_list[i-1] * new_list[i+1]
                new_list[i-1] = num
                new_list[i+1] = "none"
            else:
                num = new_list[i-1] / new_list[i+1]
                new_list[i-1] = int(num)
                new_list[i+1] = "none"
    print(new_list)
    result = new_list[0]
    for i in range(len(new_list)):
        if new_list[i] == "+":
            result = result + new_list[i+1]
        elif new_list[i] == "-":
            result = result - new_list[i + 1]
        else:
            pass
    return result

def unique_words(str):
    str_list = str.split()
    sings = ["?", ".", ",", "!", "-"]
    str_list = [current_word[:-1].lower() if current_word[-1] in sings else current_word.lower() for current_word in str_list]
    print(str_list)
    result = []
    for current_word in str_list:
        if result.count(current_word) == 0:
            result.append(current_word)
    return result

print(unique_words("Python is great, isn't it? is Yes- yes blat"))

def filter_capitalized_words(list):
    result = []
    for current_str in list:
        if current_str[0] == current_str[0].upper():
            result.append(current_str)
    return result


