from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)


class Subcategory(models.Model):
    name = models.CharField(max_length=200)
    childOf = models.ForeignKey(Category)


class Question(models.Model):
    question_text = models.CharField(max_length=600)
    pub_date = models.DateTimeField('date published')
    subcategory = models.ForeignKey(Subcategory)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=600)
    true = models.IntegerField(default=1)
    info = models.TextField()


class Game(models.Model):
    start_date = models.DateTimeField('started on')
    round = 1

    def __init__(self, *args, **kwargs):
        super(Game, self).__init__(*args, **kwargs)
        self.round = self.round.all().aggregate(models.Max('round'))['round__max']


class QuestionsInGame(models.Model):
    game = models.ForeignKey(Game)
    question = models.ForeignKey(Question)
    round = models.IntegerField()

    class Meta:
        unique_together = ('game', 'question')


class Points(models.Model):
    question = models.ForeignKey(QuestionsInGame)
    player = models.ForeignKey(User)
    points = models.IntegerField()
