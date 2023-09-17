# Домашняя работа 23.2. "Кеширование и работа с переменными окружения".

## Функционал.
Программа работает с СУБД PostgreSQL, с полями таблиц продукты и категории,
для которых созданы и описаны соответствующие модели. Созданы отображения 
и фильтры для таблиц в панели администратора Django. 
Разработаны три html-страницы для отображения списка продуктов и каждого продукта
в отдельности с подробным описанием.

В версии 22.2 добавлено приложение для работы с пользователями
В версии 23.2 добавлено отображение списка категорий и вывод продуктов по категориям

#### Создана таблица содержащая данные о статьях по типам программного обеспечения.
#### В меню главной страницы сайта добавлена ссылка "Блог".
#### Приложение "Блог" позволяет создавать, редактировать, удалять и отображать записи.
#### Добавлены формы позволяющие пользователь добавлять, редактировать и удалять продукты и их версии.
#### Реализованы фильтры на запрет ввода в название продукта запрещенных слов.
#### Добавлена стилизация форм.
#### Добавлена модель Version, позволяющая работать с версиями продуктов.
v 22.2
#### Добавлены возможности регистрации по почте и паролю, авторизации, просмотра и редактирования пользователей
#### Добавлена верификацию почты пользователя через отправленное письмо
#### Восстановление пользователя на автоматически сгенерированный пароль.
#### Редактирование, добавление и удаление продуктов закрыто для незарегистрированных пользователей
#### Создаваемые продукты автоматически привязываются к пользователю
v 23.2
#### Установлен redis, добавлено кеширование контроллера отображения одного продукта
#### Создана функция для отображения категорий продуктов, добавлено ее кеширование 
#### Чувствительные данные вынесены в файл .env

### Требования к установке.
- В PostgreSQL должна быть создана DB - products
- Необходимо заполнить таблицы БД значениями

Заполнение базы осуществляетя через команды:
- Суперпользователь
```
> python manage.py ucreate
```
- Блог
```
> python manage.py fill_blog
```
- Продукты
```
> python manage.py fill
```


## Требования к окружению

#### В программе используется менеджер зависимостей venv.
Используются следующие зависимости:

- Django==4.2.4
- ipython==8.14.0
- Pillow==10.0.0
- psycopg2-binary==2.9.7
- pytils==0.4.1
- redis==5.0.0
- python-dotenv==1.0.0


### !!! Для возможности отправки email, и подключения к postgres необходимо внести соответствующие значения в .env, .env.sample прилагается !!! 