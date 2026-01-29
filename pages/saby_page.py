from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import time

class SabyContactsPage(BasePage):
    CONTACTS_MENU_ITEM = (By.XPATH, "//div[contains(@class, 'sbisru-Header')]//*[text()='Контакты']")
    MORE_OFFICES_LINK = (By.XPATH, "//div[contains(@class, 'sbisru-Header-ContactsMenu')]//a[contains(@href, '/contacts')]")
    TENSOR_BANNER = (By.CSS_SELECTOR, "a.sbisru-Contacts__logo-tensor")
    
    REGION_CHOOSER_TEXT = (By.XPATH, "//span[contains(@class, 'sbis_ru-Region-Chooser__text')]")
    REGION_CHOOSER = (By.CSS_SELECTOR, ".sbis_ru-Region-Chooser")
    REGION_TEXT_ANY = (By.XPATH, "//span[contains(text(), 'обл.') or contains(text(), 'край') or contains(text(), 'респ')]")

    PARTNER_ITEMS = (By.CSS_SELECTOR, ".sbisru-Contacts-List__item")

    def open_contacts(self):
        """Открыть раздел контактов"""
        menu = self.find(self.CONTACTS_MENU_ITEM)
        actions = ActionChains(self.browser)
        actions.move_to_element(menu).perform()
        time.sleep(1)
        target = self.find_clickable(self.MORE_OFFICES_LINK)
        target.click()
        time.sleep(2)

    def click_tensor_banner(self):
        banner = self.find_clickable(self.TENSOR_BANNER)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", banner)
        banner.click()

    def get_region_text(self, timeout=10):
        """Получить текст региона с ожиданием появления элемента"""
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(self.REGION_CHOOSER_TEXT)
            )
            
            for locator in [self.REGION_CHOOSER_TEXT, self.REGION_TEXT_ANY]:
                try:
                    elements = self.browser.find_elements(*locator)
                    for element in elements:
                        text = element.text.strip()
                        if text and ('обл.' in text or 'край' in text or 'респ' in text):
                            print(f"Найден регион по локатору {locator}: '{text}'")
                            return text
                except:
                    continue
                    
        except Exception as e:
            print(f"Ошибка при поиске региона: {e}")
        
        return ""

    def change_region(self, region_name):
        """Изменить регион"""
        time.sleep(2)

        try:
            region = self.find(self.REGION_CHOOSER_TEXT, time=10)
            print(f"Найден элемент региона: {region.text}")

            self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", region)
            time.sleep(1)

            self.browser.execute_script("arguments[0].click();", region)
            print(f"Кликнули по текущему региону")
            
        except Exception as e:
            print(f"Ошибка при клике по текущему региону: {e}")
            try:
                region = self.find(self.REGION_CHOOSER, time=10)
                self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", region)
                self.browser.execute_script("arguments[0].click();", region)
                print(f"Кликнули по альтернативному элементу региона")
            except Exception as e2:
                print(f"Ошибка при клике по альтернативному элементу: {e2}")
                raise

        time.sleep(2)

        region_xpaths = [
            f"//div[contains(@class,'sbis_ru-Region-Panel')]//*[contains(normalize-space(text()), '{region_name}')]",
            f"//*[contains(@class,'sbis_ru-Region-Panel')]//*[contains(text(), '{region_name}')]",
            f"//*[contains(@class,'sbis_ru-Region-Panel')]//*[contains(., '{region_name}')]",
        ]
        
        region_el = None
        for xpath in region_xpaths:
            try:
                region_el = self.browser.find_element(By.XPATH, xpath)
                if region_el and region_el.is_displayed():
                    print(f"Нашли регион '{region_name}' по XPath: {xpath[:50]}...")
                    break
            except:
                continue
        
        if not region_el:
            raise Exception(f"Не удалось найти регион '{region_name}' в выпадающем списке")

        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", region_el)
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", region_el)
        print(f"Выбрали регион: {region_name}")

        time.sleep(3)

        current_url = self.browser.current_url
        print(f"Текущий URL после смены региона: {current_url}")

    def get_current_region(self, timeout=15):
        """Получить текущий регион с ожиданием"""
        region_text = ""
        start_time = time.time()
        
        while time.time() - start_time < timeout and not region_text:
            region_text = self.get_region_text(5)
            if not region_text:
                print("Регион не найден, ждем...")
                time.sleep(1)
        
        return region_text

    def get_partner_list(self, timeout=10):
        """Получить список партнеров"""
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(self.PARTNER_ITEMS)
            )
            partners = self.find_all(self.PARTNER_ITEMS)
            return [p.text.strip() for p in partners if p.text.strip()]
        except:
            print("Не удалось найти список партнеров")
            return []