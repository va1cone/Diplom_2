import requests
import allure
URL = "https://stellarburgers.nomoreparties.site/api/orders"
URL2 = "https://stellarburgers.nomoreparties.site/api/auth/login"

class TestUserOrder:

    @allure.title("Проверка получения заказов без авторизации")
    def test_order_user_without_login(self):
        response = requests.get(URL)
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "You should be authorised"

    @allure.title("Проверка получения заказов с авторизацией")
    def test_order_user_with_login(self):
        login_response = requests.post(URL2, json={
            "email": "test.myau@yandex.ru",
            "password": "cool password"
        })
        assert login_response.status_code == 200
        access_token = login_response.json()["accessToken"]

        order_response = requests.get(
            URL, headers={"Authorization": access_token}
        )
        response = order_response.json()
        assert order_response.status_code == 200
        assert response["success"] is True
        assert "orders" in response
        assert "total" in response
        assert "totalToday" in response
