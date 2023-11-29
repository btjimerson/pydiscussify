# Generated by Django 4.2.7 on 2023-11-29 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=256, null=True)),
                ('post_date', models.DateTimeField(verbose_name='post_date')),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=256)),
                ('comment_date', models.DateTimeField(verbose_name='comment_date')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='discussify.post')),
            ],
            options={
                'ordering': ['-comment_date'],
            },
        ),
    ]