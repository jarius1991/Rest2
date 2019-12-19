from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user import views


app_name = 'user'

# router = DefaultRouter()
# router.register('', views.CreateUserView, basename='')

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),  #  include(router.urls)),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me')
]
