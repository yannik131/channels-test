from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User

class Consumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        assert User.objects.all()

