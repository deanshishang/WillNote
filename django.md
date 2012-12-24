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

###For a full list of available settings
see the [setting reference](https://docs.djangoproject.com/en/1.4/ref/settings/)

###Creating your own settings
setting names are in all uppercase and do't reinvent an already exsiting settings
For settings are sequence, Django itself use tuples, rather than lists, this is only a convention（惯例）

###Using settings without setting DJANGO_SETTINGS_MODULE and Custom default settings
You can configure settings manually, do this by calling:
	
	django.conf.settings.configure(default_settings, **settings)

	from django.conf import settings
	settings.configure(DEBUG=Ture, TEMPLATE_DEBUG=True, TEMPLATE_DIRS=('/home/web-apps/myapp'))

Pass configure() as many keyword as you'd like, with each keyword argument representing a setting and its value, if a particular setting is not passed to configure() and is needed at some later point, django will use the default setting value

Configuring Django in this fashion is mostly necessary---and, indeed, recommended---when you are using a piece of framework inside a larger application

Custom default settings, If you'd like default values to come from somewhere other than gloabl_settings, you can pass in a module or class that provides the default settings as the default_settings argument(or as the first positional argument)in the call to configure

###Either configure() or DJANGO_SETTINGS_MODULE is required
Use exactly one of either configure() or DJNAGO_SETTINGS_MODULE. Not both, and not neither.

*****************************************************************************************************************************
