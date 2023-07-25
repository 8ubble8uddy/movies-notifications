from django.urls import path

from api.v1 import views

urlpatterns = [
    path('users_notifications/', views.UserNotificationCreate.as_view()),
    path('users_notifications/<uuid:pk>/', views.UserNotificationUpdate.as_view()),
    path('notifications/<uuid:pk>/users/', views.UsersListByNotification.as_view()),
]
