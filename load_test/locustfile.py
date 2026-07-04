from threading import Lock

from locust import HttpUser, between, task

PRODUCT_ID = 1
TOTAL_REQUESTS = 10_000

counter = 0
lock = Lock()


class RegistrationUser(HttpUser):
    wait_time = between(0, 0)

    @task
    def register(self):
        global counter

        with lock:
            if counter >= TOTAL_REQUESTS:
                self.environment.runner.quit()
                return

            counter += 1

        with self.client.post(
            f"/products/{PRODUCT_ID}/registrations/",
            name="/products/:id/registrations/",
            catch_response=True,
        ) as response:
            if response.status_code == 201:
                response.success()

            elif response.status_code == 400:
                response.success()

            else:
                response.failure(f"Unexpected status code: {response.status_code}")
