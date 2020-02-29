import random
import time
from Ten_Apps_Course.App_7_Wizzard_Battle.actors import Creature, Wizard, SmallAnimal, Dragon

def main():
    print_header()
    game_loop()


def print_header():
    """
    Prints the standard (course convention) header with the name of the application.
    :return: Prints the header in a standardized format.
    """
    print('---------------------------------')
    print('       WIZARD BATTLE')
    print('---------------------------------')


def game_loop():
    """
    Runs over the game logic until wizard wins or player exit forcefully.
    :return: Display the game flow.
    """
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 1000)
    ]

    # print(creatures)

    hero = Wizard('Gandolf', 750)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appear from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns healed!")
        elif cmd == 'r':
            print('The wizard has become unsure of his power and runs away!!!')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'
                  .format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print("OK, exiting game... bye!")
            break

        if not creatures:
            print("You've defeated all the creatures, well done!!!")
            break

        print()


if __name__ == '__main__':
    main()
