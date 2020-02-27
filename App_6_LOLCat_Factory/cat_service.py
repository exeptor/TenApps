import shutil
import requests
import os

def get_cat(folder, name):
    """
    Download and save (under specified location) an object (picture) from a specified resource.

    :param folder: The folder where data should be stored.
    :param name: The name of the object (picture).
    :return: Data (picture) in a specified location.
    """

    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)
    save_image(folder, name, data)


def get_data_from_url(url):
    """
    Get raw data (binary) from a specified resource.

    :param url: The resource location (website url).
    :return: Binary data (picture).
    """

    response = requests.get(url, stream=True)

    return response.raw


def save_image(folder, name, data):
    """
    Save some data (e.g. picture) in a specified location.

    :param folder: The folder where data should be stored.
    :param name: Name of the object (e.g. picture).
    :param data: Downloaded data (e.g. picture) stored in the memory.
    :return: Object (e.g. picture) saved in a specified location.
    """

    file_name = os.path.join(folder, name + '.jpg')

    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)
