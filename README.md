# mmorpg
Т.З.
Необходимо разработать интернет-ресурс для фанатского сервера одной известной MMORPG — что-то вроде доски объявлений. Пользователи нашего ресурса должны иметь возможность зарегистрироваться в нём по e-mail, получив письмо с кодом подтверждения регистрации. После регистрации им становится доступно создание и редактирование объявлений. Объявления состоят из заголовка и текста, внутри которого могут быть картинки, встроенные видео и другой контент. Пользователи могут отправлять отклики на объявления других пользователей, состоящие из простого текста. При отправке отклика пользователь должен получить e-mail с оповещением о нём. Также пользователю должна быть доступна приватная страница с откликами на его объявления, внутри которой он может фильтровать отклики по объявлениям, удалять их и принимать (при принятии отклика пользователю, оставившему отклик, также должно прийти уведомление). Кроме того, пользователь обязательно должен определить объявление в одну из следующих категорий: Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний. Также мы бы хотели иметь возможность отправлять пользователям новостные рассылки.

Краткое пояснение. Основное:

1) Для реализации регистрации используются библиотеки django-user-accounts и django-allauth. В настройках (bulletin_board/settings.py) прописываем LOGIN_URL, LOGIN_REDIRECT_URL и т.д. Там же ACCOUNT_EMAIL_REQUIRED - пользователь должен обязательно подтвердить e-mail. ACCOUNT_UNIQUE_EMAIL - e-mail должен быть уникальным. Ниже находятся константы, относящиеся к почтовому сервису. Еще ниже - настройки Celery.
2) В сигналах (bulletin/signals.py) прописываем функции: отправить письмо автору поста после отклика и отправить письмо юзеру, оставившему отклик.
3) В моделях прописываем авторов, отзывы, объявления, категории согласно Т.З.
4) Пишем вьюшки для списка новостей, а также для их поиска, удаления, добавления, обновления, а также для обзоров.
5) Подключаем MEDIA и STATIC в settings.py. Подгружаем статику через python manage.py collectstatic
6) В настройках Celery (celery.py) указываем Celery автоматически искать задания в файлах tasks.py каждого приложения проекта.
7) В tasks.py прописаны еженедельная отсылка, а также отправка отклика.
