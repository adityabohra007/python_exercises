import requests


URL = 'http://movie_service.talkpython.fm/api/search/'


def main():
    print_header()
    main_loop()


def print_header():
    print('------------------------------')
    print('      Movie Search App')
    print('------------------------------')
    print()


def main_loop():
    search_text = None

    while search_text != 'x':
        try:
            search_text = input('Enter search text (x to exit): ').strip()
            if search_text != 'x':
                results = movie_search(search_text)

                print('Found {} movie(s)'.format(len(results)))
                for movie in results:
                    title, year = movie
                    print('{} - {}'.format(year, title))
        except ValueError:
            print('Error with that: Bad title!')
        except requests.exceptions.ConnectionError:
            print('Host unreachable, sorry network is down')
        except Exception as e:
            print(e)
        print()


def movie_search(search_text):
    url = URL + search_text

    response = requests.get(url)
    response.raise_for_status()

    response_data = response.json()
    movies = response_data.get('hits')

    results = [(movie['title'], movie['year']) for movie in movies]
    results.sort(key=lambda x: -x[1])

    return results


if __name__ == '__main__':
    main()
