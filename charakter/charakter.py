FIGHTER = {"health": 5, "attack": 3, "dodge": 1}
THIEF = {"health": 2, "attack": 3, "dodge": 4}
MAGE = {"health": 1, "attack": 5, "dodge": 4}
TYPES = {"fighter": FIGHTER, "thief": THIEF, "mage": MAGE}

class Charakter():
    def __init__(self, type):
        char_type = TYPES[type]
        self.health = char_type["health"]
        self.attack = char_type["attack"]
        self.dodge =  char_type["dodge"]

    def attac(self):

