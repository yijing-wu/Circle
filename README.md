# Circle

[GO TO Circle Site](https://circle.up.railway.app/)

Deloyed on Railway

## API
Rooms information is accessable through route: `website Url+/api`

`https://circle.up.railway.app/api`

Using [Django REST framework](https://www.django-rest-framework.org/) to build the API service

## Run locally
- clone the repository
- Create a virtual environment ([virtualenv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/))
  ```bash
  # install virtualenv
  pip install virtualenv

  # create virtual environment
  virtualenv myenv

  # activate the virtual environment
  source myenv/bin/activate  # Mac only

  # install requirements
  pip install -r requirements.txt
  ```
- Change database to local
  in circle/settings.py, uncomment local database settings, comment Railway postgresql database settings

- Run the App 
  ```
  python manage.py runserver
  ```

## Todo List
- [x] Room Host should be added into Participants when room created
- [x] Redirect to room when room created
- [x] Add `enter` reminder in comments
- [x] Fix display Name, email, username
- [ ] Add photo preview when uploading files
- [x] svg icon alignment
- [x] Random avatar
- [ ] Default avatar: if avator not found, then use the default one



## ISSUES
- CSS changes no response: `command + shift + R`

## Railway Deloy Guide
[Railway Deloy Guide](/RailwayDeloyGuide.md)