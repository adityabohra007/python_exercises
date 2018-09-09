import bs4
import collections
import requests


SITE_URL = 'https://www.wunderground.com/weather-forecast/'


WeatherReport = collections.namedtuple('WeatherReport', 'location, temperature, scale, condition')


def main():
    print_header()
    zipcode = get_zipcode()
    html = get_html_from_site(SITE_URL, zipcode)
    report = get_report(html)
    print_report(report)


def print_header():
    print('---------------------------')
    print('       WEATHER APP')
    print('---------------------------')
    print()


def get_zipcode():
    zipcode = input('Enter your zipcode (e.g. 01010): ')
    return zipcode


def get_html_from_site(site, zipcode):
    url = site + zipcode
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return ''


def get_report(html):
    if not html:
        return ''

    soup = bs4.BeautifulSoup(html, 'html.parser')

    location = soup.find(class_='columns').find('h1').get_text()
    temperature = soup.find(class_='current-temp').find(class_='wu-value-to').get_text()
    scale = soup.find(class_='current-temp').find(class_='wu-label').get_text()
    condition = soup.find(class_='conditions-extra').find('p').get_text()

    location = cleanup_report_field(location)
    temperature = cleanup_report_field(temperature)
    scale = cleanup_report_field(scale)
    condition = cleanup_report_field(condition)

    return WeatherReport(location=location, temperature=temperature, scale=scale, condition=condition)


def cleanup_report_field(field):
    return field.strip()


def print_report(report):
    if report:
        print('The weather in {} is {} {} and {}'.format(report.location, report.temperature,
                                                         report.scale, report.condition))
    else:
        print("Sorry, we can't get the weather for your zip code")


if __name__ == '__main__':
    main()
