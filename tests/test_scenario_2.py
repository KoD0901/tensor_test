import pytest
from pages.saby_page import SabyContactsPage
import time

def test_scenario_2(browser):
    saby = SabyContactsPage(browser)
    
    print("=== Начало теста второго сценария ===")
    
    print("1. Переход на сайт и открытие контактов...")
    saby.go_to_site()
    saby.open_contacts()
    
    assert "/contacts" in browser.current_url, "Не перешли на страницу контактов"
    
    print("2. Проверка текущего региона и списка партнеров...")
    initial_region = saby.get_current_region()
    print(f"   Начальный регион: '{initial_region}'")
    
    assert initial_region, f"Регион не определен, получено: '{initial_region}'"
    
    initial_partners = saby.get_partner_list()
    print(f"   Начальных партнеров: {len(initial_partners)}")
    
    assert len(initial_partners) > 0, f"Список партнеров пуст для региона {initial_region}"
    
    if initial_partners:
        initial_first_partner = initial_partners[0].split('\n')[0]
        print(f"   Первый партнер: {initial_first_partner}")
    
    target_region = "Камчатский край"
    print(f"3. Изменение региона на {target_region}...")
    saby.change_region(target_region)
    
    print("4. Проверка нового региона...")
    time.sleep(2)
    new_region = saby.get_current_region()
    print(f"   Новый регион: '{new_region}'")
    
    assert "Камчатск" in new_region, f"Регион не изменился на Камчатский край, текущий: {new_region}"
    
    print("5. Проверка нового списка партнеров...")
    new_partners = saby.get_partner_list()
    print(f"   Новых партнеров: {len(new_partners)}")
    
    assert len(new_partners) > 0, f"Новый список партнеров пуст для региона {new_region}"

    if initial_partners and new_partners:
        new_first_partner = new_partners[0].split('\n')[0] if new_partners else ""
        if initial_first_partner != new_first_partner:
            print(f"     Списки партнеров различны: '{initial_first_partner}' vs '{new_first_partner}'")
        else:
            print(f"     Первые партнеры совпадают: '{initial_first_partner}'")

    current_url = browser.current_url.lower()
    print(f"6. Проверка URL: {current_url}")

    url_contains_region = "камчатск" in current_url or "41" in current_url
    assert url_contains_region, f"URL не содержит информацию о регионе Камчатский край: {current_url}"

    title = browser.title.lower()
    print(f"7. Проверка title: {title}")
    
    title_contains_region = "камчатск" in title
    assert title_contains_region, f"Title не содержит информацию о регионе Камчатский край: {title}"
    
    print("=== Тест успешно завершен ===")
    print(f"Итог: регион изменен с '{initial_region}' на '{new_region}'")
    print(f"Партнеров: было {len(initial_partners)}, стало {len(new_partners)}")