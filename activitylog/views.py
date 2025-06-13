
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.core.cache import cache
from .models import UserActivityLog
from .serializers import UserActivityLogSerializer

CACHE_TTL = 60

class UserActivityLogCreateView(generics.CreateAPIView):
    queryset = UserActivityLog.objects.all()
    serializer_class = UserActivityLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        cache.delete(f"user_logs_{instance.user.id}")

class UserActivityLogListView(generics.ListAPIView):
    serializer_class = UserActivityLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        action = self.request.query_params.get('action')
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')
        cache_key = f"user_logs_{user_id}_{action}_{start}_{end}"
        cached_data = cache.get(cache_key)
        if cached_data:
            return cached_data
        queryset = UserActivityLog.objects.filter(user__id=user_id)
        if action:
            queryset = queryset.filter(action=action)
        if start and end:
            queryset = queryset.filter(timestamp__range=[start, end])
        cache.set(cache_key, queryset, CACHE_TTL)
        return queryset

class UserActivityLogPatchView(generics.UpdateAPIView):
    queryset = UserActivityLog.objects.all()
    serializer_class = UserActivityLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        log = self.get_object()
        new_status = request.data.get("status")
        if new_status not in dict(UserActivityLog.STATUS_CHOICES):
            return Response({"error": "Invalid status"}, status=400)
        log.status = new_status
        log.save()
        return Response(self.get_serializer(log).data)
