from django.urls import path
from todo import views

urlpatterns = [
    path('todo/', views.TodoList.as_view()),
    path('todo/<int:pk>/', views.TodoDetail.as_view())
]
