from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
@api_view(["GET"])
def index(request) :
    return HttpResponse('Hello.')

@swagger_auto_schema(
    operation_description="Hello world!"
)
@action(detail=False, methods=['GET'], url_path="hello")
def hello_world(request):
    # return Response({"message": "Hello, world!"})
    return Response(status=200)
    pass