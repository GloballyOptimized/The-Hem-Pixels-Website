from django.urls import path
from core.views import index,about,collection,contact,services


urlpatterns = [
    path('',index),
    path('about',about),
    path('collection',collection),
    path('contact',contact),
    path('services',services),
]