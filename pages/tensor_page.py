from selenium.webdriver.common.by import By
from .base_page import BasePage

class TensorPage(BasePage):
    POWER_BLOCK = (By.CSS_SELECTOR, ".tensor_ru-Index__block4")
    ABOUT_LINK = (By.XPATH, "//div[contains(@class, 'tensor_ru-Index__block4')]//a[contains(@href, '/about') and text()='Подробнее']")

    WORK_IMAGES = (By.CSS_SELECTOR, ".tensor_ru-About__block3-image-wrapper img")

    def is_power_block_present(self):
        block = self.find(self.POWER_BLOCK)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", block)
        return block.is_displayed()

    def click_about(self):
        self.find_clickable(self.ABOUT_LINK).click()

    def are_images_equal_size(self):
        images = self.find_all(self.WORK_IMAGES)
        sizes = []
        for img in images:
            w = img.get_attribute("width")
            h = img.get_attribute("height")
            sizes.append((w, h))
        
        return all(s == sizes[0] for s in sizes)