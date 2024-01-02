from django.urls import path

from .views import register, login, home

urlpatterns = [
    path('', register, name='register'),
    path('login/', login, name='login'),
    path('home/', home, name='home')

]
