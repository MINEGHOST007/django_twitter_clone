from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from datetime import datetime,date
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        # return reverse('detail_view', args=(str(self.id),))
        return reverse('home')

class Message(models.Model):
    title= models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    postdate = models.DateField(auto_now_add= True)
    categories = models.CharField(max_length=25,choices=Category.objects.all().values_list('name','name'),default="begining of an era")
    image = models.ImageField(upload_to="message/memories", default="",null=True,blank=True)
    like = models.ManyToManyField(User,related_name='blog_posts')
    book = models.ManyToManyField(User,related_name='blog_book')

    def __str__(self) -> str:
        return self.title+' | '+str(self.author)
    
    def get_absolute_url(self):
        # return reverse('detail_view', args=(str(self.id),))
        return reverse('home')
    
    def total_likes(self):
        return self.like.count()
    
choices = Category.objects.all()
choices_list = []

for item in choices:
    choices_list.append(item)

# bchoices = Message.objects.all().values_list('author', flat=True).distinct()
# bchoices_list = []
# for item in bchoices:
#     bchoices_list.append(item)

    
class Comment(models.Model):
    post = models.ForeignKey(Message,related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s - %s' % (self.post.title ,self.name )