from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from .api.views import TestUrlViewset 

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("test-rat", TestUrlViewset)


app_name = "test-api"
urlpatterns = router.urls