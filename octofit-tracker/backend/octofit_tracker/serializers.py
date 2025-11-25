from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class TeamSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)
    class Meta:
        model = Team
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)
    team = serializers.CharField(source='team._id', read_only=True)
    class Meta:
        model = User
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)
    user = serializers.CharField(source='user._id', read_only=True)
    class Meta:
        model = Activity
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)
    class Meta:
        model = Workout
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)
    class Meta:
        model = Leaderboard
        fields = '__all__'
