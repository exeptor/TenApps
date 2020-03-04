import requests

# todo: why importing country_domain with with the full path fix the Pycharm error message, but fails the execution of
#  the program if the same file is called in command line?
#  Example:
#  ------------------------------ Run <program_app_5> in cmd --------------------------------------
#   (testnv) C:\Users\Tsvetomila\Desktop\PythonQA\Ten_Apps_Course\App_5_Real_Time_Weather_Client>python program_app_5.py
#   Traceback (most recent call last):
#     File "program_app_5.py", line 2, in <module>
#       import Ten_Apps_Course.App_5_Real_Time_Weather_Client.country_domain as ctrdom
#   ModuleNotFoundError: No module named 'Ten_Apps_Course'
#   ------------------------------------------------------------------------------------------------
import Ten_Apps_Course.App_5_Real_Time_Weather_Client.country_domain as ctrdom

import bs4
import collections

# todo: why importing the module directly cause Pycharm to throw an error 'No module named country_domain', but when
#  used in the code bellow all methods defined in the country_domain are successfully called/invoked.
# import country_domain as ctrdom

WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, loc')


def main():
    print_header()

    file_name = 'country_domain'
    city = input('Please, specify the name of the city: ')
    city = city.lower().strip()
    country = input('Please, specify the country where the city is located: ')
    country = country.lower().strip()

    try:
        html = get_html_from_web(country, file_name, city)
        report = get_weather_from_html(html)
        print()
        print('-------------------------------------------------')
        print('The temp in {} is {} °C and {}.'.format(report.loc, report.temp, report.cond))
        print('-------------------------------------------------')
    except:
        print('Oops, something went wrong! Check the name of the city and/or country.')


def print_header():
    """
    Prints the standard (course convention) header with the name of the application.

    :return: Prints the header in a standardized format.
    """

    print('-----------------------------------')
    print('          WEATHER APP')
    print('-----------------------------------')
    print()


def get_html_from_web(country, file_name, city):
    """
    Build a structurally valid url in a specified format (e.g. <default_url_part>/<country_domain>/<city_name>)
    with country domain (extracted from a stored file) and city name.

    :param country: The name of the country where the specified city is located
    :param file_name: The name of the stored file which contains country-to-domain list
    :param city: The name of the city
    :return: Html response in a text format
    """

    domain = ctrdom.get_domain(country, file_name)
    url = 'https://www.wunderground.com/weather/{}/{}'.format(domain, city)
    response = requests.get(url)

    return response.text


def get_weather_from_html(html):
    """
    Extract location, temperature and condition from a html response, store and return them in a named tuple.

    :param html: Html response in text format
    :return: A named tuple containing location, temperature and condition at this location.
    """

    soup = bs4.BeautifulSoup(html, 'html.parser')

    html_loc = soup.find('h1').get_text()  # location string coming from html response
    loc = clean_location(html_loc)

    html_temperature = soup.find(class_='wu-value wu-value-to').get_text()  # temp value coming from html response
    temperature = to_celsius(html_temperature)

    condition = soup.find(class_='condition-icon small-6 medium-12 columns').get_text()

    report = WeatherReport(cond=condition, temp=temperature, loc=loc)

    return report


def clean_location(text):
    # todo: how this could be changed in more generic way in order to be used for different inputs (not only location)
    """
    Clean the html response (location part) to show only the city part.

    :param text: html response string containing location
    :return: City part of html response
    """

    split_text = text.split(',')
    text = split_text[0]

    return text


def to_celsius(fahrenheit):
    """
    Convert fahrenheit to celsius by explicitly convert input parameter to integer and round the end result.

    :param fahrenheit: Data with undefined type (i.e. could be int or str).
    :return: Rounded celsius temperature of type int.
    """

    celsius = round((int(fahrenheit) - 32) * 5 / 9)

    return celsius


if __name__ == '__main__':
    main()
