from warrior import Warrior  # from warrior import * #imports ALL classes from warrior
import battle  # must do battle.Battle() to use Battle class from battle


def main():
    # Create 2 Warriors
    paul = Warrior("Paul", 50, 30, 10)
    sam = Warrior("Sam", 50, 30, 10)
    print(paul)
    print(sam)

    # Create Battle object
    battle1 = battle.Battle()
    print(battle1)
    # Initiate Battle
    battle1.startFight(paul, sam)


main()
