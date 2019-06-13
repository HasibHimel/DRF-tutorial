from django.conf.urls import url
from django.urls import path

from .views import SubscriberViewSet

# app_name = "api"
#
# urlpatterns = [
#     url("subscriber/", SubscriberViewSet.as_view({'get': 'list', 'post': 'create'}), name="subscriber"),
#     url("subscriber/<int:subscriber_id>/", SubscriberViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name="subscriber"),
# ]


from rest_framework.routers import SimpleRouter

from .views import SubscriberViewSet

router = SimpleRouter()
router.register("subscribers", SubscriberViewSet)

urlpatterns = router.urls
