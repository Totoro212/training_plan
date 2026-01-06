from django.contrib import admin
from .models import TrainingDay, Exercise, DayExercise


class TrainingDayAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_filter = ['order']
    search_fields = ['title']

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

class DayExerciseAdmin(admin.ModelAdmin):
    list_display = ['training_day', 'exercise', 'sets', 'reps']
    search_fields = ['training_day', 'exercise']
    list_filter = ['training_day']

admin.site.register(TrainingDay, TrainingDayAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(DayExercise, DayExerciseAdmin)