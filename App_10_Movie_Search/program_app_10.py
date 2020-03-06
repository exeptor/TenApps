import requests

from Ten_Apps_Course.App_10_Movie_Search import movie_svc


def main():
    print_header()
    search_event_loop()


def print_header():
    print('--------------------------------------------')
    print('            MOVIE SEARCH APP')
    print('--------------------------------------------')
    print('')


def search_event_loop():
    search = 'GO_ONCE_THROUGH_THE_LOOP'

    while search != 'x':
        try:
            search = input('Movie search text (x for exit): ')
            if search != 'x':
                results = movie_svc.find_movies(search)
                print('Found {} results.'.format(len(results)))
                for r in results:
                    print('{} -- {}'.format(r.year, r.title))
        except ValueError:
            print('Error: Search text is required!')
        except requests.exceptions.ConnectionError:
            print('Error: Your network is down!')
        except Exception as x:
            print('Error: Unexpected error occurs. Details: {}'.format(x))

    print('... exiting.')


if __name__ == '__main__':
    main()
