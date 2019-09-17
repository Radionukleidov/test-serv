from locust import HttpLocust, TaskSet, task
import requests as r

"""
For https://tritonshoes.ru
locust -f locust_files/my_first_locust.py --host=https://tritonshoes.ru

"""

base_url = 'https://tritonshoes.ru'


def login(l):
    l.client.post("/account/login", {"LoginForm[username]": "123123", "LoginForm[password]": "123123"})
    response = r.post(base_url + "/account/login", {"LoginForm[username]": "123123", "LoginForm[password]": "123123"})
    print("Login response - ", response.status_code, response.reason)


def logout(l):
    l.client.post("/account/logout", {"LoginForm[username]": "123123", "LoginForm[password]": "123123"})
    response = r.post(base_url + "/account/logout", {"LoginForm[username]": "123123", "LoginForm[password]": "123123"})
    print("Logout response - ", response.status_code, response.reason)


class UserBehavior(TaskSet):
    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)

    @task(1)
    def main_page(self):
        self.client.get("/")

    @task(2)
    def questions(self):
        self.client.get("/pages/chastye_voprosy")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
