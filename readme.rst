=====
Simple CRM
=====



Quick start
-----------

1. Add "simplecrm" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'simplecrm',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('accounts/', include('accounts.urls')),

3. Run `python manage.py migrate` to create the simplecrm models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   

