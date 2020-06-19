# Generated by Django 3.0.1 on 2020-02-08 14:43

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField()),
                ('status', models.BooleanField(default=0)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(upload_to='blog')),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('address', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=200, unique=True)),
                ('club_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.Club')),
            ],
            options={
                'verbose_name_plural': 'players',
            },
        ),
    ]