from django.test import TestCase
from .forms import EventForm

class EventFormTestCase(TestCase):
    def test_valid_data(self):
        form_data = {
            'title': 'テストイベント',
            'text': 'テストイベントの説明',
            'start_datetime': '2023-04-07T13:51',
            'end_datetime': '2023-04-07T14:51',
            'mail': 'test@example.com',
            'tel_number': '09012345678',
        }

        form = EventForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form_data = {
            'title': 'テストイベント',
            'text': 'テストイベントの説明',
            'start_datetime': '2023-04-07T14:51',
            'end_datetime': '2023-04-07T13:51',
            'mail': 'test@example.com',
            'tel_number': 'invalid',
        }

        form = EventForm(data=form_data)
        self.assertFalse(form.is_valid())