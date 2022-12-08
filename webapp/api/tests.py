from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from htmltext import find_text, format_html, gettext
import requests


# Create your tests here.


class HtmlApiTest(APITestCase):

    def test_response_correct(self):
        url = reverse(viewname='api-route')
        response = self.client.get(url, data={'url': 'https://online-edu.mirea.ru/my/'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,{
            'url': "https://online-edu.mirea.ru/my/",
            'text': [
                "Единая система аутентификации РТУ МИРЭА",
                "МИРЭА - Российский технологический университет",
                "Аутентификация пользователей",
                "Для продолжения необходима авторизация",
                "Логин:",
                "В домене ",
                "@mirea.ru",
                " или ",
                "@edu.mirea.ru",
                "Пароль:",
                "Пожалуйста, подождите...",
                "Идет авторизация на сервере.",
                "Регистрация эл. почты:",
                "для сотрудников",
                "для учащихся",
                "© 2022 МИРЭА - Российский технологический университет"
            ]
        })

    def test_response_invalid_value_1(self):
        url = reverse(viewname='api-route')
        response = self.client.get(url, data={'url': 'ladidadida'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_response_invalid_value_2(self):
        url = reverse(viewname='api-route')
        response = self.client.get(url, data={'url': 'http://google'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_response_invalid_value_3(self):
        url = reverse(viewname='api-route')
        response = self.client.get(url, data={'url': 'url'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class HtmlScriptTest(TestCase):

    def test_find_1(self):
        to_compare = [
            "Единая система аутентификации РТУ МИРЭА",
            "МИРЭА - Российский технологический университет",
            "Аутентификация пользователей"
        ]
        result = find_text(format_html(requests.get('https://online-edu.mirea.ru/my/').text))
        self.assertEqual(result[0:3], to_compare)

    def test_find_2(self):
        to_compare = [
            "​kizaru – Break Up Lyrics | Genius Lyrics",
            "Featured",
            "Charts"
        ]
        result = find_text(format_html(requests.get('https://genius.com/Kizaru-break-up-lyrics').text))
        self.assertEqual(result[0:3], to_compare)

    def test_find_3(self):
        to_compare = [
            "Mail.ru: почта, поиск в интернете, новости, игры",
            "Mail.ru",
            "Почта",
            "Мой Мир",
            "Одноклассники"
        ]
        result = find_text(format_html(requests.get('https://mail.ru').text))
        self.assertEqual(result[0:5], to_compare)
        