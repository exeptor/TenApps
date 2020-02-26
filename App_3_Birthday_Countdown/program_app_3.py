import datetime

def print_header():
    """
    :return: Print the header of the program
    """
    print('------------------------------------')
    print('       BIRTHDAY COUNTDOWN')
    print('------------------------------------')
    print()


def get_birthday_from_user():
    """
    :return: Formatted birth date object of type date, based on the three inputs for year, month and day
    """

    print('What is your birthday?')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.date(year, month, day)    # returns object of type date
    return birthday


def compute_days_between_dates(original_date, target_date):
    """
    :param original_date: Date object coming from get_birthday_from_user() function
    :param target_date: Date object which wil be given in the main(), normally the current day
    :return: Calculated days between transformed original_date (year replaced with target_date year) and target_date
    """

    # remove year factor by replacing the original year with the target year and only counting the days in the
    # current year
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)

    dt = this_year - target_date    # both objects are of type date and so 'dt' is also the same type
    return dt.days                  # we can use the methods of datetime module because 'dt' is of type date


def print_birthday_information(days, p_name):
    """
    :param days: Coming from compute_days_between_dates
    :param p_name: String that comes as user input in the main(), normally defining the user name
    :return: Formatted string out of three options based on the value from compute_days_between_dates
    """

    if days < 0:
        print('\n{}, you had your birthday before {} days!'.format(p_name, -days))
    elif days > 0:
        print('\n{}, you will have a birthday in {} days!'.format(p_name, days))
    else:
        print('\nCongratulation {}!!! It\'s your birthday!'.format(p_name))


def main():
    """
    :return: The program main flow
    """

    print_header()
    person_name = input('Your name: ')
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days, person_name)


main()
