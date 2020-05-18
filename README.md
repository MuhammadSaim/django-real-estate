# Django Real Estate

![Django Real Estate](https://i.ibb.co/WskK7dL/screencapture-127-0-0-1-8000-2020-05-18-20-27-59.png)

 ## Dependencies
- Django 3
- Postgres SQL

## Configurations

Install dependencies

```shell script
$ pipenv install
```

In <kbd>djReal/settings.py</kbd> add your database configurations

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dj_real',
        'USER': 'postgres',
        'PASSWORD': 'muhammadsaim',
        'HOST': 'localhost'
    }
}
```

after that run migration

```shell script
$ python manage.py migrate
```

Good to go Happy Django