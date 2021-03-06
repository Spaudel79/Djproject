# Generated by Django 3.0.1 on 2020-03-02 02:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_mainmenu_submenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCricket',
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
            name='BlogNBA',
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
            name='BlogTennis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField()),
                ('status', models.BooleanField(default=0)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(upload_to='blog')),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
