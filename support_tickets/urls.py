from django.urls import path
from support_tickets import views

urlpatterns = [
    path('support_tickets/', views.SupportList.as_view()),
    path('support_tickets/<int:pk>/', views.SupportDetail.as_view())
]
