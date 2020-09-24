from selenium import webdriver


def get_upcoming_events(url):
    # this is the only line that changes
    # the rest remain the same as in selenium.
    driver = webdriver.PhantomJS()
    driver.get(url)

    events = driver.find_elements_by_xpath('//ul[contains(@class, "list-recent-events")]/li')

    for event in events:
        event_details = dict()
        event_details['name'] = event.find_element_by_xpath('h3[@class="event-title"]/a').text
        event_details['location'] = event.find_element_by_xpath('p/span[@class="event-location"]').text
        event_details['time'] = event.find_element_by_xpath('p/time').text
        print(event_details)
    # When done, we don't want to populate our display with lots of open web
    # browser tabs.
    driver.close()


if __name__ == '__main__':
    get_upcoming_events('https://www.python.org/events/python-events/')
