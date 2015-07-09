# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=600)),
                ('true', models.IntegerField(default=1)),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField(verbose_name=b'started on')),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField()),
                ('player', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=600)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionsInGame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('round', models.IntegerField()),
                ('game', models.ForeignKey(to='quiz.Game')),
                ('question', models.ForeignKey(to='quiz.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('childOf', models.ForeignKey(to='quiz.Category')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='subcategory',
            field=models.ForeignKey(to='quiz.Subcategory'),
        ),
        migrations.AddField(
            model_name='points',
            name='question',
            field=models.ForeignKey(to='quiz.QuestionsInGame'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='quiz.Question'),
        ),
        migrations.AlterUniqueTogether(
            name='questionsingame',
            unique_together=set([('game', 'question')]),
        ),
    ]
