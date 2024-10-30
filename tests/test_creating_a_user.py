import requests
from helpers import *
import allure

URL = "https://stellarburgers.nomoreparties.site/api/auth/register"

test_data = {
    "email": new_email,
    "password": "cool password",
    "name": "Lerochka"
}
class TestUserRegistration:

    @allure.title("Проверка возможности зарегистрировать пользователя")
    def test_user_registration(self):
        response = requests.post(URL, json=test_data)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["email"] == test_data["email"]
        assert response.json()["user"]["name"] == test_data["name"]

    @allure.title("Проверка возможности зарегистрировать уже зарегистрированного пользователя")
    def test_creating_registered_user(self):
        response = requests.post(URL, json= {"email": "test.myau@yandex.ru","password": "cool password", "name": "Lerochka"})
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "User already exists"

    @allure.title("Проверка возможности зарегистрировать пользователя без почты")
    def test_user_registration_without_email(self):
        response = requests.post(URL, json={
            "password": "cool password",
            "name": "Lerochka"
        })
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"

    @allure.title("Проверка возможности зарегистрировать пользователя без пароля")
    def test_user_registration_without_password(self):
        response = requests.post(URL, json={
            "email": "test.no_password@yandex.ru",
            "name": "Lerochka"
        })
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"

    @allure.title("Проверка возможности зарегистрировать пользователя без имени")
    def test_user_registration_without_name(self):
        response = requests.post(URL, json={
            "email": "test.no_name@yandex.ru",
            "password": "cool password"
        })
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"






