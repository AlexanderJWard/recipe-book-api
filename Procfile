release: python manage.py makemigrations && python manage.py migrate
web: gunicorn recipe_book_api.wsgi