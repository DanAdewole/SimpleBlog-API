from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

from .views import PostListCreateView


User = get_user_model()


class HelloWorldTestCase(APITestCase):
    def test_hello_world(self):
        response = self.client.get(reverse("posts_home"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Hello")


class PostListCreateTestCase(APITestCase):
    """want to use test client, no need to setup data again"""

    def setUp(self):
        #     self.factory = APIRequestFactory()
        #     self.view = PostListCreateView.as_view()
        self.url = reverse("list_posts")
        # self.user = User.objects.create(
        #     first_name="Dan",
        #     last_name="Ade",
        #     email="dan@gmail.com",
        #     password="password123456",
        # )

    def authenticate(self):
        self.client.post(
            reverse("signup"),
            {
                "email": "dan@gmail.com",
                "password": "password123456",
                "first_name": "Dan",
                "last_name": "Ade",
            },
        )
        response = self.client.post(
            reverse("login"),
            {
                "email": "dan@gmail.com",
                "password": "password123456",
            },
        )
        # print(response.data)
        token = response.data["token"]["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_list_posts(self):
        """using normal method"""
        # request = self.factory.get(self.url)

        """using client method"""
        response = self.client.get(self.url)
        # response = self.view(request)
        # print(response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
        self.assertEqual(response.data["results"], [])

    def test_post_creation(self):
        self.authenticate()

        sample_data = {
            "title": "Sample title",
            "content": "Sample Content",
        }
        response = self.client.post(reverse("list_posts"), sample_data)
        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], sample_data["title"])

        """using previous setting up method"""
        # sample_post = {"title": "Sample post", "content": "Sample content"}
        # request = self.factory.post(self.url, sample_post)
        # request.user = self.user

        # response = self.view(request)
        # # print(response.data)

        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
