
from django.urls import path
from .views import UserActivityLogCreateView, UserActivityLogListView, UserActivityLogPatchView

urlpatterns = [
    path('logs/', UserActivityLogCreateView.as_view(), name='create-log'),
    path('logs/<int:user_id>/', UserActivityLogListView.as_view(), name='list-logs'),
    path('logs/update/<int:pk>/', UserActivityLogPatchView.as_view(), name='patch-log'),
]
