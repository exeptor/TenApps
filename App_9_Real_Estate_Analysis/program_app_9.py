import csv
import os

from Ten_Apps_Course.App_9_Real_Estate_Analysis.data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    """
    Prints the standard (course convention) header with the name of the application.
    :return: Prints the header in a standardized format.
    """
    print('---------------------------------------------')
    print('       REAL ESTATE DATA MINING APP')
    print('---------------------------------------------')
    print('')


def get_data_file():
    """
    Build the full path to the target data file.
    :return: File path string.
    """
    base_folder = os.path.dirname(__file__)

    # Use abspath because join of '__file__' and the other two parameters brings a mixed path (i.e. ../../..\..\..).
    return os.path.abspath(os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv'))


def load_file(filename):
    """
    Transforms the data in the target file to a list of objects.
    :param filename: Full file path of the target data file.
    :return: List of objects of class Purchase.
    """
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases


def query_data(data):
    data.sort(key=lambda p: p.price)

    high_purchase = data[-1]
    print('The most expensive house is ${:,} with {} bedrooms and {} bathrooms.'.format(
        high_purchase.price, high_purchase.beds, high_purchase.baths))

    low_purchase = data[0]
    print('The cheapest house is ${:,} with {} bedrooms and {} bathrooms.'.format(
        low_purchase.price, low_purchase.beds, low_purchase.baths))


if __name__ == '__main__':
    main()
