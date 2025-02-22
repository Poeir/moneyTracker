from django.contrib import admin
from django.urls import path
from moneyApp import views

urlpatterns = [
    path('',views.index),
    path('account/',views.account),
]
