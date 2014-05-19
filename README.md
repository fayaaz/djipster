djipster
========

Website to show off artist's work using the Django web framework.

Installation
--------------

Install and run like a django project:

1. Install requirements with `pip install -r requirements.txt` (you may have problems with pillow on Windows, in which case it can be installed from here: http://www.lfd.uci.edu/~gohlke/pythonlibs/)
2. From the root folder run:`python manage.py syncdb`
3. Because this app is using South, run `python manage.py schemamigration artSite --initial` and then `python manage.py migrate artSite`
4. Run the development server: `python manage.py runserver 8080`

Built on
--------------
Built with Django, Grapelli, Twitter Bootstrap and Grayscale theme.

Made for Joe and Pete
