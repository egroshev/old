# warriors have names, health, max attack, max block
# warrior capabilities include random attacking and blocking
# attack random() 0.0 to 1.0 + 0.5 * maxAttack
# block will use random()
import random


class Warrior:

    # @property, setter, and getter, lets us use functions as variables
    # thus, we can do warriorObj.health = 12, and it will set warrior Health
    # but through a function health to a private variable _health

    # ##PROPERTY DEFINITIONS CAN ALL BE COMMENTED OUT IF NEEDED** *
    @property
    def name(self):
        # can check parameters and set default statements here
        return self._name

    @name.setter
    def name(self, value):
        # HOW CAN I MAKE SURE NAME ISN'T CHANGED AGAIN?
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

    @health.deleter
    def health(self):
        del self._health

    @property
    def attkMax(self):
        return self._attkMax

    @attkMax.setter
    def attkMax(self, value):
        self._attkMax = value

    @attkMax.deleter
    def attkMax(self):
        del self._attkMax

    @property
    def blockMax(self):
        return self._blockMax

    @blockMax.setter
    def blockMax(self, value):
        self._blockMax = value

    @blockMax.deleter
    def blockMax(self):
        del self._blockMax

    # ##PROPERTY DEFINITIONS CAN ALL BE COMMENTED OUT IF NEEDED** *

    def __init__(self, name="warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def __str__(self):
        # Used if you ever simply "print" the object i.e. print(warriorInstance)
        return "I am a {}. My name is {}. My stats are health: {}, Max attack: {}, Max block: {}.".format(
            type(self).__name__, self.name, self.health, self.attkMax, self.blockMax
        )

    def attack(self):
        # Randomly calculate the attack amount
        # random() returns a value from 0.0 to 1.0
        attkAmt = self.attkMax * (random.random() + 0.5)

        return attkAmt

    def block(self):

        # Randomly calculate how much of the attack was blocked
        blockAmt = self.blockMax * (random.random() + 0.5)

        return blockAmt


# The Battle class will have the capability to loop until 1 Warrior dies
# The Warriors will each get a turn to attack each turn
