from django.db import models

# Create your models here.
class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    # when we add image it will create a new dir and based on specified path it will create directry first time and upload this image to it
    photo = models.ImageField(upload_to='media/slider/%Y/')
    # auto_now_add true means whenever any object created/added then it will autometically add the current date and time in date time field
    created_date = models.DateTimeField(auto_now_add=True)
    
    # this is used for string representation of the slider object so that when we add some object in admin pannel then it will show the specific string that represent the object of this class instead of "slider object"
    # link = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.headline