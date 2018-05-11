=====
Simple CRM
=====

Requirements
------------
Django v1.11.7
django-unixdatetimefield v0.1.6
psycopg2 v 2.7.4  (if using a Postgresql db, also works with MySQL) 

Quick start
-----------

1. Add "simplecrm" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
		bootstrap3_datetime
        'simplecrm',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('accounts/', include('accounts.urls')),

3. Run `python manage.py migrate` to create the simplecrm models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   
Other Notes
-----------
Some of the models do have foreign key relationships.
I had reasons to do it this way at first. However, In the newest build, 
I have added them and I will be updating the form processing views to reflect that.
