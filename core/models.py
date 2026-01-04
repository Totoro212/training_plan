from django.db import models

class Exercise(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class TrainingDay(models.Model):
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField()
    exercises = models.ManyToManyField(Exercise, through='DayExercise')
    def __str__(self):
        return self.title

class DayExercise(models.Model):
    training_day = models.ForeignKey(
        TrainingDay,
        on_delete=models.CASCADE,
        related_name='day_exercises'
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE
    )

    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.FloatField(null=True, blank=True)
    order = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.exercise.title} — {self.reps}x{self.sets}"