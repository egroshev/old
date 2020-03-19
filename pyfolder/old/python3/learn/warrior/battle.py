# The Battle class will have the capability to loop until 1 Warrior dies
# The Warriors will each get a turn to attack each turn
import math


class Battle:
    def __str__(self):
        # Used if you ever simply "print" the object i.e. print(battleInstance)
        return "{} takes 2 given warriors and makes them fight to the death".format(
            type(self).__name__
        )

    def startFight(self, warrior1, warrior2):

        # Continue looping until a Warrior dies switching back and
        # forth as the Warriors attack each other
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    # A function will receive each Warrior that will attack the other
    # Have the attack and block amounts be integers to make the results clean
    # Output the results of the fight as it goes
    # If a Warrior dies return that result to end the looping in the
    # above function

    # Make this method static because we don't need to use self
    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()

        warriorBBlockAmt = warriorB.block()

        if warriorBBlockAmt >= warriorAAttkAmt:
            warriorBBlockAmt = warriorAAttkAmt

        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)

        warriorB.health = warriorB.health - damage2WarriorB

        print(
            "{} attacks {} and deals {} damage".format(
                warriorA.name, warriorB.name, damage2WarriorB
            )
        )

        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print(
                "{} has Died and {} is Victorious".format(warriorB.name, warriorA.name)
            )

            return "Game Over"
        else:
            return "Fight Again"
