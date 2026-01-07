from django.contrib import admin
from .models import  Exercise, DayExercise

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

class DayExerciseAdmin(admin.ModelAdmin):
    list_display = ['weekday', 'exercise', 'sets', 'reps']
    search_fields = ['weekday', 'exercise']
    list_filter = ['weekday']

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(DayExercise, DayExerciseAdmin)