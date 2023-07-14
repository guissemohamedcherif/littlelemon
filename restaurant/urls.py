from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),

]
# urlpatterns =  router.urls
