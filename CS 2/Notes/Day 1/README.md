<center>Day 1 Outline</center>


Frameworks:
- Java: Spring Framework
- C#: .Net Framework
- RoR: Ruby on Rails Framework
- JS: Express (NodeJS)
- PHP: Laravel Framework
- Python: Flask, Django


<b>Django</b>

Creating new django project:
```
      django-admin startproject projectname
```

Project components:
- __init__.py -> tells that we are using different python packages
- manage.py -> the heart of your application. You will be using it to run scripts.
- settings.py -> all of the settings (timezones, applications, databases,...)
- urls.py -> determines all urls of your apps and connects to the corresponding functions
- wsgi.py, asgi.py -> deployment file


Creating django application:

```
  python manage.py startapp appname
```

Adding function to views.py of your project

```
  from django.http import HttpResponse
  def index(request):
    return HttpResponse("Hi there!")
```

Creating new appname/urls.py file inside of a new application:

```
  from django.urls import path
  from . import views
  urlpatterns = [
    path("url",views.index),

  ]

```

Link all urls.py files ()

```
  from django.urls import path, include
  path('url', include('appname.urls'))

```

Tell Django about new app (settings.py):

```
  INSTALLED_APPS += 'app'
```

Run server
```
  python manage.py runserver
```


models.py -> databases

```

  class Person(models.Model):
    name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    age = models.IntegerField()

```

Migrations will make everything for us:

```
  python manage.py makemigrations #take care of all changes
  python manage.py migrate #application of all changes

```

Django Shell:

```
  python manage.py shell
```

Saving to Database (while in django shell):

```
  from appname.models import *
  a = Person(name = 'Daniyar', last_name = 'Au', age = 22)
  a.save() # save an entry to database
```

Accessing database:

```
  from appname.models import *
  people = Person.objects.all()
  print(me)

```

```
  class Country(models.Models):
    name = models.CharField(max_length = 60)

  class Person(models.Model):
    name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    age = models.IntegerField()
    country = models.ForeignKey(Country, on_delete = models.CASCADE, related_name = 'countries')
```

Add templates directory in settings file

```
  'DIRS': ['templates'],
```



Templates:
```
  def main(request):
    context = {
      'people': Person.objects.all()
    }
    return render(request, 'appname/index.html', context)
```

Admin:

```
  from .models import *
  admin.site.register(Person)
  admin.site.register(Country)

```

Create superuser:

```
  python manage.py createsuperuser
```


customizing urls:

```
  path('<int:my_number>', views.foo)
```


# HW 1 (Aug 19)

```
Part 1. Any application. Have buttons (I will not manually type any URLs) everywhere.

- Add entry
- Get entry by id
- Get entry by name
- Delete entry by id
- Filter by /something/


```