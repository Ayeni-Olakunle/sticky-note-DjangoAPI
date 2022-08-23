web: gunicorn stickynote.wsgi
releases: python manage.py makemigrations --noinput
releases: python manage.py collectstatic --noinput
releases: python manage.py migrate --noinput