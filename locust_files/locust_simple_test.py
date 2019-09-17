from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    # runs one time for each user
    def on_start(self):
        self.client.get("/")

    @task(2)  # chance to run 2/3
    def posts(self):
        self.client.get("/posts")

    @task(1)  # chance to run 1/3
    def comment(self):
        data = {
            "postId": 1,
            "name": "my comment",
            "email": "test@user.test",
            "body": "Author is cool. Some text. Hello world!"
        }
        self.client.post("/comments", data)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000
