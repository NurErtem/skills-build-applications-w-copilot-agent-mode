from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='marvel')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, 'marvel')

    def test_team_creation(self):
        team = Team.objects.create(name='marvel', members=['test@example.com'])
        self.assertEqual(team.name, 'marvel')
        self.assertIn('test@example.com', team.members)

    def test_activity_creation(self):
        activity = Activity.objects.create(user='test@example.com', activity='Running', duration=30)
        self.assertEqual(activity.user, 'test@example.com')
        self.assertEqual(activity.activity, 'Running')
        self.assertEqual(activity.duration, 30)

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user='test@example.com', points=100)
        self.assertEqual(lb.user, 'test@example.com')
        self.assertEqual(lb.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', difficulty='Easy')
        self.assertEqual(workout.name, 'Pushups')
        self.assertEqual(workout.difficulty, 'Easy')
