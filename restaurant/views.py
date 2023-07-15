from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


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
    permission_classes = [IsAuthenticated]
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
    
    
class BookingViewSet(viewsets.ViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    
    def list(self, request):
        queryset = Booking.objects.all()
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})