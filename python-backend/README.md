# Setup
1. install with `pip install loguru python-dotenv psycopg2 django djangorestframework djoser djangorestframework_simplejwt django-filter drf-yasg django-cors-headers==3.5.0` or use `pip install -r requirements.txt`
2. Create from backend/example.env => backend/.env with yours settings 
3. from backend/ run server `python manage.py migrate` and `python manage.py runserver`
 
Go to `./swagger/` to read the API full documentation

# Auth methods
1. Use `post` - `/auth/token/login/` - `{username: '', password: ''}` for log in and getting your auth token
2. Use `post` - `/auth/token/logout/` for out and deactivate token
3. Use `post` - `/auth/users/` - `{username: '', password: '', email: ''}` for create new user and send code on his email
4. Use `post` - `/auth/users/activation/` - `{uid: '', token: ''}` for activate new user (link from his email)

### JWT Auth
1. Use `post` - `/api/token/` - `{username: '', password: ''}` for log in and getting your auth tokens (pair)
2. Use `post` - `/api/token/refresh/` - `{refresh: 'your refresh token'}` to refresh access token


Also provided filter params `/?date_after=****-*-*&date_before=****-*-*` to filter rezult by added date