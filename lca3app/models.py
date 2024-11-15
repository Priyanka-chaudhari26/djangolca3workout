from django.db import models

class Workoutmodel(models.Model):
    WORKOUT_TYPES = [
        ('Cardio', 'Cardio'),
        ('Strength', 'Strength'),
        ('Flexibility', 'Flexibility'),
        ('Balance', 'Balance'),
    ]
    workout_type = models.CharField(max_length=50, choices=WORKOUT_TYPES)
    
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    notes = models.TextField(blank=True, null=True)
    date = models.DateField()