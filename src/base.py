from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    """Driver class inherited by all the other classes.
    - It does initiate the chrome driver, chrome browser being the option.
    - It also closes the browser if needed."""

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.driver.maximize_window()

    def exit_driver(self):
        self.driver.quit()