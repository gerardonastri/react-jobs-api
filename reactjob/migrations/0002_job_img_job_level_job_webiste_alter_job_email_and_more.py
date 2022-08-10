# Generated by Django 4.1 on 2022-08-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactjob', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='img',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='level',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='webiste',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='email',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='jobCategory',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='jobDesc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='jobTitle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='jobType',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='linkToJob',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
