import shutil
import requests
import os

def get_cat(folder, name):
    """


    :param folder:
    :param name:
    :return:
    """
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)
    save_image(folder, name, data)


def get_data_from_url(url):
    """


    :param url:
    :return:
    """
    response = requests.get(url, stream=True)

    return response.raw


def save_image(folder, name, data):
    file_name = os.path.join(folder, name + '.jpg')
    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)
