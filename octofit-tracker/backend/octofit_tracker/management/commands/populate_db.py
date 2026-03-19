from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()

        # Delete existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        Team.objects.create(name='Team Marvel')
        Team.objects.create(name='Team DC')

        # Create users (superheroes)
        User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', first_name='Tony', last_name='Stark', team_name='Team Marvel')
        User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', first_name='Steve', last_name='Rogers', team_name='Team Marvel')
        User.objects.create_user(username='blackwidow', email='natasha@marvel.com', password='password', first_name='Natasha', last_name='Romanoff', team_name='Team Marvel')
        User.objects.create_user(username='batman', email='batman@dc.com', password='password', first_name='Bruce', last_name='Wayne', team_name='Team DC')
        User.objects.create_user(username='superman', email='superman@dc.com', password='password', first_name='Clark', last_name='Kent', team_name='Team DC')
        User.objects.create_user(username='wonderwoman', email='diana@dc.com', password='password', first_name='Diana', last_name='Prince', team_name='Team DC')

        # Create activities
        Activity.objects.create(username='ironman', activity_type='run', duration=30, calories=300)
        Activity.objects.create(username='captainamerica', activity_type='strength', duration=45, calories=500)
        Activity.objects.create(username='batman', activity_type='cycle', duration=60, calories=600)
        Activity.objects.create(username='superman', activity_type='flight training', duration=20, calories=200)
        Activity.objects.create(username='blackwidow', activity_type='martial arts', duration=50, calories=450)
        Activity.objects.create(username='wonderwoman', activity_type='combat training', duration=40, calories=400)

        # Create workouts
        Workout.objects.create(name='Morning Cardio', description='High intensity cardio to start the day')
        Workout.objects.create(name='Strength Training', description='Full body strength workout')
        Workout.objects.create(name='Combat Drills', description='Superhero combat training drills')

        # Create leaderboard
        Leaderboard.objects.create(username='captainamerica', score=1500)
        Leaderboard.objects.create(username='ironman', score=1400)
        Leaderboard.objects.create(username='batman', score=1300)
        Leaderboard.objects.create(username='wonderwoman', score=1200)
        Leaderboard.objects.create(username='blackwidow', score=1100)
        Leaderboard.objects.create(username='superman', score=1000)

        self.stdout.write(self.style.SUCCESS('Successfully populated octofit_db with superhero test data.'))
