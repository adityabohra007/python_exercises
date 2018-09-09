import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return 'A level {} {}'.format(self.level, self.name)

    def get_roll(self):
        return random.randint(1, 20) * self.level


class Dragon(Creature):
    def __init__(self, name, level, scale_thickness, is_breathing_fire):
        super().__init__(name, level)
        self.scale_thickness = scale_thickness
        self.is_breathing_fire = is_breathing_fire

    def get_roll(self):
        base_roll = super().get_roll()
        scale_modifier = self.scale_thickness // 10
        fire_modifier = 5 if self.is_breathing_fire else 1

        return base_roll * scale_modifier * fire_modifier


class SmallAnimal(Creature):
    def get_roll(self):
        return super().get_roll() // 2


class Wizard(Creature):
    def fight(self, enemy):
        player_roll = self.get_roll()
        print('The wizard roles {}'.format(player_roll))

        enemy_roll = enemy.get_roll()
        print('The {} roles {}'.format(enemy.name, enemy_roll))

        if player_roll >= enemy_roll:
            return True
        else:
            return False
