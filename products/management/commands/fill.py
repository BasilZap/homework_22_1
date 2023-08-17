from django.core.management import BaseCommand
from products.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Удаление данных таблиц
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Формирование списка полей для таблицы "Категории"
        category_list = [
            {'id': 1, 'category_name': 'Операционная система',
             'category_description': 'Устанавливается на новый ПК и всё работает'},
            {'id': 2, 'category_name': 'Антивирус',
             'category_description': 'Защищает компьютер от вирусов, кричит, ругается, грузит систему'},
            {'id': 3, 'category_name': 'Офисное ПО',
             'category_description': 'Работа с текстом, числами, таблицами и прочими интересными вещами'},
            {'id': 4, 'category_name': 'Графика и дизайн',
             'category_description': 'Всё для того, чтобы делать "Красиво"'},
        ]

        # Формирование списка объектов класса Category для распаковки
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        # Запись данных в таблицу сategory
        Category.objects.bulk_create(category_for_create)

        # Формирование списка полей для таблицы "Продукты"
        product_list = [
            {'id': 1, 'product_name': 'Windows 10', 'product_description': 'Устаревшая версия Windows 11, основным '
                                                                           'отличием является то, что.. что?',
             'image_preview': 'product/Win_10.png',
             'category': Category.objects.get(pk=1), 'price': 8000, 'creation_date': "2023-08-11T20:58:01Z",
             'change_date': "2023-08-12T20:58:01Z"},
            {'id': 2, 'product_name': 'Windows 11', 'product_description': 'Более новая, современная и сырая версия '
                                                                           'Windows 10, можно установить на свой ПК и'
                                                                           ' проводить холодные зимние вечера за '
                                                                           'бета-тестированием.',
             'image_preview': 'product/Win_11.png',
             'category': Category.objects.get(pk=1), 'price': 25000, 'creation_date': "2023-09-11T20:58:01Z",
             'change_date': "2023-09-20T10:58:01Z"},
            {'id': 3, 'product_name': 'Astra Linux', 'product_description': 'Это прямо для гурманов. 10 из 10.',
             'image_preview': 'product/Astra.png', 'category': Category.objects.get(pk=1), 'price': 54000,
             'creation_date': "2022-04-11T13:58:01Z", 'change_date': "2022-06-14T10:58:01Z"},

            {'id': 4, 'product_name': 'Антивирус Касперского', 'product_description': 'Проверяет всегда, все и везде, '
                                                                                      'не особенно спрашивает '
                                                                                      'разрешения, отлично грузит '
                                                                                      'систему.',
             'image_preview': 'product/KAV.png', 'category': Category.objects.get(pk=2), 'price': 1343,
             'creation_date': "2022-04-11T13:58:01Z", 'change_date': "2022-06-14T10:58:01Z"},

            {'id': 5, 'product_name': 'Kaspersky Internet Security', 'product_description': 'Отлично грузит не только '
                                                                                            'систему но еще и '
                                                                                            'Интернет, '
                                                                                            'выбор редакции, '
                                                                                            'остальной функционал как '
                                                                                            'у антивируса Касперского.',
             'image_preview': 'product/KIS.png', 'category': Category.objects.get(pk=2), 'price': 1823,
             'creation_date': "2022-04-11T13:58:01Z", 'change_date': "2022-06-14T10:58:01Z"},

            {'id': 6, 'product_name': 'Dr. Web', 'product_description': 'Сидит себе тихонечко в трее, вроде чего-то '
                                                                        'ищет... лечит...',
             'image_preview': 'product/Dr_Web.png', 'category': Category.objects.get(pk=2), 'price': 1610,
             'creation_date': "2022-04-11T13:58:01Z", 'change_date': "2022-06-14T10:58:01Z"},

            {'id': 7, 'product_name': 'Microsoft Office Home and Business',
             'product_description': 'Полный набор офисных радостей в одной коробке',
             'image_preview': 'product/Office.png', 'category': Category.objects.get(pk=3), 'price': 34939,
             'creation_date': "2022-04-11T13:58:01Z", 'change_date': "2022-06-14T10:58:01Z"},

            {'id': 8, 'product_name': 'МойОфис Стандартный 2',
             'product_description': 'Название броское, многообещающее. Покупаем, ставим, выясняем что это.',
             'image_preview': 'product/My_off.png', 'category': Category.objects.get(pk=3), 'price': 6690,
             'creation_date': "2022-04-11T13:58:01Z", 'change_date': "2022-06-14T10:58:01Z"},

            {'id': 9, 'product_name': 'CorelDRAW Graphics Suite 2023',
             'product_description': 'Замечательный редактор векторной графики с девизом "Совершенство через страдания"',
             'image_preview': 'product/Corel.png', 'category': Category.objects.get(pk=4), 'price': 123726,
             'creation_date': "2022-04-11T13:58:01Z", 'change_date': "2022-06-14T10:58:01Z"},

            {'id': 10, 'product_name': 'Adobe Photoshop CC',
             'product_description': 'Специальная программа для замазывания прыщей на фото, можно и фотожабы на друзей.',
             'image_preview': 'product/Photoshop.png', 'category': Category.objects.get(pk=4), 'price': 67131,
             'creation_date': "2022-04-11T13:58:01Z", 'change_date': "2022-06-14T10:58:01Z"},

        ]

        # Формирование списка объектов класса Product для распаковки
        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product(**product_item)
            )

        # Запись данных в таблицу product
        Product.objects.bulk_create(product_for_create)
