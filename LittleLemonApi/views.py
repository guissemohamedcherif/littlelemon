from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()

    def get(self, request, pk, format=None):
        try:
            item = MenuItem.objects.get(pk=pk)
            serializer = MenuItemSerializer(item)
            return Response(serializer.data)
        except MenuItem.DoesNotExist:
            return Response(status=404)

    def put(self, request, pk, format=None):
        try:
            item = MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response(status=404)
        serializer = MenuItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        try:
            item = MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get(self, request, format=None):
        items = MenuItem.objects.order_by('pk')
        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
