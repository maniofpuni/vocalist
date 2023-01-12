from django.db import models

# Create your models here.


class starmaker (models.Model):
    party= models.CharField(max_length=200)
    moment= models.CharField(max_length=200)
    chat=models.CharField(max_length=200)
    profile=models.CharField(max_length=200)


class profile (models.Model):
	name=models.CharField(max_length=200)
	image=models.CharField(max_length=200)
	gender=models.CharField(max_length=200)
	education=models.CharField(max_length=200)
	hometown=models.CharField(max_length=200)


class songs (models.Model):
	song_type=models.CharField(max_length=200)
	song_name=models.CharField(max_length=200)
	singer_name=models.CharField(max_length=200)
	music_director=models.CharField(max_length=200)

		