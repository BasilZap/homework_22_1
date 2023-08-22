# Домашняя работа 21.1. "fbv и cbv".

## Функционал.
Программа работает с СУБД PostgreSQL, с полями таблиц продукты и категории,
для которых созданы и описаны соответствующие модели. Созданы отображения 
и фильтры для таблиц в панели администратора Django. 
Разработаны три html-страницы для отображения списка продуктов и каждого продукта
в отдельности с подробным описанием.

#### Создана таблица содержащая данные о статьях по типам программного обеспечения.
#### В меню главной страницы сайта добавлена ссылка "Блог".
#### Приложение "Блог" позволяет создавать, редактировать, удалять и отображать записи.

### Требования к установке.
- В PostgreSQL должна быть создана DB - products
- Необходимо заполнить таблицы БД значениями

Заполнение может осуществляться через фикстуру
```
> python manage.py loaddata myblog_data.json
```


## Требования к окружению

#### В программе используется менеджер зависимостей venv.
Используются следующие зависимости:

- Django==4.2.4
- ipython==8.14.0
- Pillow==10.0.0
- psycopg2-binary==2.9.7
- pytils==0.4.1