from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
class BookingViewSet(viewsets.ViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    
    def list(self, request):
        queryset = Booking.objects.all()
        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)