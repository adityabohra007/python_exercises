import collections
import os

SearchResult = collections.namedtuple('SearchResult', 'file, line_no, text')


def main():
    print_header()
    search_dir = get_search_dir()
    search_text = get_search_text()
    print_results(search_dir, search_text)


def print_header():
    print('-------------------------------')
    print('        File Search App')
    print('-------------------------------')
    print()


def get_search_dir():
    search_dir = input('What directory do you want to search:\n')
    return search_dir


def get_search_text():
    search_text = input('What string are you looking for: ')
    print()
    return search_text


def validate_input(search_dir, search_text):
    if not search_dir:
        print('\nYou need to provide directory to be searched')
        return False
    if not os.path.exists(search_dir) or not os.path.isdir(search_dir):
        print("\nSorry there is no '{}' directory".format(search_dir))
        return False

    if not search_text:
        print('\nYou need to provide a text to search for')
        return False

    print('Searching {} for {}'.format(search_dir, search_text))

    return True


def search_directory(search_dir, search_text):
    full_path = os.path.abspath(search_dir)

    for item in os.listdir(full_path):
        full_item = os.path.join(full_path, item)
        if os.path.isdir(full_item):
            yield from search_directory(full_item, search_text)
        else:
            yield from search_file(full_item, search_text)


def search_file(search_file, search_text):
    try:
        with open(search_file, 'r', encoding='utf-8') as file:
            i = 0
            for line in file:
                i += 1
                if line.lower().find(search_text) >= 0:
                    file_temp = search_file.split('/')
                    yield SearchResult(file=file_temp[-1], line_no=i, text=line)
    except UnicodeDecodeError:
        return None


def print_results(search_dir, search_text):
    if validate_input(search_dir, search_text):
        n = 0
        for item in search_directory(search_dir, search_text):
            n += 1
            print('{}, line {} >> {}'.format(item.file, item.line_no, item.text.strip()))

        print('{} total matches'.format(n))
        print('End of search')


if __name__ == '__main__':
    main()
