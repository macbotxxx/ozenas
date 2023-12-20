from django.urls import path
from . import views

app_name = "rat"

urlpatterns = [
    path("test/", views.execute_script, name="rat-test"),
]