# Blog Application

In this project, I have done a blog application with user authentication. This project is built using the Django web framework. It allows users to register, log in, create, read, update, and delete blog posts. The application includes user authentication to ensure that only authenticated users can create, update, or delete posts. Also, it enforces that only the author of a post can modify or delete their post. This application demonstrates the core functionalities of a blog system while ensuring basic security and user permissions.

## Setup

```bash
create a database in XAMPP named as blog_db 
open the code in visual studio code 
open the terminal
open cmd
In cmd create a virtual enviorment ( mkvirtualenv env )
Activate the virtual enviorment ( workon env )
Migrate the model by:
python manage.py makemigrations
python manage.py migrate
Run the project by:
python manage.py runserver
```