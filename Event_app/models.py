from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class event(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_event')
    event_title = models.CharField(max_length=250,verbose_name="put a title")
    organizer = models.CharField(max_length=140,verbose_name="organization name",blank=True )
    slug = models.SlugField(max_length=250,unique=True)

    event_content = models.TextField(verbose_name="event detailes" )
    event_image = models.ImageField(upload_to='event_images', verbose_name="Image")
    publish_date = models.DateTimeField(auto_now_add=True)
    Start_date = models.DateField(" End_date(mm/dd/year)",blank=True, null=True)
    End_date = models.DateField(" End_date(mm/dd/year)",blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True)



    class Meta:
        ordering  =['-publish_date']


    def __str__(self):
        return self.event_title
class Comment(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE,related_name='event_comment')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return self.comment

class Like(models.Model):
    event = models.ForeignKey(event,on_delete=models.CASCADE, related_name='like_event')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='like_user')



# Create your models here.
