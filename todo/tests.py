from django.test import TestCase
from django.urls import reverse
from .models import Schedules


class ToDoAppTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.schedule = Schedules.objects.create(
            title='Good title.'
        )

    def test_schedule_model(self):
        self.assertEqual(self.schedule.title, 'Good title.')
        self.assertEqual(str(self.schedule), 'Good title.')

    def test_homepageview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/home.html')
        self.assertContains(response, 'Schedule list')

    def test_editpageview(self):
        response = self.client.get('/schedule/1/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/schedule_edit.html')
        self.assertContains(response, 'Update')

    def test_schedule_deletepageview(self):
        response = self.client.post(reverse('schedule_delete', args='1'))
        self.assertEqual(response.status_code, 302)
