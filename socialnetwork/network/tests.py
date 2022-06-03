from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Post, User


# -- coding: cp1251--

class AccountTests(APITestCase):
    def test_create_account(self):
        url = ('http://127.0.0.1:8000/api/v1/network/auth/users/')
        data = {
            "username": "user3",
            "password": "1234qwer1234",
            "email": "user3@mail.ru"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get().username, 'user3')
        self.assertEqual(User.objects.count(), 1)

    def test_create_post(self):
        url = reverse('postlist')
        data = {
            "title": "34566",
            "content": "asdfwefwefrg"
        }
        self.test_token()
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, '34566')

    def test_token(self):
        self.test_create_account()
        response = self.client.post(reverse('token_obtain_pair'), data={
            "username": "user3",
            "password": "1234qwer1234"
        }, format='json')
        self.token = response.data['access']
        self.api_authentication()

    #
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_post_view(self):
        self.test_create_post()
        response = self.client.get('http://127.0.0.1:8000/api/v1/network/post/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_like(self):
        self.test_create_post()
        response = self.client.get('http://127.0.0.1:8000/api/v1/network/postrating/1/like')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get(id=1).post_like, 1)

    def test_post_dislike(self):
        self.test_create_post()
        response = self.client.get('http://127.0.0.1:8000/api/v1/network/postrating/1/dislike')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get(id=1).post_dislike, 1)
