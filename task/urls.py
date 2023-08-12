from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("taskapi/", views.ListTodoAPIView.as_view(), name="taskapi"),
    path("taskapicreate/", views.CreateTodoAPIView.as_view(), name="taskapi"),
    path("taskapiupdate/<int:pk>/", views.UpdateTodoAPIView.as_view(), name="taskapi1"),
    path("taskapidelete/<int:pk>/", views.DeleteTodoAPIView.as_view(), name="taskapi1"),
]
