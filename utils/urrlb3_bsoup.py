import urllib3
from bs4 import BeautifulSoup


def get_upcoming_events(url):
    """We make use of urllib3 in this module instead of requests module.
    The changes are however minimal.
    NOTE: Unlike requests urllib3 doesn't apply header encoding automatically."""
    req = urllib3.PoolManager()
    res = req.request('GET', url)
    soup = BeautifulSoup(res.data, 'html.parser')
    # The above lines are the only difference. Below onwards it's the same.
    events = soup.find('ul', {'class': 'list-recent-events'}).findAll('li')

    for event in events:
        event_details = dict()
        event_details['name'] = event.find('h3').find('a').text
        event_details['location'] = event.find('span', {'class', 'event-location'}).text
        event_details['time'] = event.find('time').text
        print(event_details)


if __name__ == '__main__':
    url = 'https://www.python.org/events/python-events/'
    get_upcoming_events(url)
