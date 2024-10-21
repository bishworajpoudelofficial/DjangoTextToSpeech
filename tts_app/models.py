from django.db import models

# Create your models here.
class TextFile(models.Model):
    text = models.TextField()
    file = models.FileField(upload_to='upload/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text