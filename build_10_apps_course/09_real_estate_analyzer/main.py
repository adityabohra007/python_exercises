import csv
import os
import statistics

from data_types import Transaction

BASE_DIR = os.path.dirname(__file__)
DATA_FILENAME = 'SacramentoRealEstateTransactions2008.csv'


def main():
    print_header()
    data_file_path = get_data_file_path()
    header, data = load_data(data_file_path)
    print_data_header(header)
    answer_questions(data)


def print_header():
    print('-----------------------------')
    print('      Real Estate App')
    print('-----------------------------')
    print()


def get_data_file_path():
    return os.path.join(BASE_DIR, 'data', DATA_FILENAME)


def load_data(data_file_path):
    print('Loading CSV real estate data ... ', end='')

    with open(data_file_path, 'r', encoding='utf-8') as file:
        header = file.readline()
        file.seek(0)
        reader = csv.DictReader(file)
        transactions = [Transaction.create_from_dict(row) for row in reader]

    print('done\n')

    return header, transactions


def print_data_header(header):
    headers = header.split(',')
    print('Header: {}'.format(', '.join(headers)))


def answer_questions(data):
    data.sort(key=lambda t: t.price)

    print('Most expensive house: {}-bed, {}-bath, house for ${:,} in {}'.format(
        data[-1].beds, data[-1].baths, int(data[-1].price), data[-1].city))

    print()

    print('Least expensive house: {}-bed, {}-bath, house for ${:,} in {}'.format(
        data[0].beds, data[0].baths, int(data[0].price), data[0].city))

    print()

    average_price = statistics.mean((t.price for t in data))
    average_beds = statistics.mean((t.beds for t in data))
    average_baths = statistics.mean((t.baths for t in data))

    print('Average house: ${:,}, {} bed, {} bath'.format(
        int(average_price), round(average_beds, 1), round(average_baths, 1)))

    print()

    average_two_bed_price = statistics.mean((t.price for t in data if t.beds == 2))
    average_two_bed_beds = statistics.mean((t.beds for t in data if t.beds == 2))
    average_two_bed_baths = statistics.mean((t.baths for t in data if t.beds == 2))

    print('Average 2-bedroom house: ${:,}, {} bed, {} bath'.format(
        int(average_two_bed_price), round(average_two_bed_beds, 1), round(average_two_bed_baths, 1)))


if __name__ == '__main__':
    main()
