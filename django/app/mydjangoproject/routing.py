from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import re_path

from api_server import consumers

# URLs that handle the WebSocket connection are placed here.
websocket_urlpatterns = [
    re_path(
        r"ws/chat/(?P<chat_box_name>\w+)/$", consumers.ChatRoomConsumer.as_asgi()
    ),
]

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket":
            URLRouter(
                websocket_urlpatterns
            ),
    }
)
