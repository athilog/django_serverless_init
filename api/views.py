from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

class UserAPIView(APIView):
    def get(self, request):
        return Response("login success")

# def index(request):
#     return Response("success")