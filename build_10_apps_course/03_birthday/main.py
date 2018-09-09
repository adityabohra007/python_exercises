import datetime


def print_header():
    print('--------------------------')
    print('      BIRTHDAY APP')
    print('--------------------------')
    print()


def get_birthday_info():
    year = int(input('What year were you born [YYYY]? '))
    month = int(input('What month were you born [MM]? '))
    day = int(input('What day were you born [DD]? '))
    print()

    print('Looks like you were born on {:02}/{:02}/{}.'.format(day, month, year))

    return datetime.date(year, month, day)


def compute_days_between_dates(birthday, today):
    date = datetime.date(birthday.year, today.month, today.day)
    dt = birthday - date

    return dt.days


def print_result(days):
    if days < 0:
        print('Looks like your birthday were {} days ago\nHope it was really fun!'.format(-days))
    elif days > 0:
        print("Looks like your birthday is in {} days.\nHope you're looking forward to it!".format(days))
    else:
        print('Your birthday is today. Happy birthday!')


def main():
    print_header()
    birthday = get_birthday_info()
    result = compute_days_between_dates(birthday, datetime.date.today())
    print_result(result)


if __name__ == '__main__':
    main()
