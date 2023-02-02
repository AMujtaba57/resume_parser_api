import re

from django.http import JsonResponse

from rest_framework import status

"""
Cache the key available at https://{AUTH0_DOMAIN}/.well-known/jwks.json as a python dict
"""


class Auth0Middleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # GET TOKEN
        auth = request.headers.get("Authorization", None)
        regex = "/admin/"
        paths = re.search(regex, request.path)
        if request.path == "/production/" or paths or re.search("/summernote/", request.path)\
                or re.search("/static/", request.path):
            pass
        elif not auth:
            return JsonResponse(
                {"response_data": None, "message": "Unauthorized", "status": 401}, status=status.HTTP_401_UNAUTHORIZED
            )

        elif auth != "6251655368566D597133743677397A24":
            return JsonResponse(
                {"response_data": None, "message": "Unauthorized", "status": 401}, status=status.HTTP_401_UNAUTHORIZED
            )

        response = self.get_response(request)
        return response
