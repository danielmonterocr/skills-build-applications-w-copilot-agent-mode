from djongo import models
from django.contrib.auth.models import AbstractUser


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'teams'


class User(AbstractUser):
    email = models.EmailField(unique=True)
    team_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'users'


class Activity(models.Model):
    username = models.CharField(max_length=150)
    activity_type = models.CharField(max_length=50)
    duration = models.FloatField()  # in minutes
    calories = models.FloatField()

    class Meta:
        db_table = 'activities'


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'workouts'


class Leaderboard(models.Model):
    username = models.CharField(max_length=150)
    score = models.FloatField()

    class Meta:
        db_table = 'leaderboard'
