from django.db import models
from ckeditor.fields import RichTextField
from crispy_forms.helper import FormHelper

 
# Create your models here.

class MainMenu(models.Model):
    created_at = models.DateField()
    status = models.BooleanField(default=0)
    name = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='menu')
    description = RichTextField()

    def __str__(self):
        return self.title

class SubMenu(models.Model):
    created_at = models.DateField()
    main_menu=models.ForeignKey(MainMenu, on_delete=models.CASCADE)
    status = models.BooleanField(default=0)
    title = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    image = models.ImageField(blank=True, upload_to='menu')
    description = RichTextField()

    def __str__(self):
        return self.title



class Blog(models.Model):
    created_at = models.DateField()
    status = models.BooleanField(default=0)
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='blog')
    description = RichTextField()

    class Meta:
        verbose_name: 'blog newname'

    def __str__(self):
        return self.title

class BlogEPL(models.Model):
    title = models.OneToOneField(Blog,on_delete=models.CASCADE)


    class Meta:
        verbose_name: 'blog newname'

    def __str__(self):
        return self.title


class BlogSerieA(models.Model):
    title = models.OneToOneField(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)


    class Meta:
        verbose_name: 'blog newname'

    def __str__(self):
        return self.title


class BlogLaLiga(models.Model):
    title = models.OneToOneField(Blog, on_delete=models.CASCADE)

    class Meta:
        verbose_name: 'blog newname'

    def __str__(self):
        return self.title


class BlogChampionsLeague(models.Model):
    title = models.OneToOneField(Blog, on_delete=models.CASCADE)

    class Meta:
        verbose_name: 'blog newname'

    def __str__(self):
        return self.title

class BlogCricket(models.Model):
    created_at = models.DateField()
    status = models.BooleanField(default=0)
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='blog')
    description = RichTextField()

    class Meta:
        verbose_name: 'blog newname'

    def __str__(self):
        return self.title

class BlogNBA(models.Model):
    created_at = models.DateField()
    status = models.BooleanField(default=0)
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='blog')
    description = RichTextField()

    class Meta:
        verbose_name: 'blog newname'

    def __str__(self):
        return self.title


class BlogTennis(models.Model):
    created_at = models.DateField()
    status = models.BooleanField(default=0)
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='blog')
    description = RichTextField()

    class Meta:
        verbose_name: 'blog newname'

    def __str__(self):
        return self.title


class Club(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200, unique=True)

    # titel=(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Players(models.Model):
    club_name = models.OneToOneField(Club,on_delete=models.CASCADE)
    player_name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'players'

    def __str__(self):
        return self.player_name
