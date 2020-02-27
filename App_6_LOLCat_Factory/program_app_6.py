import os
import platform
import subprocess
from Ten_Apps_Course.App_6_LOLCat_Factory import cat_service


def main():
    print_header()

    folder = get_or_create_output_folder()
    print('Found or created folder: {}'.format(folder))
    print()

    count = int(input('Please, set a number of pictures to download: '))
    if not isinstance(count, int):
        count = int(input('Please, set a number of pictures to download: '))

    download_cats(folder, count)

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
    Create a storing location (a folder) where the data will be downloaded and saved.

    :return: The path to the folder location.
    """

    base_folder = os.path.dirname(__file__)
    folder = 'cat_factory'
    full_path = os.path.join(base_folder, folder)

    # checking if the location (folder) with the same name already exists.
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder, count):
    """
    Download (and show the download progress) a user specified number of data objects from a specified resource.

    :param count: The number of objects to be downloaded.
    :param folder: The folder where data has to be stored.
    :return: Download data and shows the downloading progress.
    """

    print('Contacting server to download cats ...')
    cats_count = count
    for i in range(1, cats_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat {}'.format(name))
        cat_service.get_cat(folder, name)

    print('done.')


def display_cats(folder):
    """
    Opens the folder with the downloaded data in explorer (for Windows) or the equivalent for MacOS and Linux.

    :param folder: The folder where objects has to be stored.
    :return: Triggers explorer with a specified location.
    """

    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        # todo: check why using 'explorer' instead of 'start' opens explorer with wrong (not 'folder') location.
        subprocess.call(['start', folder], shell=True)
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print('Sorry, we do not support your OS: {}'.format(platform.system()))


if __name__ == '__main__':
    main()
