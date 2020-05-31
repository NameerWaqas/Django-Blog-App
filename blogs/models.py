from django.db import models

class ProgrammingModel(models.Model):
    title = models.CharField(max_length=200)
    header = models.TextField(default=None)
    section1 = models.TextField()
    gist1 = models.CharField(max_length=200,default=None)
    section2 = models.TextField()
    gist2 = models.CharField(max_length=200,default=None)
    section3 = models.TextField()
    gist3 = models.CharField(max_length=200,default=None)
    section4 = models.TextField()
    gist4 = models.CharField(max_length=200,default=None)
    footer = models.TextField(default=None)
    
    
    def __str__(self):
        return self.title
    
    
class DevelopmentModel(models.Model):
    title = models.CharField(max_length=200)
    header = models.TextField(default=None)
    section1 = models.TextField()
    gist1 = models.CharField(max_length=200,default=None)
    section2 = models.TextField()
    gist2 = models.CharField(max_length=200,default=None)
    section3 = models.TextField()
    gist3 = models.CharField(max_length=200,default=None)
    section4 = models.TextField()
    gist4 = models.CharField(max_length=200,default=None)
    footer = models.TextField(default=None)
    
    def __str__(self):
        return self.title

    
class MlModel(models.Model):
    title = models.CharField(max_length=200)
    header = models.TextField(default=None)
    section1 = models.TextField()
    gist1 = models.CharField(max_length=200,default=None)
    section2 = models.TextField()
    gist2 = models.CharField(max_length=200,default=None)
    section3 = models.TextField()
    gist3 = models.CharField(max_length=200,default=None)
    section4 = models.TextField()
    gist4 = models.CharField(max_length=200,default=None)
    footer = models.TextField(default=None)
    
    def __str__(self):
        return self.title
    
    
class DataScienceModel(models.Model):
    title = models.CharField(max_length=200)
    header = models.TextField(default=None)
    section1 = models.TextField()
    gist1 = models.CharField(max_length=200,default=None)
    section2 = models.TextField()
    gist2 = models.CharField(max_length=200,default=None)
    section3 = models.TextField()
    gist3 = models.CharField(max_length=200,default=None)
    section4 = models.TextField()
    gist4 = models.CharField(max_length=200,default=None)
    footer = models.TextField(default=None)
    
    def __str__(self):
        return self.title
# Create your models here.
