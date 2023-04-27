#from cards.const import NumsList

def get_min_card(deck_list):
    if type(deck_list) != list:
        deck_list = deck_list.return_list()
    index_min_card = len(NumsList)
    for current_card in deck_list:
        if index_min_card >= NumsList.index(current_card.num):
            index_min_card = NumsList.index(current_card.num)
            result = current_card
    if "result" not in locals():
        result = False
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

