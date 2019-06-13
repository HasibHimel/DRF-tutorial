from django.conf.urls import url, include
from django.urls import path

from django.contrib import admin

#from api import urls as api_urls

urlpatterns = [
    url('api/', include("api.urls")),
    url('admin/', admin.site.urls),
]
