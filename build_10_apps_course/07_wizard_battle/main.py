import random
import time

from actors import Creature, Dragon, SmallAnimal, Wizard


def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------')
    print('     WIZARD GAME APP')
    print('--------------------------')
    print()


def game_loop():
    player = Wizard('Gandolf', 75)

    enemies = [
        SmallAnimal('Toad', 1),
        SmallAnimal('Bat', 3),
        Creature('Tiger', 12),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 1000),
    ]

    while True and enemies:
        print()

        active_enemy = random.choice(enemies)

        print('The wizard {} sees a {}.'.format(player.name, active_enemy.name))

        cmd = input('Do you [f]ight, [r]un away or [l]ook around? ').lower().strip()

        if cmd == 'f':
            fight_result = player.fight(active_enemy)
            if fight_result:
                print('The wizard has been triumphant over {}'.format(active_enemy.name))
                enemies.remove(active_enemy)
            else:
                print('The wizard runs and hides taking time to recover...')
                time.sleep(5)
                print('The wizard returns revitalized!')
        elif cmd == 'r':
            print('The wizard {} runs away!.'.format(player.name))
        elif cmd == 'l':
            print('The wizard {} looks around and sees:'.format(player.name))

            for enemy in enemies:
                print(enemy)
        else:
            break

    if not enemies:
        print('\nWell done, you have defeated all the enemies!')
    else:
        print('\nThere are more enemies to defeat, please try next time.')


if __name__ == '__main__':
    main()
