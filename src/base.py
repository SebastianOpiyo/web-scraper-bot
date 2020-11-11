from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
import time


class BasePage:
    """Driver class inherited by all the other classes.
    - It does initiate the chrome driver, chrome browser being the option.
    - It also closes the browser if needed."""

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.driver.maximize_window()

    def test_site_access(self, url):
        # Check to see that the site is accessible or not
        # important because the site needs VPN ON to be accessible.
        try:
            self.driver.implicitly_wait(5)
            self.driver.get(url)
            print("Site can be reached!")
        except Exception as e:
            print(f'Site cannot be reached because of {e}')

    def quit_driver(self):
        """Closes all open instances of the browser instances"""
        time.sleep(15)
        self.driver.quit()

    def close_browser(self):
        """Closes the browser that is in ficus."""
        time.sleep(15)
        return self.driver.close()
