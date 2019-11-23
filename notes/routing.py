from channels.routing import ProtocolTypeRouter, URLRouter
import notesapp.routing
from channels.auth import AuthMiddlewareStack
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            notesapp.routing.websocket_urlpattenrs
        )
    )
})