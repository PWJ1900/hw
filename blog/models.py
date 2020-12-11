from django.db import models


# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.TextField()
    brief_content = models.TextField()
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)


class Peradminuse(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.TextField()
    password = models.TextField()
    name = models.TextField()


class index_slider(models.Model):
    slider_id = models.AutoField(primary_key=True)
    # slider_order_id = models.CharField(max_length=400)
    slider_image = models.CharField(max_length=400)
    slider_title = models.CharField(max_length=1000)
    slider_description = models.TextField()
    #
    # def __str__(self):
    #     return self.slider_title


class index_introduction(models.Model):
    introduction = models.TextField()


class index_people(models.Model):
    people_pic = models.CharField(max_length=400)
    tutor = models.TextField()
    tutor_en = models.TextField()


class Achievementss(models.Model):
    ID = models.AutoField(primary_key=True)
    orderID = models.IntegerField(null=True)
    paperinfo = models.TextField()
    pdf_link = models.CharField(max_length=1000)
    index = models.CharField(max_length=400, null=True)
    index_link = models.CharField(max_length=1000, null=True)
    index2 = models.CharField(max_length=400, null=True)
    index_link2 = models.CharField(max_length=1000, null=True)
    index3 = models.CharField(max_length=400, null=True)
    index_link3 = models.CharField(max_length=1000, null=True)


class Achievementss_project(models.Model):
    ID = models.AutoField(primary_key=True)
    orderID = models.IntegerField(null=True)
    projectname = models.TextField()
    projecturl = models.CharField(max_length=1000)
    direction = models.CharField(max_length=400, null=True)
    peoplenum = models.CharField(max_length=1000, null=True)


class people(models.Model):
    pic = models.CharField(max_length=400)
    name = models.CharField(max_length=400)
    identity = models.CharField(max_length=400)
    category = models.CharField(max_length=400)


class people_detail_simple(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400)
    identity = models.CharField(max_length=400)
    major = models.CharField(max_length=400)
    subject = models.CharField(max_length=400)
    description = models.TextField()


class people_education(models.Model):
    id = models.IntegerField(primary_key=True, max_length=100)
    time = models.CharField(max_length=400)
    education = models.CharField(max_length=400)
    university = models.CharField(max_length=400)
