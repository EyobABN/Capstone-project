from django.urls import path
from . import views
# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='home'),
    path('menu', views.MenuView.as_view(), name='menu'),
    path('menu/<int:pk>', views.MenuItemView.as_view(), name='menuitem'),
    path('booking', views.BookingView.as_view(), name='booking'),
    path('booking/<int:pk>', views.BookingItemView.as_view(), name='bookingitem'),
    # path('api-token-auth/', obtain_auth_token, name='auth'),
]
