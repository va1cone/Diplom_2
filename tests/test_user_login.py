import requests
import allure

URL = "https://stellarburgers.nomoreparties.site/api/auth/login"

class TestUserLogin:

    @allure.title("Проверка возможности авторизировать пользователя")
    def test_user_login(self):
        response = requests.post(URL, json={
            "email": "test.myau@yandex.ru",
            "password": "cool password",
            "name": "Lerochka"
        })
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["email"] == "test.myau@yandex.ru"
        assert response.json()["user"]["name"] == "Lerochka"

    @allure.title("Проверка возможности авторизировать пользователя с некорректным паролем")
    def test_user_login_with_incorrect_password(self):
        response = requests.post(URL, json={
            "email": "test.myau@yandex.ru",
            "password": "cool password1123456"
        })
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Проверка возможности авторизировать пользователя с некорректной почтой")
    def test_user_login_with_incorrect_email(self):
        response = requests.post(URL, json={
            "email": "test.myauqq@yandex.ru",
            "password": "cool password"
        })
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Проверка возможности авторизировать пользователя с некорректным паролем и почтой")
    def test_user_login_with_incorrect_email_and_password(self):
        response = requests.post(URL, json={
            "email": "test.myauqq@yandex.ru",
            "password": "cool password111"
        })
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Проверка возможности авторизировать пользователя без почты")
    def test_user_login_without_email(self):
        response = requests.post(URL, json={
            "password": "cool password"
        })
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Проверка возможности авторизировать пользователя без пароля")
    def test_user_login_without_password(self):
        response = requests.post(URL, json={
            "email": "test.myauqq@yandex.ru"
        })
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"