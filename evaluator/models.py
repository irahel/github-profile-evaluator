from django.db import models

class Tracker(models.Model):
    name = models.CharField(max_length=25)
    clicks = models.IntegerField(default=0)

class Evaluation(models.Model):
    github_user = models.CharField(max_length=50)
    has_photo = models.BooleanField()
    has_email = models.BooleanField()
    has_linkedin = models.BooleanField()
    stacks = models.IntegerField()
    repositories = models.IntegerField()
    pinned_repositories = models.IntegerField()
    grade = models.IntegerField()

    def __str__(self):
        return f'{self.github_user}: {self.grade}/100'
