## Base commands
### Migration commands
- reset all apllied migrations <br>
`python manage.py migrate main zero`
- add new empty migration <br>
`python manage.py makemigrations --empty main`
- check changes made in models/migrations <br>
`python manage.py makemigrations `
- aplly new migrations/ changes in migrations <br>
`python manage.py migrate `
### Application commands
- run app <br>
`python  manage.py runserver `
### Users commands
- create admin user <br>
`python manage.py createsuperuser`
