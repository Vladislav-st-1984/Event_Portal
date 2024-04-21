from locust import HttpUser, task, constant_throughput
from pyquery import PyQuery


class LocustTest(HttpUser):
    wait_time = constant_throughput(2)

    @task(10)
    def login_page(self):
        response = self.client.get("/magazine/login")

        pq = PyQuery(response.text)
        csrf_token = pq('input[name="csrfmiddlewaretoken"]').attr("value")

        self.client.headers["X-CSRFToken"] = csrf_token

    @task(1)
    def login_users(self):
        username = "obraz"
        password = "Qwerty_123"

        self.client.post(
            '/magazine/login/',
            {
                'username': username,
                'password': password,

            },
            headers={
                'X-CSRFToken': self.client.headers["X-CSRFToken"],

            })
