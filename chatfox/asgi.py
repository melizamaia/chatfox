import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# importa seu routing do app "chat"
# (garanta que chat/routing.py exista e exponha websocket_urlpatterns)
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatfox.settings')

# aplicativo HTTP padrão do Django
django_asgi_app = get_asgi_application()

# ProtocolTypeRouter expõe a variável "application" — é isso que o Daphne tenta importar
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(chat.routing.websocket_urlpatterns)
    ),
})