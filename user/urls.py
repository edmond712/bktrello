from django.urls import path

from user.views import UserList, UserDetails, UserCreate, UserDelete

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetails.as_view()),
    path('create/', UserCreate.as_view()),
    path('delete/<int:pk>/', UserDelete.as_view()),
]
