# Django v4 with Highcharts and Chart-JS

[![Python Version](https://img.shields.io/badge/python-3.8-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-4.0.1-brightgreen.svg)](https://djangoproject.com)

Install the requirements:
```bash
pip install -r requirements.txt

python manage.py runserver
```

The project will be available at [127.0.0.1:8000](127.0.0.1:8000)

## API's 
[http://127.0.0.1:8000/api/v1/cities/](http://127.0.0.1:8000/api/v1/cities/)

[http://127.0.0.1:8000/api/v1/browsers/](http://127.0.0.1:8000/api/v1/browsers/)

[http://127.0.0.1:8000/api/v1/rainfall/](http://127.0.0.1:8000/api/v1/rainfall/)

[http://127.0.0.1:8000/api/v1/month/](http://127.0.0.1:8000/api/v1/month/)

[http://127.0.0.1:8000/api/v1/sales/](http://127.0.0.1:8000/api/v1/sales/)

### Create User from command line
```shell
python manage.py shell
```

```shell
from django.apps import apps

# replace 'authentication' if using default user app!
User = apps.get_model('authentication', 'User')

new_user = User.objects.create(username='emmad', email='emmad@mail.com')

new_user.set_password('easy-password')

new_user.save()

```