import setuptools

with open('README.md') as file:
    read_my_description = file.read()

setuptools.setup(
    # Назва пакету у налаштуваннях до документації
    name= 'test-package-Group_19_30',
    # Версія пакету на момент створення файлу setup.py
    version= '1.0',
    # Вказуємо авторів створивших цей пакет
    author= 'Group_19_30',
    # Вказуємо електронну адресу автора для зв'язку з ним
    author_email= 'group_19_30@gmail.com',
    # Короткий опис пакету
    description= 'This is a test package',
    # Детальний опис пакету взятий з README.md
    long_description= read_my_description,
    # Ліцензія й компанія яка має права
    long_description_content_type = 'text/WorldIT',
    # Вказуємо посилання на наш github репозиторій
    url= 'package_github_page',
    #
    packages= ['test_package'],
    #
    classifiers= [
        'Programming Language :: Python :: 3', 
        'License :: OSI Approved :: WorldIT.academy',
        'Operating System :: OS Independent'
    ],
    #
    python_requires = '>=3.7'
)
