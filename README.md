# Парсер продуктов магазина METRO
Проект на Scrapy и Selenium, собирает все продукты из одной категории и их свойства,
после этого сохраняет их в jsonlines-файл в папке data.

---
## Запуск приложения
В корне репозитория выполните:
```
    python3 -m venv venv # для запуска основного приложения
    source venv/bin/activate # активация виртуального окружения
    pip install -r requirements.txt # установка зависимостей
    scrapy crawl cheese_spider # запуск паука
```
---

## Технологии

- Python 3.11
- Scrapy
- Selenium
