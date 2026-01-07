from django.db import models

class Exercise(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Упражнения'


class DayExercise(models.Model):
    class WeekDay(models.IntegerChoices):
        MONDAY = 0, "Понедельник"
        TUESDAY = 1,"Вторник"
        WEDNESDAY = 2, "Среда"
        THURSDAY = 3, "Четверг"
        FRIDAY = 4, "Пятница"
        SATURDAY = 5, "Суббота"
        SUNDAY = 6, "Воскресенье"
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE
    )
    weekday = models.IntegerField(choices=WeekDay.choices, blank=True, null=True)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.exercise.title} — {self.reps}x{self.sets}"

    class Meta:
        verbose_name = 'День упражнения'
        verbose_name_plural = 'Дни упражнений'