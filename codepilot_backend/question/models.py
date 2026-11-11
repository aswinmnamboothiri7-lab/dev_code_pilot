from django.db import models
from account.models import User
from assessments.models import Assessment

# Create your models here.
class Question(models.Model):
    
    prompt = models.TextField()

    maximum_mark = models.PositiveIntegerField()

    display_order = models.PositiveIntegerField()


    assessment = models.ForeignKey(Assessment,on_delete=models.CASCADE,related_name='questions')

    PROGRAMMING_LANGUAGE_CHOICES = LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('java', 'Java'),
        ('c', 'C'),
        ('c++', 'C++'),
        ('javascript', 'JavaScript'),
    ]
    programming_language = models.CharField(max_length=100,choices=PROGRAMMING_LANGUAGE_CHOICES)

    created_at = models.DateTimeField(auto_now_add= True)

    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.prompt