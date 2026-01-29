### Стек технологий

- **Python 3.11+**
- **Selenium WebDriver 4.x**
- **pytest**
- **Webdriver-manager** (для автоматического управления драйверами)

## Структура проекта

```
.
├── pages/                    # Page Object Model классы
│   ├── __init__.py
│   ├── base_page.py         # Базовый класс для всех страниц
│   ├── saby_page.py         # Page Object для saby.ru
│   └── tensor_page.py       # Page Object для tensor.ru
├── tests/                    # Тесты
│   ├── __init__.py
│   ├── test_scenario1.py    # Тесты для Сценария 1
│   └── test_scenario2.py    # Тесты для Сценария 2
├── conftest.py              # Pytest конфигурация и fixtures
├── pytest.ini               # Pytest настройки
├── requirements.txt         # Зависимости проекта
└── README.md               # Этот файл
```

## Установка

### 1. Создание виртуального окружения

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Проверка установки Chrome/Chromium

Тесты используют Google Chrome. Убедитесь, что Chrome установлен на вашей системе.

## Запуск тестов

### Запуск всех тестов

```bash
pytest
```

### Запуск конкретного сценария

```bash
# Сценарий 1
pytest -m scenario1

# Сценарий 2
pytest -m scenario2

# Smoke тесты
pytest -m smoke
```

### Запуск конкретного файла

```bash
pytest tests/test_scenario1.py
pytest tests/test_scenario2.py
```
