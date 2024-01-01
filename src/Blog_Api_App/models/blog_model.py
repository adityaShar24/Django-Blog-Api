from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100)
    
    author = models.CharField(max_length=100)
    
    content = models.CharField(max_length=500)
    
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Blog' 

