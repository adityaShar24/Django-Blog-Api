# Generated by Django 4.2.6 on 2024-01-01 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_Api_App', '0009_alter_blog_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
        migrations.AlterModelTable(
            name='blog',
            table='Blog',
        ),
    ]