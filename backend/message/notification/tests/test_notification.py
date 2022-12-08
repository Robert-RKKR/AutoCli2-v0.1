# Django import
from django.test import TransactionTestCase

# Application import:
from messages.notifications.notification import Notification
from network.inventory.models.device import Device


# Test classes:
class TestNotification(TransactionTestCase):

    def test_notification_creation(self):

        # Create test device:
        test_device = Device.objects.create(
            name='chsthrtrlab1',
            hostname='10.1.1.1'
        )

        # Create new notification object:
        notification = Notification()
        # Create a new notification:
        notify = notification.send('Test notification', **{
            'object': test_device,
        })

        # Check result:
        assert notify.message == 'Test notification'
