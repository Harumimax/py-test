from cards.deckofcards import DeckofCards
from cards.deckofcards import Hand
from cards.utils import get_min_card

# Условия игры: колода карт 36, без джокеров
# подкидывать козырь нельзя
# отбой 6 карт
# подкидываем минимальную карту
# первый ход с самой маленькой карты

NumsList = ['6', '7', '8', '9', '10', 'Валет', "Дама", "Король", "Туз"]
MastList = ["Пики", "Крести", "Буби", "Черви"]
start_card_in_hand = 6 # количество карт на руки
num_of_throw = 6 # количество подкидываний

deck = DeckofCards()
deck.make_deck()
deck.shuffle()

player1 = Hand("Гарри Поттер")
player2 = Hand("Винни Пух")

for _ in range(start_card_in_hand): # раздаём карты, берем верхние карты
    player1.take_card(deck.get_card(deck.get_deck_len() - 1))
    player2.take_card(deck.get_card(deck.get_deck_len() - 1))

trump = deck.return_list()
trump = trump[deck.get_deck_len() - 1].mast # определяем козырь
print(trump, "- this is trump")

cards_on_table = Hand() # сюда складываются карты, которые участвуют в розыгрыше

print("-------------- Lest start --------------")

# определяем, кто первый ходит - смотрим минимальный козырь в руке
min_player1_trump = get_min_card(player1.get_all_trumps_from_hand(trump))
min_player2_trump = get_min_card(player2.get_all_trumps_from_hand(trump))


if min_player1_trump != False and min_player2_trump == False: # когда у одного игрока нет козырей вообще
    first, second = [player1, player2]
elif min_player1_trump == False and min_player2_trump != False:
    first, second = [player2, player1]
elif NumsList.index(min_player1_trump.num) < NumsList.index(min_player2_trump.num):
    first, second = [player1, player2]
else:
    first, second = [player2, player1]

print("This is first player hand - ", first.name)
first.show_hand()
print("This is second player hand - ", second.name)
second.show_hand()
print("--------------------------------")





while (first.is_win() == False) or (second.is_win() == False):

    iter = 1
    second_fought_back = True # флаг того, что отбивающейся игрок смог отбиться

    if num_of_throw > second.get_deck_len(): # это случай, когда в конце колоды на руках отбивающегося карт меньше 6
        num_of_throw = second.get_deck_len()
    while second_fought_back == True and iter <= num_of_throw:
        if first.is_win() or second.is_win():
            break

        print(f"Круг подбрасывания карт #", iter)

        attack_card = first.throw_card(trump, cards_on_table)
        if attack_card:
            cards_on_table.take_card(attack_card)
            print(first.name, " ходит картой:", end=' ')
            attack_card.print_card()

        else:
            print(first.name, " нечего подбросить")
            break

        defend_card = second.fight_back(trump, attack_card)
        if defend_card:
            cards_on_table.take_card(defend_card)
            print(second.name, " бьётся картой:", end=' ')
            defend_card.print_card()
        else:
            second_fought_back = False
            print(second.name, " берет карты")
            for current_card in cards_on_table.return_list():
                second.take_card(current_card)

        print("--------------------------------")
        iter += 1

    # пополняем карты в руке первый и второй игрок
    if (first.get_deck_len() < start_card_in_hand) and (deck.get_deck_len() != 0):
        if (start_card_in_hand - first.get_deck_len()) <= deck.get_deck_len():
            for _ in range(start_card_in_hand - first.get_deck_len()):
                first.take_card(deck.get_card(deck.get_deck_len() - 1))
        else:
            for _ in range(deck.get_deck_len()): # если осталось карт в колоде меньше, чем нужно игроку
                first.take_card(deck.get_card(deck.get_deck_len() - 1))
    if (second.get_deck_len() < start_card_in_hand) and (deck.get_deck_len() != 0):
        if (start_card_in_hand - second.get_deck_len()) <= deck.get_deck_len():
            for _ in range(start_card_in_hand - second.get_deck_len()):
                second.take_card(deck.get_card(deck.get_deck_len() - 1))
        else:
            for _ in range(deck.get_deck_len()):
                second.take_card(deck.get_card(deck.get_deck_len() - 1))


    print("--------------------------------")
    print(deck.get_deck_len(), "- Это столько осталось карт в колоде")
    print(first.get_deck_len(), "- Это столько карт на руке первого игрока")
    print(second.get_deck_len(), "- Это столько карт осталось на руке второго игрока")

    cards_on_table = Hand() # сбрасываем все карты, которые были в розыгрыше
    num_of_throw = 6
    if second_fought_back == True: # меняем игрока, который ходит, если отбился
        first, second = [second, first]
    else:
        first, second = [first, second]

    if first.is_win() or second.is_win():
        break
    print("--------------------------------")



if first.is_win() == True and second.is_win() == True:
    print("Это НИЧЬЯ!!!!!")
else:
    if first.is_win() == True:
        print("Игрок %s - победил!!!!!!!!!!!!"%(first.name))

    if second.is_win() == True:
        print("Игрок %s - победил!!!!!!!!!!!!"%(second.name))