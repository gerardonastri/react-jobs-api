from pyexpat import model
from django.db import models

# Create your models here.


class Job(models.Model):
    email = models.CharField(max_length=60, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    jobTitle = models.CharField(max_length=50, blank=True, null=True)
    linkToJob = models.CharField(max_length=255, blank=True, null=True)
    jobType = models.CharField(max_length=50, blank=True, null=True)
    jobCategory = models.CharField(max_length=50, blank=True, null=True)
    jobDesc = models.TextField(blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)
    img = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.jobTitle


class User(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
