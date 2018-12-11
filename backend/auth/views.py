from rest_framework.views import APIView
from django.http import JsonResponse
import requests
from project.settings import API_BASE_URL, DJANGO_AUTH_FACEBOOK_CLIENT_ID, DJANGO_AUTH_FACEBOOK_CLIENT_SECRET


class convert(APIView):
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        access_token = request.data.get('token')
        return convert_token(access_token)


def convert_token(access_token):
    r = requests.post(API_BASE_URL + 'auth/social/convert-token/', json={"grant_type": "convert_token", "client_id": DJANGO_AUTH_FACEBOOK_CLIENT_ID,
                                                                 "client_secret": DJANGO_AUTH_FACEBOOK_CLIENT_SECRET, "backend": "facebook", "token": access_token})

    return JsonResponse(r.json(), status=200)