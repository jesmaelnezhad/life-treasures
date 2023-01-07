from django.urls import path

from api_server.views import index, chat_box

urlpatterns = [
    path("chat/<str:chat_box_name>/", chat_box, name="chat"),
    path("index", index, name="index")
]
