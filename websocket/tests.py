from django.test import TestCase
from channels_test.routing import application
from channels.testing import WebsocketCommunicator
from django.contrib.auth.models import User
import pytest

class Tests(TestCase):
    def setUp(self):
        User.objects.create_user(username='test')

    @pytest.mark.asyncio
    @pytest.mark.django_db(transaction=True)
    async def test_connect(self):
        communicator = WebsocketCommunicator(application, '/ws/test/')
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        await communicator.disconnect()

    async def test_connect_without_pytest(self):
        communicator = WebsocketCommunicator(application, '/ws/test/')
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        await communicator.disconnect()
        
