from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import User, Team, Activity, Workout, Leaderboard
from .serializers import (
    UserSerializer,
    TeamSerializer,
    ActivitySerializer,
    WorkoutSerializer,
    LeaderboardSerializer,
)


@method_decorator(csrf_exempt, name='dispatch')
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@method_decorator(csrf_exempt, name='dispatch')
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


@method_decorator(csrf_exempt, name='dispatch')
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


@method_decorator(csrf_exempt, name='dispatch')
class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


@method_decorator(csrf_exempt, name='dispatch')
class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    ordering = ['-score']  # Default ordering by score descending
