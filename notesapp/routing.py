from django.urls import path

from . import consumers

websocket_urlpattenrs=[
    path('ws/notes', consumers.NoteConsumer)
]