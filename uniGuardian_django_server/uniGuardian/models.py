from django.db import models


class UserProfile(models.Model):
    email = models.CharField(primary_key=True, max_length=155)
    createdAt = models.TimeField(auto_now_add=True)
    raw_resume = models.TextField(default='')
    raw_sop = models.TextField(default='')
    raw_lor1 = models.TextField(default='')
    raw_lor2 = models.TextField(default='')
    psychometrics = models.TextField(default='')
    analysis = models.TextField(default='')
    hightlight = models.TextField(default='')
    ai_detection_score = models.TextField(default='')
