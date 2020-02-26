import os

def load(name):
    """
    This method creates and load a new journal.

    :param name: The base name of the journal.
    :return: A new journal data structure populated with the file data
    """
    data = []
    filename = get_full_filename(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = get_full_filename(name)
    print('...saving to {}'.format(filename))

    with open(filename, 'w') as fout:   # this way if an error occurs the file will be automatically closed
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_filename(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)
