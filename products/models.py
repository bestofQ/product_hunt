from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):

	title = models.CharField(default='例:抖音-用短视频记录没有生活', max_length=50)
	intro = models.TextField(default='在这里写APP介绍')
	url   = models.CharField(default='Http://', max_length=50)
	icon  = models.ImageField(default='default_icon.png', upload_to='images/')
	image = models.ImageField(default='default_image.png', upload_to='images/')

	

	# 投票
	votes = models.IntegerField(default=1)
	pub_date = models.DateTimeField()
	# 数据库知识 使用了外键 ForeignKey
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
    