# Aplikacja Edukacyjna

## Opis

Aplikacja Edukacyjna to platforma internetowa oparta na frameworku Django, stworzona do ułatwiania zarządzania kursami online. Pozwala użytkownikom na pełne korzystanie z funkcji związanych z edukacją, rejestrację, dostęp do różnych kursów, edycję profilu, dodawanie kursów do swojego konta oraz śledzenie postępu w nauce.

## Funkcje Kluczowe

### Strony i Widoki

- **Strona Główna**: Zawiera informacje ogólne i jest dostępna po zalogowaniu.
- **Rejestracja Użytkownika**: Umożliwia nowym użytkownikom dołączenie do społeczności edukacyjnej.
- **Logowanie/Wylogowywanie**: Bezpieczne logowanie i wylogowywanie z systemu.
- **Profil Użytkownika**: Dostęp do i edycja informacji o użytkowniku.
- **Dostępne Kursy**: Przegląd i wybór kursów dostępnych dla danego użytkownika.
- **Dodawanie Kursu**: Możliwość dodawania nowych kursów do konta użytkownika.
- **Usuwanie Kursu**: Opcja usuwania kursów z konta użytkownika.





















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

## Workflow
### Branches
- Main branch is develop. From this branch we create feature branches and all other types of branches. When The project is done or we are confident that everything is work fine we can merge it to master.
### When feature branch is done
- When your job is done and you commited and pushed your all changes you should create pull request. Second person will check if everything is working fine and after that second person can merge your feature branch to develop.
