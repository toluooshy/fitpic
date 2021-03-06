# Generated by Django 3.0.8 on 2020-07-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outfits', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothing',
            name='accessories',
        ),
        migrations.RemoveField(
            model_name='clothing',
            name='bottom',
        ),
        migrations.RemoveField(
            model_name='clothing',
            name='footgear',
        ),
        migrations.RemoveField(
            model_name='clothing',
            name='headgear',
        ),
        migrations.RemoveField(
            model_name='clothing',
            name='top',
        ),
        migrations.AddField(
            model_name='clothing',
            name='category',
            field=models.CharField(choices=[('TOPS', '(shirts, sweaters, jackets,...)'), ('BTTM', '(shorts, pants, skirts,...)'), ('FTGR', '(shoes, boots, sandals,...)'), ('HDGR', '(glasses, facial piercings,...)'), ('ACCS', '(jewelry, belts, watches,...)')], default='TOPS', max_length=4),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
