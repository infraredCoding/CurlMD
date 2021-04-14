from django.db import models


class WorkoutPlan(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    name = models.CharField(max_length=50, null=True)
    days = models.IntegerField(null=True)
    type = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)


class Workout(models.Model):
    plan = models.ForeignKey(WorkoutPlan, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    target = models.CharField(max_length=50, null=True)


class Sets(models.Model):
    exercise = models.CharField(max_length=100, null=True)
    workout = models.ForeignKey(Workout, null=True, on_delete=models.CASCADE)
    reps_or_time = models.IntegerField(null=True)
    sets = models.IntegerField(null=True)