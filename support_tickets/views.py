from django.shortcuts import render
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Support
from .serializers import SupportSerializer
from recipe_book_api.permissions import IsOwnerOrReadOnly


class SupportList(APIView):
    serializer_class = SupportSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        support_ticket = Support.objects.all()
        serializer = SupportSerializer(
            support_ticket, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = SupportSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupportDetail(APIView):
    serializer_class = SupportSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            support_ticket = Support.objects.get(pk=pk)
            self.check_object_permissions(self.request, support_ticket)
            return support_ticket
        except Support.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        support_ticket = self.get_object(pk)
        serializer = SupportSerializer(
            support_ticket, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        support_ticket = self.get_object(pk)
        serializer = SupportSerializer(
            support_ticket, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        support_ticket = self.get_object(pk)
        support_ticket.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
