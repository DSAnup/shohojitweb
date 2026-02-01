from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        # Get the CSRF token from the login page
        response_get = self.client.get("/login/")
        csrftoken = self.client.cookies.get('csrftoken')
        # Send the login request with the CSRF token
        response = self.client.post("/login/", {
            "username": "anup",
            "password": "Anup@2024",
            "csrfmiddlewaretoken": csrftoken
        }, headers={"X-CSRFToken": csrftoken})
        if response.status_code == 200:
            self.client.cookies = response_get.cookies
        else:
            print("Login failed")
    
    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def profile(self):
        self.client.get("/profile/")

    @task(3)
    def logout(self):
        self.client.get("/logout/")

    @task(4)
    def user_list(self):
        self.client.get("/user/")

    # @task(5)
    # def region_add(self):
    #     # Get the CSRF token from the login page
    #     response = self.client.get("/international_region/")
    #     csrftoken = response.cookies['csrftoken']  
    #     # Send the login request with the CSRF token
    #     response = self.client.post("/add/internationalregion/1/", {
    #         "international_region_name": "adminddd",
    #         "csrfmiddlewaretoken": csrftoken
    #     }, headers={"X-CSRFToken": csrftoken})

    #     if response.status_code == 200:
    #         print('ok')
    #     else:
    #         print("failed")
    #     self.interrupt()


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    # host = "http://127.0.0.1:8000"
    wait_time = between(1, 5)
