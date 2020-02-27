import os
import platform
import subprocess
from Ten_Apps_Course.App_6_LOLCat_Factory import cat_service


def main():
    print_header()

    folder = get_or_create_output_folder()
    print('Found or created folder: {}'.format(folder))

    download_cats(folder)

    display_cats(folder)


def print_header():
    """
    Prints the standard (course convention) header with the name of the application.

    :return: Prints the header in a standardized format.
    """

    print('------------------------------------')
    print('          CAT FACTORY')
    print('------------------------------------')


def get_or_create_output_folder():
    """


    :return:
    """

    base_folder = os.path.dirname(__file__)
    folder = 'cat_factory'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    """


    :param folder:
    :return:
    """

    print('Contacting server to download cats ...')
    cats_count = 8
    for i in range(1, cats_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat {}'.format(name))
        cat_service.get_cat(folder, name)

    print('done.')


def display_cats(folder):
    """


    :param folder:
    :return:
    """
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['start', folder], shell=True)
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print('Sorry, we do not support your OS: {}'.format(platform.system()))


if __name__ == '__main__':
    main()