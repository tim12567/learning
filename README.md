# FirstDjango_01/12/2024
## Инструкция по развертыванию
1. python3 -m venv django_venv
2. source django_venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

## Запуск ipython в контексте приложений django
'''python manage.py shell_plus --ipython'''

## Выгрузить данные из БД
'''python manage.py dumpdata MainAPP --indent 4 > ~/projects/FirstDjango/MainAPP/fixtures/base.json
'''

## Дополнительно
1. полезное дополнение для джанго
'''
ext install batisteo.vscode-django
'''

Добавить в settings.json
'''
"emmet.includeLanguages": {
    "django-html": "html",
},
"files.associations": {
    "*.html": "django-html"
}
'''