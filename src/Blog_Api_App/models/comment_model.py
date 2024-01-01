from .blog_model import Blog
from django.contrib.auth.models import User
from django.db import models

class Comment(models.Model):
    comment = models.TextField()
    
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, default=None , related_name = 'child_comments')
    
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.comment