import random
from cards.const import NumsList, MastList

class Card():
    def __init__(self, num, mast="none"):
        self.num = num
        self.mast = mast

    def print_card(self):
        str = self.num + "_" + self.mast
        print(str)

    def is_trump(self, trump):
        if self.mast == trump:
            return True
        else:
            return False

class DeckofCards(): ############################################### DECK
    def __init__(self):
        self.deck = []

    def make_deck(self):
        for current_num in NumsList:
            if current_num == "Джокер":
                pass
            else:
                for current_mast in MastList:
                    current_cart = Card(current_num, current_mast)
                    self.deck.append(current_cart)
        #self.deck.append(Card("Джокер"))
        #self.deck.append(Card("Джокер"))

    def shuffle(self):
        random.shuffle(self.deck)

    def get_card(self, index):
        if index < len(self.deck):
            if len(self.deck) > 0:
                result = self.deck[index]
                self.deck.remove(self.deck[index])
            else:
                result = "Карты кончились"
        else:
            result = "Такого индекса нет в колоде"
        return result

    def get_deck_len(self):
        return len(self.deck)

    def return_list(self):
        return self.deck

class Hand(DeckofCards): ######################################  HAND
    def __init__(self, name="none"):
        super().__init__()
        self.deck = []
        self.name = name
    def take_card(self, card):
        self.deck.append(card)

    def show_hand(self):
        for current_card in self.deck:
            current_card.print_card()

    def get_all_trumps_from_hand(self, trump):
        trumps = []
        for current_card in self.deck:
            if current_card.mast == trump:
                trumps.append(current_card)
        return trumps

    def find_min_card_for_first(self, trump):
        index_min_card = len(NumsList)
        result = self.deck[0]

        for current_card in self.deck:
            i = NumsList.index(current_card.num)
            if i <= index_min_card and current_card.mast != trump:
                index_min_card = i
                result = current_card

        if index_min_card == len(NumsList):
            for current_card in self.deck:
                i = NumsList.index(current_card.num)
                if i <= index_min_card:
                    index_min_card = i
                    result = current_card
        self.deck.remove(result)
        return result

    def fight_back(self, trump, card):
        trumps = self.get_all_trumps_from_hand(trump)
        result = False
        if card.is_trump(trump) == False:
            index_card = NumsList.index(card.num)
            can_fight_list = []
            for current_card in self.deck:
                if NumsList.index(current_card.num) > index_card and current_card.mast == card.mast:
                    can_fight_list.append([NumsList.index(current_card.num), current_card])

            if len(can_fight_list) != 0:
                min_fight_card = len(NumsList)
                for current_card in can_fight_list:
                    if min_fight_card >= current_card[0]:
                        min_fight_card = current_card[0]
                        result = current_card[1]
            else:
                min_trupm_card = len(NumsList)
                for current_card in trumps:
                    if min_trupm_card >= NumsList.index(current_card.num):
                        min_trupm_card = NumsList.index(current_card.num)
                        result = current_card
        else:
            for current_card in trumps:
                if NumsList.index(card.num) < NumsList.index(current_card.num):
                    result = current_card
                    break

        if result != False:
            self.deck.remove(result)
        return result

    def throw_card(self, trump, cards_on_table):
        if cards_on_table.get_deck_len() == 0:
            index_min_card = len(NumsList)
            result = self.deck[0]

            for current_card in self.deck:
                i = NumsList.index(current_card.num)
                if i <= index_min_card and current_card.mast != trump:
                    index_min_card = i
                    result = current_card

            if index_min_card == len(NumsList):
                for current_card in self.deck:
                    i = NumsList.index(current_card.num)
                    if i <= index_min_card:
                        index_min_card = i
                        result = current_card
            self.deck.remove(result)
            return result

        else:
            hand = self.return_list()
            trumps_hand = self.get_all_trumps_from_hand(trump)
            hand_without_trump_list = [x for x in hand if x not in trumps_hand]
            cards_on_table_list = cards_on_table.return_list()
            throw_list = []
            for current_card_table in cards_on_table_list:
                for current_card_hand in hand_without_trump_list:
                    if current_card_table.num == current_card_hand.num:
                        throw_list.append(current_card_hand)
            if len(throw_list) != 0:
                index_min_card = len(throw_list)
                result = throw_list[0]
                for current_card in throw_list:
                    i = NumsList.index(current_card.num)
                    if i <= index_min_card:
                        index_min_card = i
                        result = current_card
                self.deck.remove(result)
            else:
                result = False
            #for c in throw_list:
            #    c.print_card()
            return result

    def is_win(self):
        if self.get_deck_len() == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    deck = DeckofCards()
    deck.shuffle()
    random_cart = deck.get_card(0)

    for iter in range(deck.get_deck_len()):
        print(iter+1)
        random_cart = deck.get_card(0)
        random_cart.print_card()
        print(deck.get_deck_len())
        print("\n")
