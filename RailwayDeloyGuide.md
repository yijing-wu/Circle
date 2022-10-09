# Railway Deloy Guide

[Deploy to Railway Reference](https://dev.to/osahenru/using-railway-app-to-deploy-your-django-project-3ah1)

Develop in a virtual enviroment / docker

1. Link Database
   - add database settings in `settings.py`
    ```python
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.environ["PGDATABASE"],
            "USER": os.environ["PGUSER"],
            "PASSWORD": os.environ["PGPASSWORD"],
            "HOST": os.environ["PGHOST"],
            "PORT": os.environ["PGPORT"],
        }
    }
    ```
    can use string replace `os.environ["PGDATABASE"]` to test remote 
    database on local machine, such as `"NAME": "railway`,`
   - run `python manage.py migrate` (must replace all variables to str then run locally)
   - Railway setting: in the variables, add all database settings
  
2. `pip install gunicorn`
3. `pip freeze > requirements.txt`
4. Create a Procfile in your root folder and save the following lines of codes in it
   ```
   web: gunicorn name-of-application.wsgi
   ```
    Note: A Procfile has no file extension
5. Create `runtime.txt`
   
   Railway needs to know the version of python you used for your project, to know the version used type `python --version` in your terminal copy, paste and save the version inside your runtime.txt `python-3.8.11`
6. In settings.py file
   
   change `ALLOWED_HOST = [ ]` to `ALLOWED_HOST = ['*']`

7. In settings.py file
    ```
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    
    STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')
    ```

8. run `python manage.py collectstatic` collect static files into one folder

9. `git status`, `git add`,  `git commit -m "messages"`, `git push`


