from games.cards.deckofcards import DeckofCards
from games.cards.deckofcards import Hand
from cards.const import NumsList, Names
from games.cards.utils import get_index_max_card
from games.cards.utils import get_winner_of_round
from games.cards.utils import check_players_have_cards

deck = DeckofCards()
deck.make_deck()
deck.shuffle()

number_of_players = int(input("Введите количество игроков (2, 3, 4, 6)"))
list_of_players = []
for i in range(number_of_players): # создаем список игроков
    list_of_players.append(Hand(f"Алкаш {Names[i]}"))

while deck.get_deck_len() > 0: # раздаём все карты всем игрокам
    for current_player in list_of_players:
        if deck.get_deck_len() > 0:
            current_player.take_card(deck.get_card(deck.get_deck_len() - 1))
        else:
            break

print("---------------------- началась игра в ПЬЯНИЦУ ----------------------")
iter = 1
while len(list_of_players) > 1:
    cards_on_table = Hand() # сюда складываются карты, которые участвуют в розыгрыше
    someone_win_round = False
    print(f"---------------------- Номер круга: ", iter, "----------------------")
    players_in_round = {}
    for index in range(number_of_players):
        players_in_round[list_of_players[index].name] = index
    while someone_win_round != True:
        if check_players_have_cards(list_of_players, players_in_round) == True:
            list_of_cards_in_round = []
            for name, index in players_in_round.items():
                current_player_card = list_of_players[index].get_card(0)
                list_of_cards_in_round.append({"card": current_player_card, "name": list_of_players[index].name})
                cards_on_table.take_card(current_player_card)
                print("%s положил карту"%(list_of_players[index].name), end=" ")
                current_player_card.print_card()

            winner_of_round_index = get_winner_of_round(list_of_cards_in_round) # Победитель раудна найден?
            if winner_of_round_index == True:
                someone_win_round = True
                player_who_win_round = get_index_max_card(list_of_cards_in_round)
                for current_card in cards_on_table.return_list():
                    list_of_players[players_in_round[player_who_win_round]].take_card(current_card)
            else:
                names = get_index_max_card(list_of_cards_in_round)
                iterable_players_in_round = players_in_round.copy()
                for name, index in iterable_players_in_round.items():
                    if name not in names:
                        del players_in_round[name]
        else:
            iterable_players_in_round = players_in_round.copy()
            for name, index in iterable_players_in_round.items():
                if list_of_players[index].get_deck_len() == 0:
                    del players_in_round[name]
            if len(players_in_round) == 1:
                for current_card in cards_on_table.return_list():
                    values = list(players_in_round.values())
                    list_of_players[values[0]].take_card(current_card)
                break
            elif len(players_in_round) == 0:
                break

    for current_player in list_of_players: # перемешать карты в руке, чтобы игра не зацикливалась
        current_player.shuffle()

    iterable_list_of_players = list_of_players.copy()
    for current_player in iterable_list_of_players: #убрать из списка игроков выйгравших игроков
        if current_player.is_win() == True:
            list_of_players.remove(current_player)
    number_of_players = len(list_of_players)

    print("Текущее количество карт на руках игроков:")
    for current_player in list_of_players:
        print(f"%i количество карт - это игрок %s"%(current_player.get_deck_len(), current_player.name))
    iter += 1

print("--------------- Победил в игре Пьяница: %s ---------------"%list_of_players[0].name)