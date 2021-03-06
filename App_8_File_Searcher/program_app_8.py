import os
import collections

SearchResults = collections.namedtuple('SearchResults', 'file, line, text')


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("We can't search that location.")
        return

    text = get_search_text_from_user()
    if not text:
        print('We can\'t search for nothing')
        return

    matches = search_folders(folder, text)
    match_count = 0
    for m in matches:
        match_count += 1
        # Use this when search in small size data (a few MB).
        # print()
        # print('-------------- MATCH -------------')
        # print('file: {}'.format(m.file))
        # print('line: {}'.format(m.line))
        # print('match: {}'.format(m.text.strip()))
        # print()

    print('-------------- SUMMARY -------------')
    print('Found {} matches for \'{}\' in {}.'.format(match_count, text, folder))


def print_header():
    print('---------------------------------')
    print('        FILE SEARCH APP')
    print('---------------------------------')
    print('')


def get_folder_from_user():
    folder = input('Which folder do you want to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What are yo searching for [single phrase only]? ')
    return text.lower()


# def search_folders(folder, text):
#     all_matches = []
#     items = os.listdir(folder)
#
#     for item in items:
#         full_item = os.path.join(folder, item)
#         if os.path.isdir(full_item):
#             matches = search_folders(full_item, text)  # Fix the folder problem with recursion
#             all_matches.extend(matches)
#         else:
#             matches = search_file(full_item, text)
#             all_matches.extend(matches)
#
#     return all_matches
#
#
# def search_file(filename, search_text):
#     matches = []
#     with open(filename, 'r') as fin:
#         line_num = 0
#         for line in fin:
#             line_num += 1
#             if line.lower().find(search_text) >= 0:
#                 m = SearchResults(line=line_num, file=filename, text=line)
#                 matches.append(m)
#
#         return matches


# Using generators (both functions bellow) to work out the performance issue (esp. the memory usage).

def search_folders(folder, text):
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folders(full_item, text)
        else:
            yield from search_file(full_item, text)


def search_file(filename, search_text):
    with open(filename, 'r') as fin:
        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResults(line=line_num, file=filename, text=line)
                yield m


if __name__ == '__main__':
    main()
