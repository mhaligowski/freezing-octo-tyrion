web: django-admin.py collectstatic --noinput; gunicorn_django --workers=4 --bind=0.0.0.0:$PORT src/tyrion/settings/heroku.py
