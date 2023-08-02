# Recipe Book API

Recipe Book is a recipe-sharing site where foodies can share their favourite meals with other members of the community. With the ability to comment and like posts users are encouraged to engage with each other and share their love of food.

- Deployed HEROKU frontend project: [https://ajw-recipe-book.herokuapp.com/](https://ajw-recipe-book.herokuapp.com/)
- Deployed HEROKU backend API: [https://ajw-recipe-book-api.herokuapp.com/](https://ajw-recipe-book-api.herokuapp.com/)
- GitHub repository frontend: [https://github.com/AlexanderJWard/recipe-book/](https://github.com/AlexanderJWard/recipe-book/)

## Table of Contents
+ [User Stories](#user-stories "User Stories")
+ [Database](#database "Database")
+ [Testing](#testing "Testing")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Technologies Used](#technologies-used "Technologies Used")
  + [Main Languages Used](#main-languages-used "Main Languages Used")
+ [Deployment](#deployment "Deployment")
+ [Credits](#credits "Credits")
  + [Content](#content "Content")
  + [Media](#media "Media")

## User Stories:

Here are the links to my [kanban board](https://github.com/users/AlexanderJWard/projects/4) and the user stories hosted in [Github issues](https://github.com/AlexanderJWard/recipe-book/issues)

## Database:

I used the following models in my database:

- User
- Profile
- Likes
- Comment
- Posts
- Todo
- Followers

## Testing:
### Validator Testing: 

Tested in Gitpod problems, PEP 8 online tester contradicted the GitPod problems section.
![image](https://github.com/AlexanderJWard/recipe-book-api/assets/102811792/a2896371-44db-4f44-8a0a-82ca4defdd23)

### Manual Testing:
1. Verified CRUD for each relevant database components
2. Check links and URLS go to the correct places
3. Test 404 page for incorrect links
4. Check search filter works for posts
5. Create user using admin console and create superuser using CLI
6. Test makemigrations and migrate commands

### Unfixed Bugs

None found currently

## Technologies Used:
### Main Languages Used:
- Python

### Frameworks, Libraries & Programs Used:
- Django
- Django RestFramework
- Cloudinary
- Heroku
- Pillow
- Django Rest Auth
- PostgreSQL
- Cors Headers

## Deployment:
### Creation:

1. Start new GitHub repository
2. Start new Heroku project
3. Install Postgres to Heroku via resources
4. Lauch repository in GitPod and install the following using pip install
   - django<4
   - dj3-cloudinary-storage
   - pillow
   - djangorestframework
   - django-filter
   - dj-rest-auth
   - djangorestframework-simplejwt
   - dj_database_url psycopg2
   - gunicorn
   - django-cors-headers
5. Start Django project using startproject __project_name__ .
6. Add config vars into Heroku:
   - SECRET_KEY = Randomized hidden key
   - CLOUDINARY_KEY = cloudinary://YOUR_UNIQUE_KEY
   - DISABLE_COLLECTSTATIC = 1
   - ALLOWED_HOST = UNIQUE_PROJECT_NAME.herokuapp.com
7. Add two config vars same as in the frontend Heroku remembering to remove trailing /
   - CLIENT_ORIGIN = https://react-app-name.herokuapp.com
   - CLIENT_ORIGIN_DEV = https://gitpod(UNIQUE LINK).io
8. Create env.py file and add the following
   - import os
   - os.environ["CLOUDINARY_URL"] = "cloudinary://YOUR_UNIQUE_KEY"
   - os.environ["DATABASE_URL"] = "postgres://YOUR_UNIQUE_URL"
   - os.environ["SECRET_KEY"] = "YOUR_UNIQUE_KEY"
   - os.environ["ALLOWED_HOST"] = "YOUR_UNIQUE_GITPOD_BROWSER_URL.gitpod.io"

### Settings.py: 

1. Add the following INSTALLED_APPS
    - 'django.contrib.admin',
    - 'django.contrib.auth',
    - 'django.contrib.contenttypes',
    - 'django.contrib.sessions',
    - 'django.contrib.messages',
    - 'cloudinary_storage',
    - 'django.contrib.staticfiles',
    - 'cloudinary',
    - 'django_filters',
    - 'rest_framework.authtoken',
    - 'dj_rest_auth',
    - 'django.contrib.sites',
    - 'allauth',
    - 'allauth.account',
    - 'allauth.socialaccount',
    - 'dj_rest_auth.registration',
    - 'corsheaders',
    - 'rest_framework',
  
![image](https://github.com/AlexanderJWard/recipe-book-api/assets/102811792/a5cfa40c-3943-413e-8712-641abe7e44d4)

2. Import database in settings.py with the following:
![image](https://github.com/AlexanderJWard/recipe-book-api/assets/102811792/5fdbcef3-4123-4a54-a126-a1deffe959d4)

3. Add the Cloudinary storage settings:
![image](https://github.com/AlexanderJWard/recipe-book-api/assets/102811792/4066f42f-c9a1-4b7a-9270-62881f79f25f)

4. Below INSTALLED_APPS add the __SITE_ID = 1__
![image](https://github.com/AlexanderJWard/recipe-book-api/assets/102811792/40e64699-696d-4535-8b43-962a91db86d3)

5. Underneath BASE_DIR add the __REST_FRAMEWORK__
![image](https://github.com/AlexanderJWard/recipe-book-api/assets/102811792/16a50850-027b-40c0-ba92-e67ea78b19df)

6. Below that add the __JWT_AUTH__ settings
![image](https://github.com/AlexanderJWard/recipe-book-api/assets/102811792/7d46118a-13f3-49ed-b780-7686d65937c2)

7. Add __DEBUG__ and edit the __DATABASES__
![image](https://github.com/AlexanderJWard/recipe-book-api/assets/102811792/7ea8b47e-fe66-4b9c-ba27-550533c26eff)

![image](https://github.com/AlexanderJWard/recipe-book-api/assets/102811792/52d9548b-9688-442e-b032-0a4fd1b23dcd)

8. Add the __ALLOWED_HOST__ variable for Heroku as well as the __CORS__ settings.
![image](https://github.com/AlexanderJWard/recipe-book-api/assets/102811792/11bb62be-3671-417c-9f3e-cdb6846351cd)

![image](https://github.com/AlexanderJWard/recipe-book-api/assets/102811792/0d1baf63-400b-415b-9188-f5af003919c4)

9. Edit the __MIDDLEWARE__
![image](https://github.com/AlexanderJWard/recipe-book-api/assets/102811792/ef00f61f-94ac-431d-b9ac-84453b80b50b)

### Additional steps:

1. Create a Procfile with the following settings:

- release: python manage.py makemigrations && python manage.py migrate
- web: gunicorn recipe_book_api.wsgi

2. Run the following commands to make migrations
- python3 manage.py makemigrations
- python3 manage.py migrate

3. Update requirements.txt with the following:
- pip3 freeze --local > requirements.txt

4. Add, commit and push changes

5. Finally, Go to Heroku and deploy to GitHub repository

## CREDITS:

### Content:
- Steps for creating this API was provided by Code Institute DRF-API walkthrough project

### Media:
- Default post image from Code Institute DRF-API walkthrough
- Default profile image from Code Institute DRF-API walkthrough
