from django.conf.urls import url
from django.urls import path

from .views import hello_world

app_name = "api"

urlpatterns = [
    url("hello/", hello_world, name="hello_world"),
]
