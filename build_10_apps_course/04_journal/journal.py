import os


def load(filename):
    data = []
    filepath = get_pathname(filename)

    print('... loading journal from {} ...'.format(filepath))

    if os.path.exists(filepath):
        with open(filepath) as file:
            for line in file.readlines():
                data.append(line.rstrip())

    print('... loaded {} entries ...'.format(len(data)))

    return data


def save(filename, data):
    filepath = get_pathname(filename)

    print('... saving to {} ...'.format(filepath))

    with open(filepath, 'w') as file:
        for entry in data:
            file.write(entry + '\n')

    print('... save complete ...')


def add_entry(data, text):
    data.append(text)


def get_pathname(filename):
    filepath = os.path.join('.', 'data', filename)

    return filepath
