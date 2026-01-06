from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import TrainingDay, Exercise,DayExercise
from django.db.models import Q

class IndexView(TemplateView):
    template_name = 'main/base.html'
