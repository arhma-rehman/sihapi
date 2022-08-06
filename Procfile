#release: python manage.py migrate
#web:waitress-serve --port=$PORT sihapi1.wsgi :application

release: python manage.py migrate
web: gunicorn sihapi1.wsgi --log-file=-
