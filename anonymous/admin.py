from django.contrib import admin

# Register your models here.
from .models import Message,Category , Comment

admin.site.register(Category)
admin.site.register(Message)
admin.site.register(Comment)
