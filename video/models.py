from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Categorie(models.Model):
	id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=255)
	color=models.CharField(max_length=10)
	timestamp = models.DateTimeField(auto_now_add=True)
	def natural_key(self):
		return u'%s  - %s' % (self.id)
	def __unicode__(self):
		return u'%s  - %s' % (self.id,self.name)

''' API Flickr '''
class Group(models.Model):
	id = models.AutoField(primary_key=True)
	group_id=models.CharField(max_length=20)
	name=models.CharField(max_length=150)
	description=models.CharField(max_length=500)
	timestamp = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return u'%s  - %s' % (self.id,self.name)

class Photo(models.Model):
	id = models.AutoField(primary_key=True)
	photo_id=models.CharField(max_length=20)
	owner=models.CharField(max_length=100)
	secret=models.CharField(max_length=20)
	server=models.CharField(max_length=10)
	farm=models.CharField(max_length=3)
	title=models.CharField(max_length=250)
	ownername=models.CharField(max_length=100)
	dateadded=models.CharField(max_length=50)
	group = models.ForeignKey(Group, related_name='u+')
	timestamp = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return u'%s  - %s' % (self.id,self.photo_id)

''' API Youtube '''
class Channel(models.Model):
	id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=255)
	channel=models.CharField(max_length=100)
	image=models.CharField(max_length=500)
	url=models.CharField(max_length=500)
	color=models.CharField(max_length=10)
	timestamp = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return u'%s  - %s' % (self.id,self.name)

class Video(models.Model):
	id = models.AutoField(primary_key=True)
	uuid=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
	name=models.CharField(max_length=255)
	description=models.TextField()
	url=models.CharField(max_length=255,unique=True)
	image=models.CharField(max_length=500)
	publishedAt= models.DateTimeField()
	timestamp = models.DateTimeField(auto_now_add=True)
	categorie = models.ManyToManyField(Categorie, related_name='u+')
	channel = models.ForeignKey(Channel, related_name='u+')
	def __unicode__(self):
		return u'%s  - %s' % (self.id,self.name)

class Like(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, related_name='u+')
	video = models.ForeignKey(Video, related_name='u+')
	type = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	def natural_key(self):
		return u'%s  - %s' % (self.video.name,self.user.name)
	def __unicode__(self):
		return u'%s  - %s' % (self.video.name,self.user.name)

	class Meta:
		unique_together = ('user', 'video')
