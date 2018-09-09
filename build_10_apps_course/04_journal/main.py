import journal


FILENAME = 'default.jrn'


def main():
    print_header()
    main_loop()


def print_header():
    print('----------------------')
    print('     JOURNAL APP')
    print('----------------------')
    print()


def main_loop():
    data = journal.load(FILENAME)

    cmd = 1

    while cmd and cmd != 'x':
        cmd = input('What do you want to do? [L]ist, [A]dd, or E[x]it? ').lower().strip()

        if cmd == 'l':
            list_entries(data)
        elif cmd == 'a':
            add_entry(data)
        elif cmd and cmd != 'x':
            print("Sorry I don't understand '{}' command".format(cmd))

    journal.save(FILENAME, data)


def list_entries(data):
    print('Your {} journal entries'.format(len(data)))

    for index, entry in enumerate(reversed(data)):
        print('{}. {}'.format(index + 1, entry))


def add_entry(data):
    text = input('Enter your journal entry:\n')
    journal.add_entry(data, text)


if __name__ == '__main__':
    main()
