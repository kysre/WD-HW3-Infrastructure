from locust import HttpUser, between, task


HOST_NAME = 'localhost:8000'


class LoadTestUser(HttpUser):
    @task
    def api(self):
        self.client.get('/api/')
