
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import UserActivityLog

class ActivityLogTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_log(self):
        data = {"action": "LOGIN", "metadata": {"ip": "127.0.0.1"}}
        response = self.client.post("/api/logs/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_list_log(self):
        UserActivityLog.objects.create(user=self.user, action="LOGIN")
        response = self.client.get(f"/api/logs/{self.user.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_status(self):
        log = UserActivityLog.objects.create(user=self.user, action="UPLOAD_FILE")
        response = self.client.patch(f"/api/logs/update/{log.id}/", {"status": "DONE"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "DONE")
