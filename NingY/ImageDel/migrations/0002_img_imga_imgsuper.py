# Generated by Django 2.1.3 on 2019-01-30 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ImageDel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Imga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_desc', models.ImageField(max_length=200, upload_to='')),
                ('img_url', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='ImgSuper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_desc', models.ImageField(max_length=200, upload_to='')),
                ('img_url', models.ImageField(upload_to='img')),
                ('img_score1', models.CharField(max_length=30)),
                ('img_root1', models.CharField(max_length=30)),
                ('img_keyword1', models.CharField(max_length=30)),
                ('img_score2', models.CharField(max_length=30)),
                ('img_root2', models.CharField(max_length=30)),
                ('img_keyword2', models.CharField(max_length=30)),
                ('img_score3', models.CharField(max_length=30)),
                ('img_root3', models.CharField(max_length=30)),
                ('img_keyword3', models.CharField(max_length=30)),
                ('img_score4', models.CharField(max_length=30)),
                ('img_root4', models.CharField(max_length=30)),
                ('img_keyword4', models.CharField(max_length=30)),
                ('img_score5', models.CharField(max_length=30)),
                ('img_root5', models.CharField(max_length=30)),
                ('img_keyword5', models.CharField(max_length=30)),
                ('img_keywords', models.CharField(max_length=200)),
            ],
        ),
    ]