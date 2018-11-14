from django.db import models

# Create your models here.
class Game(models.Model):
    objects = models.Manager()
    CONSOLE_CHOICES = (
        ('PC','Personal Computer'),
        ('PS4','Play Station 4'),
        ('XB1','XBox One'),
    )
    GENRE_CHOICES =(
        ('act','Action'),
        ('adv','Adventure'),
        ('sp','Sports'),
        ('sho','Shooting'),
        ('mus','Musical'),
        ('fig','Fighting'),
        ('rac','Racing'),
    )
    AGRE_REST_CHOICES = (
        ('Ao','AdultsOnly'),
        ('M','Mature'),
        ('T','Teen'),
        ('E','Everyone'),
        ('eC','EarlyChildhood'),
    )
    console= models.CharField(
        max_length = 100,
        choices = CONSOLE_CHOICES,
        default = ''
    )
    genre = models.CharField(
        max_length = 100,
        choices = GENRE_CHOICES,
        default = ''
    )
    age_restriction = models.CharField(
        max_length = 100,
        choices = AGRE_REST_CHOICES,
        default = ''
    )
    game_image = models.ImageField(upload_to = 'images')
