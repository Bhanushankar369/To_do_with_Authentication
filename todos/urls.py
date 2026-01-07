from django.urls import path

from .views import index, RegisterView, LoginView, TaskToDo, GetTasks

urlpatterns = [
    path('index/', index),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('task/', TaskToDo.as_view()),
    path('getTask/', GetTasks.as_view())
]
