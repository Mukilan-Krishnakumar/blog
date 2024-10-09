from django.urls import path
from blogs.views import health

urlpatterns = [path("health/", health, name="health")]
