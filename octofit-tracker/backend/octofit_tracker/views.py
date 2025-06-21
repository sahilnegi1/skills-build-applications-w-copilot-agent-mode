from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout

@api_view(['GET', 'POST'])
def api_root(request, format=None):
    if request.method == 'POST':
        return Response({"message": "POST request received"}, status=status.HTTP_201_CREATED)

    codespace_url = 'https://[automatic-cod-5jwgw4gg942vpxw]-8000.app.github.dev/'
    localhost_url = 'http://localhost:8000/'
    return Response({
        'users_codespace': codespace_url + 'api/users/?format=api',
        'teams_codespace': codespace_url + 'api/teams/?format=api',
        'activities_codespace': codespace_url + 'api/activities/?format=api',
        'leaderboard_codespace': codespace_url + 'api/leaderboard/?format=api',
        'workouts_codespace': codespace_url + 'api/workouts/?format=api',
        'users_localhost': localhost_url + 'api/users/?format=api',
        'teams_localhost': localhost_url + 'api/teams/?format=api',
        'activities_localhost': localhost_url + 'api/activities/?format=api',
        'leaderboard_localhost': localhost_url + 'api/leaderboard/?format=api',
        'workouts_localhost': localhost_url + 'api/workouts/?format=api',
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
