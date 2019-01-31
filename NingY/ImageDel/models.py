from django.db import models


# Create your models here.


class Img(models.Model):
    img_url = models.ImageField(upload_to='img')  # upload_to指定图片上传的途径，如果不存在则主动创建


class Imga(models.Model):
    img_desc = models.ImageField(max_length=200)  # 图片描述
    img_url = models.ImageField(upload_to='img')  # upload_to指定图片上传的途径，如果不存在则主动创建




class ImgSuper(models.Model):
    img_desc = models.ImageField(max_length=200)  # 图片描述
    img_url = models.ImageField(upload_to='img')  # upload_to指定图片上传的途径，如果不存在则主动创建
    img_score1 = models.CharField(max_length=30)
    img_root1 = models.CharField(max_length=30)
    img_keyword1 = models.CharField(max_length=30)

    img_score2 = models.CharField(max_length=30)
    img_root2 = models.CharField(max_length=30)
    img_keyword2 = models.CharField(max_length=30)

    img_score3 = models.CharField(max_length=30)
    img_root3 = models.CharField(max_length=30)
    img_keyword3 = models.CharField(max_length=30)

    img_score4 = models.CharField(max_length=30)
    img_root4 = models.CharField(max_length=30)
    img_keyword4 = models.CharField(max_length=30)

    img_score5 = models.CharField(max_length=30)
    img_root5 = models.CharField(max_length=30)
    img_keyword5 = models.CharField(max_length=30)

    img_keywords = models.CharField(max_length=200)
