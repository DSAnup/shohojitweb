import requests
from django.shortcuts import render

class APICallMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        try:
            # Make the API call
            response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
            getUserId = response.json()

            if getUserId['userId'] != 1:
                return render(request, 'registration/license/licensecheck.html')
            
            response = self.get_response(request)
            return response
        except requests.exceptions.RequestException as e:
            # Print any error that occurs during the API call
            print("API Request failed:", e)


        