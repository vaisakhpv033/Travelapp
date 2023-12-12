from . import views
from django.urls import path

app_name = 'registerapp'

urlpatterns = [
    path('', views.demo, name="demo")
]
