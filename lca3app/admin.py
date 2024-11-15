from django.contrib import admin
from .models import Workoutmodel

# Register your models here.


@admin.register(Workoutmodel)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'workout_type', 'duration', 'notes', 'date')