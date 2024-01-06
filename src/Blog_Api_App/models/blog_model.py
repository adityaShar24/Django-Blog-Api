from django.db import models
from django.contrib.auth.models import User

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    
    author = models.CharField(max_length=100)
    
    content = models.CharField(max_length=500)
    
    date = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

