from django.db.models import Count
from rest_framework import generics, permissions, filters
from recipe_book_api.permissions import IsOwnerOrReadOnly
from .models import Todo
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TodoSerializer


class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Todo.objects.all().order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__profile',
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TodoSerializer
    queryset = Todo.objects.all().order_by('-created_at')
