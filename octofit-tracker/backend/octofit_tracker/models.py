from djongo import models

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user_id = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user_id} - {self.type}"

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user_id = models.CharField(max_length=50)
    score = models.IntegerField()
    rank = models.IntegerField()
    def __str__(self):
        return f"{self.user_id} - Rank {self.rank}"
