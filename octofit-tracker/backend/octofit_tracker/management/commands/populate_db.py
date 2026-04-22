from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models


from django.conf import settings

from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Sample data
        users = [
            {"name": "Tony Stark", "email": "tony@marvel.com", "team": "marvel"},
            {"name": "Steve Rogers", "email": "steve@marvel.com", "team": "marvel"},
            {"name": "Bruce Wayne", "email": "bruce@dc.com", "team": "dc"},
            {"name": "Clark Kent", "email": "clark@dc.com", "team": "dc"},
        ]
        teams = [
            {"name": "marvel", "members": ["tony@marvel.com", "steve@marvel.com"]},
            {"name": "dc", "members": ["bruce@dc.com", "clark@dc.com"]},
        ]
        activities = [
            {"user": "tony@marvel.com", "activity": "Running", "duration": 30},
            {"user": "steve@marvel.com", "activity": "Cycling", "duration": 45},
            {"user": "bruce@dc.com", "activity": "Swimming", "duration": 60},
            {"user": "clark@dc.com", "activity": "Flying", "duration": 120},
        ]
        leaderboard = [
            {"user": "tony@marvel.com", "points": 100},
            {"user": "steve@marvel.com", "points": 90},
            {"user": "bruce@dc.com", "points": 110},
            {"user": "clark@dc.com", "points": 120},
        ]
        workouts = [
            {"name": "Pushups", "difficulty": "Easy"},
            {"name": "Pullups", "difficulty": "Medium"},
            {"name": "Squats", "difficulty": "Easy"},
            {"name": "Deadlift", "difficulty": "Hard"},
        ]

        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
