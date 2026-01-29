import pytest
from pages.saby_page import SabyContactsPage
from pages.tensor_page import TensorPage

def test_scenario_1(browser):
    saby = SabyContactsPage(browser)
    tensor = TensorPage(browser)
    
    saby.go_to_site()
    saby.open_contacts()
    
    saby.click_tensor_banner()
    saby.switch_to_new_tab()
    
    assert "tensor.ru" in browser.current_url, "Не перешли на сайт Тензора"
    assert tensor.is_power_block_present(), "Блок 'Сила в людях' не найден"
    
    tensor.click_about()
    assert "tensor.ru/about" in browser.current_url, "Не перешли на страницу 'О компании'"
    
    assert tensor.are_images_equal_size(), "Изображения имеют разный размер!"