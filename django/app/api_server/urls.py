from django.urls import path

from api_server.views import index

urlpatterns = [
    path("index", index, name="index")
]
