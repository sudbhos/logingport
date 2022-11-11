
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
   path("",views.home,name="home"),
   path("java",views.java,name='java'),
   path("pytho",views.pytho,name="pytho"),
   path('sql',views.sql,name="sql"),
   path('singi',views.singi,name="singi"),


]
