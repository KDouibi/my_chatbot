The purpose of this tutorial is to learn how to build a basic chatbot with Django. Then, in a second phase to improve it to include an LLM.
Easy start to test this code:
- clone the repo and run the application in the terminal: python manage.py runserver
- click into the adress generated and go to blog page, the chatbot app will appear and you can ask some first questions.

For better understanding an learning purposes, I recommend you to follow the below steps and do the exercice yourself.
First you need to :
- install Python in your machine.
- in CMD: pip install Django
- create new folder for your project and then cd to this folder and then tap: Django-admin startproject my_project
- open the project in an IDE( pycharm or visual studio of your choice)
- manage.py is the main function, and urls functions contain all urls that you want to add to your chatbot.
- every project in Django can have several apps for different purposes.
- 
To create Django first app in your project:
- in the terminal of your IDE tap: python manage.py startapp blog  (if python 3 is installed use python3)
- Models.py is very important and it allows you to create for eg. new users to the app etc.

To run your app in the browser: 
- in the terminal, python manage.py runserver, it will give you an url where your app is launched, you copy the url and in a browser paste it. or just click on the link you get.
- you will see the following view:
  ![image](https://github.com/KDouibi/my_chatbot/assets/38917244/6ecbe4eb-059d-4e1d-bbee-d7a94626e2e1)
 
To create a new url: 
- open blog app and find urls.py if not existing: create it.

from django.urls import path
from . import views
#create url
urlpatterns = [
    path('', views.index, name= 'index') #name of the url
]


References:
- https://www.youtube.com/watch?v=5AmwVXIL-zU&list=PLg4ez-XXTcoMrk0qK1dDNbKywUhh3DdVr&index=2
- 
