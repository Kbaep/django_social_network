from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Post,User
# -- coding: cp1251--

class AccountTests(APITestCase):
    # def setUp(self):
    #     # создайте нового пользователя, отправив запрос к конечной точке djoser
    #     self.user = self.client.post('http://127.0.0.1:8000/api/v1/network/auth/users/', data={
    #         "username": "user2",
    #         "password": "1234qwer1234",
    #         "email": "user2@mail.ru"
    #     })
    #     # получить веб-токен JSON для вновь созданного пользователя
    #     response = self.client.post('http://127.0.0.1:8000/api/v1/network/token', data={
    #         "username": "user2",
    #         "password": "1234qwer1234"
    #     })
    #     self.token = response.data['access']
    #     self.api_authentication()
    #
    # def api_authentication(self):
    #     self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
    #
    def test_create_post(self):
        url = reverse('postlist')
        data = {
            "title": "34566",
            "content": "asdfwefwefrg"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Post.objects.count(), 1)
    #     self.assertEqual(Post.objects.get().title, '34566')

    def test_create_account(self):
        url = ('http://127.0.0.1:8000/api/v1/network/auth/users/')
        data = {
            "username": "user3",
            "password": "1234qwer1234",
            "email": "user3@mail.ru"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(User.objects.all())