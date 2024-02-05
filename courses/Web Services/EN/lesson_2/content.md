## What is a web framework

A web framework is a set of tools that help your code translate neatly onto something that can process HTTP requests and
return HTTP responses.

Django is one of the most popular Web Frameworks for Python, and the main reason for that is that it comes integrated
with a vast library of tools.

Django is capable to fulfill 2 very important use-cases for a web-service:

* Handling Data storage with an easy to set-up database integration
* Export the data using very simple decorators.

To help us in our adventure into the web, besides Django, we will need another framework called Django Rest Framework
(DRF).

## Installing Django and DRF

If Python and a virtual environment (venv) are already set up on your system, setting up a project with Django and
Django Rest Framework (DRF) is straightforward. Follow these steps:

1. **Install Django:**
   With your virtual environment activated, install Django using pip:
   ```
   pip install django
   ```

2. **Create a Django Project:**
   After installing Django, create a new Django project by running the following command:
   ```
   django-admin startproject myproject
   ```
   Replace `myproject` with the name of your Django project.

3. **Navigate to the Project Directory:**
   Change into the project directory that was just created:
   ```
   cd myproject
   ```

4. **Create a Django App:**
   Django projects are composed of one or more apps. Create a new Django app within your project by running:
   ```
   python manage.py startapp myapp
   ```
   Replace `myapp` with the name of your Django app.

5. **Install Django Rest Framework (DRF):**
   Now that Django is set up, install Django Rest Framework using pip:
   ```
   pip install djangorestframework
   ```

6. **Configure Settings:**
   Open the `settings.py` file in your Django project (`myproject/settings.py`) and add `'rest_framework'` to
   the `INSTALLED_APPS` list:
   ```python
   INSTALLED_APPS = [
       ...
       'rest_framework',
   ]
   ```

7. **Create Django Models, Views, and URLs:**
   Define your Django models, views, and URL patterns as needed for your project and app. Refer to the Django and DRF
   documentation for guidance on creating models, views, serializers, and URLs.

8. **Run Migrations:**
   Apply migrations to create database tables based on your models:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

9. **Start the Django Development Server:**
   Start the Django development server to run your project locally:
    ```
    python manage.py runserver
    ```

10. **Test Your Django Project:**
    Open a web browser and navigate to `http://127.0.0.1:8000` to access your Django project. If everything is set up
    correctly, you should see the Django welcome page.

That's it! You have set up a Django project with Django Rest Framework (DRF) in your Python virtual environment. You can
now start building your web application and RESTful APIs using Django and DRF. Remember to refer to the Django and DRF
documentation for detailed usage instructions and best practices.

## Django Components

Django comes built-in with many features, one most notable is the ORM and the second one is the Views. Combining the
power of them together we are able to easily define our data and operate with it.

Django follows the MVC design patern, this is why you will often see the `models` and `views` modules in Django
Projects.

### The ORM

An ORM - Object Relation Mapper, provides a simple way for us to describe our data as a Python Object, and the ORM
itself
will take care of translating this information into a Database Object and integrate it directly with the database
capabilities.

This allows us to write code like this:

```python
from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

```

The class above defines a Customer model, which would be processed by the ORM to have it work with our database.

### Migrations

A crucial part about working with database is making sure that the information (or structure) of our database is the
same as the data structure of our Python Objects. This introduces the concept of Migrations.

Migrations allow us to build instructions that tell the database how it should look like, based on our python objects,
and the **best** part is that Django takes care of this by itself.

All we have to do, after we have introduced a new object or have made changes to an existing model is to run the
commands:

```
python manage.py makemigrations # This will create the migrations
python manage.py migrate # This will update the databse with the migrations
```

## The views

Django Views, are basically pages or resources on your web-service, and as any web resource, it is easy to get them to
work, because all you have to do is to register a URL (or what is called a **route**) and point it to your view
function.

Your view function should look similar to this:

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def hello_world(request):
    data = {'message': 'Hello, world!'}
    return Response(data)
```

And your urls module should register the new route similar to how its done below:

```python
from django.urls import path
from .views import hello_world

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
]
```

You can create as many views as you like, and the best part, is that your views are automatically connected to your
database, this means that you can perform database operations right inside your views.

```python
# part of the same views.py file
@api_view(['GET'])
def get_customers(request):
    all_customers = Customer.objects.all()
    data = []
    for customer in all_customers:
        data.append(
            dict(
                id=customer.id,
                fist_name=customer.first_name,
                last_name=customer.last_name,
                email=customer.email,
                phone_number=customer.phone_number,
            )
        )
    json_data = json.dumps(data)
    return Response(json_data)


@api_view(['POST'])
def add_customer(request):
    customer_data = request.data  # a dict with the request body
    new_customer = Customer.objects.create(
        first_name=customer_data['first_name'],
        last_name=customer_data['last_name'],
        email=customer_data['email'],
        phone_number=customer_data['phone_number'],
    )
    json_data = json.dumps({
        'id': new_customer.id,
        'first_name': new_customer.first_name,
        'last_name': new_customer.last_name,
        'email': new_customer.email,
        'phone_number': new_customer.phone_number
    })
    return Response(json_data)
```

## Full example

You can find the full example if you follow the this [link](https://github.com/mtricolici98/djangoTemplate).

To set up the example, all you need to do is to clone the project, and open it in Pycharm.

1. Create a virtualenv (using Pycharm)
2. Install the requirements using `pip install -r requirements.txt`
3. Run the migrations using `python manage.py migrate`
4. Run the project using `python manage.py runserver`

Now if you navigate to: http://localhost:8000/customer/all/ in your browser, you will see all your customers, and if you
access http://localhost:8000/customer/add/ you will be able to create a new customer by providing the JSON data.

```json
{
  "first_name": "Marius",
  "last_name": "Tricolici",
  "email": "email@mail.com",
  "phone_number": "123123123"
}'
```

## Continue Reading

Continue getting accustomed to django using the resources below:

* DRF Views: https://www.django-rest-framework.org/api-guide/views/#api_view
* Django Models: https://docs.djangoproject.com/en/5.0/intro/tutorial02/
