NumsList = ['6', '7', '8', '9', '10', 'Валет', "Дама", "Король", "Туз"]
MastList = ["Пики", "Крести", "Буби", "Черви"]

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

#trump = "Черви"

#deck = [["7", "Черви"], ["Дама", "Черви"], ["7", "Пики"], ["Король", "Черви"], ["6", "Черви"], ["9", "Пики"], ["Король", "Пики"]]

#card = ["8", "Пики"]




