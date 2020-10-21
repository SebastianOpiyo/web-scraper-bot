from selenium import webdriver


class BasePage:
    """Driver class inherited by all the other classes."""

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()