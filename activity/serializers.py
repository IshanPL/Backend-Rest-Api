from rest_framework import serializers
from .models import User, Activity


class UserSerializer(serializers.ModelSerializer):
    activities = serializers.SerializerMethodField()

    def get_activities(self, request):
        user_activity = Activity.objects.filter(user=request)
        return ActivitySerializer(user_activity, many=True).data

    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz', 'activities']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['start_time', 'end_time']



