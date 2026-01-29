from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = "https://saby.ru"

    def find(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))

    def find_all(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator))

    def find_clickable(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator))

    def go_to_site(self, url=None):
        target = url if url else self.base_url
        self.browser.get(target)

    def switch_to_new_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[-1])

    def get_current_url(self):
        return self.browser.current_url

    def get_title(self):
        return self.browser.title