from django.core.management import BaseCommand
from my_blog.models import MyBlog


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Удаление данных таблиц
        MyBlog.objects.all().delete()

        # Формирование списка полей для таблицы MyBlog
        article_list = [
            {'id': 1, 'title': 'Офисный пакет', 'slug': 'ofisnyij-paket',
             'body': 'Офисный пакет — набор приложений (программный пакет), предназначенных для обработки электронной '
                     'документации на персональном компьютере. Компоненты офисных пакетов распространяются, '
                     'как правило, только вместе, имеют схожий интерфейс и хорошо взаимодействуют друг с другом.',
             'image': 'product/Office_pac.jpg',
             'creation_date': '2023-08-22T20:01:59Z',
             'is_published': True,
             'view_count': 5},

            {'id': 2, 'title': 'Антивирусная программа', 'slug': 'antivirusnaya-programma',
             'body': 'Антивирусная программа (антивирус, средство антивирусной защиты, средство обнаружения '
                     'вредоносных программ) — специализированная программа для обнаружения компьютерных вирусов, '
                     'а также нежелательных (считающихся вредоносными) программ и восстановления заражённых ('
                     'модифицированных) такими программами файлов и профилактики — предотвращения заражения ('
                     'модификации) файлов или операционной системы вредоносным кодом.',
             'image': 'product/antivirus_progs.jpg',
             'creation_date': '2023-08-22T20:07:16Z',
             'is_published': True,
             'view_count': 3},

            {'id': 3, 'title': 'Операционная система',
             'slug': 'operatsionnaya-sistema',
             'body': 'Операционная система, сокр. ОС (англ. operating system, OS) — программное обеспечение, '
                     'управляющее компьютерами (включая микроконтроллеры) и позволяющее запускать на них прикладные '
                     'программы. Предоставляет программный интерфейс для взаимодействия с компьютером, '
                     'управляет прикладными программами и занимается распределением предоставляемых ресурсов, '
                     'в том числе между прикладными программами. Некоторые операционные системы позволяют прикладным '
                     'программам работать с аппаратным обеспечением напрямую. В широком смысле под операционной '
                     'системой понимается совокупность ядра операционной системы и работающих поверх него программ и '
                     'утилит, предоставляющих интерфейс для взаимодействия пользователя с компьютером. В логической '
                     'структуре типичной вычислительной системы операционная система занимает положение между '
                     'устройствами с их микроархитектурой, машинным языком и, возможно, собственными (встроенными) '
                     'микропрограммами (драйверами) — с одной стороны — и прикладными программами с другой. '
                     'Разработчикам программного обеспечения операционная система позволяет абстрагироваться от '
                     'деталей реализации и функционирования устройств, предоставляя минимально необходимый набор '
                     'функций (см. интерфейс программирования приложений). В большинстве вычислительных систем '
                     'операционная система является основной, наиболее важной (а иногда и единственной) частью '
                     'системного программного обеспечения. С 1990-х годов наиболее распространёнными операционными '
                     'системами являются системы семейства Windows, Unix и UNIX-подобные системы.',
             'image': 'product/osys.jpg',
             'creation_date': '2023-08-22T20:10:30Z',
             'is_published': True,
             'view_count': 5},

            {'id': 4, 'title': 'Графические редакторы',
             'slug': 'graficheskie-redaktoryi',
             'body': 'Эту статью всё равно никто не увидит, потому что она не опубликована.',
             'image': 'product/gr_red.jpg',
             'creation_date': '2023-08-22T20:13:53Z',
             'is_published': False,
             'view_count': 0},
        ]

        # Формирование списка объектов класса MyBlog для распаковки
        article_for_create = []
        for article_item in article_list:
            article_for_create.append(
                MyBlog(**article_item)
            )

        # Запись данных в таблицу сategory
        MyBlog.objects.bulk_create(article_for_create)