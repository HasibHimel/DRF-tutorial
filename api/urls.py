from django.conf.urls import url
from django.urls import path

from .views import SubscriberView

app_name = "api"

urlpatterns = [
    url("subscriber/", SubscriberView.as_view(), name="subscriber"),
]
