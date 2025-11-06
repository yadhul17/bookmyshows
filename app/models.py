from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    file  = models.FileField(upload_to='upload/',null=True, blank=True)
  # see next step






  
class Abouts(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    bg=models.FileField(upload_to='upload/',null=True,blank=True)
    description=models.CharField(max_length=300)
    
class Crew(models.Model):
    about=models.ForeignKey(Abouts,on_delete=models.CASCADE,null=True,blank=True)
    crew=models.FileField(upload_to='uploads/',null=True,blank=True)
    crewname=models.TextField()

class Cast(models.Model):
  about=models.ForeignKey(Abouts,on_delete=models.CASCADE,null=True,blank=True)
  cast=models.FileField(upload_to='upload/',null=True, blank=True)
  castname=models.TextField()




   

