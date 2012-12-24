#The development process

##django settings

###default settings
	
	/django/conf/gloable_settings.py

###Seeing which settings you have changed

	python manage.py diffsettings

###Using settings in Python code
In your Django apps, using settings by import object django.conf.settings

 	from django.conf import settings
	if settings.DEBUG:
		#do something
	
###Alter settings at runtime
Your should not alter settings in your application at runtime, do not do this in a view.

 	from django.conf import settings
	settings.DEBUG = True

The only place you should assign to settings is in a settings file.

###Security
A settings files contains sensitive infomation, such as the database passwd, you should make every attempts to limit access to it. for example, change its file pemission so that only you and your webserver's, user can read it.
