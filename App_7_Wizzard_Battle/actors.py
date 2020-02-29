import random


class Creature:
    def __init__(self, name, level):
        self.level = level
        self.name = name

    def __repr__(self):
        """
        Change the way the object is represented.
        :return: Reformatted look of the object of type str.
        """
        return 'Creature: {} of level {}'.format(self.name, self.level)

    def get_defensive_role(self):
        """
        Build the temporary power of a creature based on random number (1 to 10) and the its stored level.
        :return: Calculated value of type int.
        """
        return random.randint(1, 10) * self.level


class SmallAnimal(Creature):
    # parent initializer is unchanged

    def get_defensive_role(self):
        """
        Override the base get_defensive_role() method by dividing the base_roll by 2.
        :return: Calculated value of type int.
        """
        base_roll = super().get_defensive_role()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

    def get_defensive_role(self):
        """
        Override the base get_defensive_role() method by adding modifiers for scaliness and breath_fire
        :return: Calculated value of type int.
        """
        base_roll = super().get_defensive_role()
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10
        return base_roll * fire_modifier * scale_modifier


class Wizard(Creature):
    # parent initializer is unchanged

    def attack(self, creature):
        """
        Compares the calculated defense powers of both objects and bring boolean value (Victory=True, Defeat=False).
        :param creature: Object of type Creature.
        :return: True or False.
        """
        print('The wizard {} attacks {}!'. format(self.name, creature.name))

        my_roll = self.get_defensive_role()
        creature_roll = creature.get_defensive_role()

        print('You roll {} ...'.format(my_roll))
        print('{} roll {} ...'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('The wizard triumphed over {}'.format(creature.name))
            return True
        else:
            print('The wizard has been defeated!!!')
            return False
