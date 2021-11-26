# Self Storage

Сайт аренды боксов

## Требования к окружению

* Python 3.7 и выше,
* Linux/Windows,
* Переменные окружения (ПеО).

Проект настраивается через ПеО, достаточно задать их в файле `.env.override`.
Передача значений ПеО происходит с использованием [environs](https://pypi.org/project/environs/).

### Общие

#### Параметры проекта

|       Ключ        |     Назначение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`ALLOWED_HOSTS`| Разрешённые хосты | - |
|`DEBUG`| Режим отладки | `False` |
|`SECRET_KEY`| Уникальное непредсказуемое значение | - |
|`STATIC_ROOT`| Имя каталога с статикой проекта |`static`|
|`STATIC_URL`| Имя path-части URL для отдачи статики |`/static/`|
|`MEDIA_ROOT`| Имя каталога с медиа-файлами проекта |`media`|
|`MEDIA_URL`| Имя path-части URL для отдачи медиа-файлов |`/media/`|

### Организация dev-среды

- создать на основе `env.override` файл `env`,
- заполнить значениями ключи, у которых нет значений по умолчанию,
- переопределить значения ключей, указанных в таблице ниже.

|       Ключ        |     Назначение     |   Должно стать   |
|-------------------|------------------|------------------|
|`DEBUG`| Режим отладки | `True` |


### Организация prod-среды

Планируется

## Установка

1. Клонировать проект:
```sh
git clone https://github.com/Padking/self-storage.git
cd self-storage
```
2. Создать каталог виртуального окружения (ВО)*,
   связать каталоги ВО и проекта,
   установить зависимости:
```sh
mkvirtualenv -p <path to python> <name of virtualenv>
setvirtualenvproject <path to virtualenv> <path to project>
pip install -r requirements.txt
```

3. Применить миграции к проекту:
```sh
python manage.py migrate
```

4. Собрать статику для проекта:
```sh
python manage.py collectstatic --clear
```

5. Применить фикстуру
```sh
python manage.py loaddata ./box/fixtures/db_data.json
```

6. Раскомментировать строчку [кода](https://github.com/Padking/self-storage/blob/f32cbf4fa5930e150ed84a39eab8d4d61b9c1465/selfstorage/box/forms.py#L20)

7. Запустить [сайт](http://127.0.0.1:8000/),

8. Осуществить переходы по страницам:
    - [аренда бокса](http://127.0.0.1:8000/box-rental/),
    - [сезонное хранение](http://127.0.0.1:8000/seasonal-keeping/)



\* с использованием [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)
