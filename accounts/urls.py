from django.urls import path
from .views import UserCreateAPIView, UserListAPIView, UserDetailAPIView, UserAPIView

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_list"),
    path("register", UserCreateAPIView.as_view(), name="user_create"),
    path("<int:id>", UserDetailAPIView.as_view(), name="user_detail")
]