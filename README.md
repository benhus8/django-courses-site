# Educational Application

## Description

The Educational Application is a web platform based on the Django framework, designed to facilitate the management of online courses. It allows users to fully utilize education-related functions, including registration, access to various courses, profile editing, adding courses to their account, and tracking learning progress.

## Key Features

### Pages and Views

- **Home Page**: Contains general information and is accessible after logging in.
- **User Registration**: Allows new users to join the educational community.
- **Login/Logout**: Secure login and logout from the system.
- **User Profile**: Access to and editing of user information.
- **Available Courses**: Browse and select courses available to the user.
- **Course Addition**: Ability to add new courses to the user's account.
- **Course Deletion**: Option to remove courses from the user's account.

## Base Commands
### Migration Commands
- Reset all applied migrations <br>
`python manage.py migrate main zero`
- Add new empty migration <br>
`python manage.py makemigrations --empty main`
- Check changes made in models/migrations <br>
`python manage.py makemigrations `
- Apply new migrations/ changes in migrations <br>
`python manage.py migrate `
### Application Commands
- Run app <br>
`python  manage.py runserver `
### Users Commands
- Create admin user <br>
`python manage.py createsuperuser`

## Workflow
### Branches
- The main branch is develop. From this branch, we create feature branches and all other types of branches. When the project is done or we are confident that everything is working fine, we can merge it to master.
### When Feature Branch Is Done
- When your job is done and you've committed and pushed all your changes, you should create a pull request. The second person will check if everything is working fine, and after that, the second person can merge your feature branch to develop.
