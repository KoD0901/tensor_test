# Windows
python -m venv venv
venv\Scripts\activate

# MacOS/Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# Запуск всех тестов
pytest

# Запуск с подробным выводом
pytest -s

# Запуск конкретного файла тестов
pytest tests/test_scenario_1.py -s
pytest tests/test_scenario_2.py -s