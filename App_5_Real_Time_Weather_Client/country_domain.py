import os

def get_full_filename(name):
    """
    Building the filepath for the country-domain list.

    :param name: The name of the file which stores the country-domain list.
    :return: The full filepath to access the resource.
    """

    filename = os.path.abspath(os.path.join('.', 'files', name + '.txt'))
    return filename


def load(name):
    """
    Creates a dictionary object from the country-domain list.

    :param name: The name of the file which stores the country-domain list.
    :return: Dictionary containing country-domain data (e.g. {'Bulgaria': 'bg', 'Germany': 'de'}).
    """

    data = {}
    filename = get_full_filename(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for line in fin:
                k, v = line.strip().split(',')
                data[v.lower().strip()] = k.strip()

    return data


def get_domain(country, file_name):
    """
    Extracts the domain part from the country-domain dictionary.

    :param country: Used as dictionary key to extract the corresponding value
    :param file_name: The name of the file which stores the country-domain list.
    :return: The domain of the specified country (e.g. 'bg' for Bulgaria, 'de' for Germany)
    """

    country_domain = load(file_name)
    domain = country_domain[country]

    return domain
