import datetime
from django.shortcuts import render
from core.models import Exercise, DayExercise


def index(request):
    today = datetime.date.today().weekday()
    day_exercises = DayExercise.objects.filter(weekday=today)
    return render(request, 'index.html', {'day_exercises': day_exercises, 'today': today})
