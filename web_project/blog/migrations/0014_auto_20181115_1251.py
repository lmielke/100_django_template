# Generated by Django 2.1.1 on 2018-11-15 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20181114_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='web_mode',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='post',
            name='web_mode',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='theme',
            name='web_mode',
            field=models.CharField(max_length=25),
        ),
    ]