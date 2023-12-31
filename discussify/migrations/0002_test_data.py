# Generated by Django 4.2.7 on 2023-11-29 20:59

from django.db import migrations
from datetime import datetime, timezone, timedelta
from discussify.models import Post, Comment


def insert_test_data(apps, schema_editor):
    post = Post()
    post.author = "Jason Bourne"
    post.content = "Nuff said"
    post.title = "I'm a bad dude"
    post.post_date = datetime(2022, 11, 10, 18, 0, 0, 0, timezone(timedelta(hours=-5)))
    post.save()
    comment = Comment()
    comment.post = post
    comment.author = "Sally Struthers"
    comment.comment = "Yeah you are"
    comment.comment_date = datetime(2022, 11, 11, 12, 0, 2, 0, timezone(timedelta(hours=-5)))
    comment.save()

    post = Post()
    post.author = "Matt LaFleur"
    post.content = "I think my job is safe for another week"
    post.title = "I beat the Lions!"
    post.post_date = datetime(2023, 11, 27, 8, 10, 0, 0, timezone(timedelta(hours=-5)))
    post.save()
    comment = Comment()
    comment.post = post
    comment.author = "Dan Campbell"
    comment.comment = "I'm going to bite off your kneecaps"
    comment.comment_date = datetime(2023, 11, 27, 10, 15, 6, 0, timezone(timedelta(hours=-5)))
    comment.save()

    post = Post()
    post.author = "Brandon Staley"
    post.content = "I really don't understand the whole concept of how a clock tells time."
    post.title = "I need to learn how to tell time"
    post.post_date = datetime.now(timezone(timedelta(hours=-5)))
    post.save()

class Migration(migrations.Migration):

    dependencies = [
        ('discussify', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_test_data)
    ]

