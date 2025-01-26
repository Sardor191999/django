from django.urls import path
from .views import first_view, second_view, pages

urlpatterns = [
    path('',first_view, name='first_page'),
    path('second/',second_view, name='second_page'),
    path('pages/<str:page>',pages, name='pages'),
]
