# Generated by Django 4.2.1 on 2023-06-16 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonymous', '0009_alter_message_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='categories',
            field=models.CharField(choices=[('begining of an era', 'begining of an era'), ('entrepreneurship', 'entrepreneurship'), ('open source', 'open source'), ('relationship', 'relationship'), ('friends', 'friends'), ('none of the above', 'none of the above')], default='begining of an era', max_length=25),
        ),
    ]
