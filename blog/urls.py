from django.urls import path
from . import views

#create url
urlpatterns = [
    path('', views.index, name='index'),#name of the url
    path('specific', views.specific, name='specific'),
    #path('article/<int:article_id>', views.article2, name= 'article' )
    path('getResponse', views.getResponse, name='getResponse')
]

