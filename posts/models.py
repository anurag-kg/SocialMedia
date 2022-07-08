from django.db import models
from django.urls import reverse
from django.conf import settings
import misaka
from groups.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    image = models.ImageField(upload_to='SocialMedia/photos',height_field=200, width_field=200,blank=True)
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name="posts", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','message']

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse('posts:single', kwargs={"username":self.user.username,'pk':self.pk})
