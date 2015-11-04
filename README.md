This project is here to illustrate my how to of django i18n articles that you can read here.

* [Dive into Django i18n part 1](http://www.metod.io/blog/2015/05/05/django-i18n-part-1/)
* [Dive into Djanjo i18n part 2](http://www.metod.io/blog/2015/07/22/dive-django-i18n-part-2/)

# Getting Started

You will need to have pip and virtualenv installed to make it work. In a debian/ubuntu environment this is achieved by:

    sudo apt-get install python-pip
    sudo pip install virtualenv

After that, you will need to do these commands:

    git clone https://github.com/Fenntasy/dive-into-django-i18n.git
    cd dive-into-django-i18n
    virtualenv .
    source bin/activate
    pip install -r requirements.txt
    cd your_project
    export SECRET_KEY='YOUR_SECRET_KEY'

Write your database settings in your_project/your_project/database.py like this
	
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2',
	        'NAME': 'your_db_name',
	        'USER' : 'your_db_user',
	        'PASSWORD' : 'your_db_password',
	        'HOST' : 'your_db_host',
	        'PORT' : '5432',
	    }
	}

And finally install your models in the database

    python manage.py migrate

This repository will have tags that matches the articles counterparts and are name part-#
