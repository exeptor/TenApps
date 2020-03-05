import csv
import os

try:
    import statistics
except:
    import Ten_Apps_Course.App_9_Real_Estate_Analysis.statistics_for_python2 as statistics

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
    """
    Calculate max price, min price, average price and average data for 2-bedroom home
    :param data: List of objects.
    :return: Print messages containing calculated values described above.
    """
    data.sort(key=lambda p: p.price)

    # highest home price.
    high_purchase = data[-1]
    print('The most expensive house is ${:,} with {} bedrooms and {} bathrooms.'.format(
        high_purchase.price, high_purchase.beds, high_purchase.baths))

    # lowest home price.
    low_purchase = data[0]
    print('The cheapest house is ${:,} with {} bedrooms and {} bathrooms.'.format(
        low_purchase.price, low_purchase.beds, low_purchase.baths))

    # average home price.
    prices = [
        p.price
        for p in data
    ]
    avg_price = statistics.mean(prices)
    print('The average home price is ${:,}.'.format(round(avg_price)))

    # average data for 2-bedrooms home.
    two_bed_home = [
        p
        for p in data
        if p.beds == 2
    ]

    two_bed_avg_price = statistics.mean((p.price for p in two_bed_home))
    two_bed_avg_baths = statistics.mean((p.baths for p in two_bed_home))
    two_bed_avg_sq_ft = statistics.mean((p.sq__ft for p in two_bed_home))
    print('Average 2-bedrooms home is ${:,}, {} baths and {} sq ft.'
          .format(int(two_bed_avg_price), round(two_bed_avg_baths, 1), round(two_bed_avg_sq_ft, 1)))

# todo:
#  - fix the code bellow removing the announce() method.
#  - add simple functionality to ask user if he/she wants to go over all data or aver a defined limit (eg. first 5 rows)

#     two_bed_home = (
#         p
#         for p in data
#         if announce(p, '2-bedrooms, found {}'.format(p.beds)) and p.beds == 2
#     )
#
#     homes = []
#     for h in two_bed_home:
#         if len(homes) >= 5:
#             break
#         homes.append(h)
#
#     two_bed_avg_price = statistics.mean((announce(p.price, 'price') for p in homes))
#     two_bed_avg_baths = statistics.mean((p.baths for p in homes))
#     two_bed_avg_sq_ft = statistics.mean((p.sq__ft for p in homes))
#
#     print('Average 2-bedrooms home is ${:,}, {} baths and {} sq ft.'
#           .format(int(two_bed_avg_price), round(two_bed_avg_baths, 1), round(two_bed_avg_sq_ft, 1)))
#
#
# def announce(item, msg):
#     print('Pulling item {} for {}'.format(item, msg))
#     return item


if __name__ == '__main__':
    main()
