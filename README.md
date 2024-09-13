# e2e_ui
Автоматический E2E тест для проверки сценария покупки товара на сайте saucedemo.com с использованием Python + Selenium.
Скрипт проверяет процесс от авторизации до завершения покупки.

### Запуск проекта на локальной машине:

Клонировать репозиторий:
```
git clone https://github.com/Anton-Kim/e2e_ui.git
```
Cоздать виртуальное окружение:
```
python -m venv venv
```
Активировать виртуальное окружение:
```
source venv/scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Запустить скрипт любым удобным способом:
```
python test_api.py
```