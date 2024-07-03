# Проект парсер авито

Этот проект парсит json файлы свежих объявлений о недвижимости на авито и заносит их в базу данных sqllite3 
## Использованные библиотеки

В ходе написания этого проекта использовались следующие библиотеки:

- **beautifulsoup4** (версия 4.12.3) - для парсинга HTML и XML документов.
- **requests** - для выполнения HTTP запросов.
- **lxml** - для обработки XML и HTML документов.
- **sqllite3** - для работы с базой данных sql.

## Как использовать

1. Установите необходимые библиотеки:

   ```bash
   pip install beautifulsoup4==4.12.3 requests lxml