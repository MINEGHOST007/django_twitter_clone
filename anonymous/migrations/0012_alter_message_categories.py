# Generated by Django 4.2.1 on 2023-06-16 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0011_alter_message_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='categories',
            field=models.CharField(choices=[('begining of an era', 'begining of an era'), ('entrepreneurship', 'entrepreneurship'), ('open source', 'open source'), ('relationship', 'relationship'), ('friends', 'friends'), ('news', 'news'), ('politics', 'politics'), ('religious', 'religious'), ('youtube', 'youtube'), ('Music', 'Music'), ('Gaming', 'Gaming'), ('Movies and TV Shows', 'Movies and TV Shows'), ('Food', 'Food'), ('none of the above', 'none of the above')], default='begining of an era', max_length=25),
        ),
    ]
