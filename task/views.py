from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from task.serializers import TodoSerializer
from task.models import Todo


def index(request):
    return HttpResponse("Hello, world")


# Create your views here.


class ListTodoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateTodoAPIView(CreateAPIView):
    """This endpoint list all of the available todos from the database"""

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DeleteTodoAPIView(DestroyAPIView):
    """This endpoint list all of the available todos from the database"""

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UpdateTodoAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
