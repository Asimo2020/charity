from django.db import models
from django.contrib.auth.models import User
from django.conf import settings  
from django.db import models
from accounts.models import User

class TaskManager(models.Manager):  

    def related_tasks_to_charity(self, user):  
        return self.filter(charity__user=user)  

    def related_tasks_to_benefactor(self, user):  
        return self.filter(benefactor=user)  

    def all_related_tasks_to_user(self, user):  
        return self.filter(  
            models.Q(benefactor=user) |   
            models.Q(charity__user=user) |   
            models.Q(status='Pending')  
        )  
class Benefactor(models.Model):
    id = models.AutoField(primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    EXPERIENCE_CHOICES = [  
        (0, 'مبتدی'),  
        (1, 'متوسط'),     
        (2, 'متخصص'),     
    ]   
      
    experience = models.SmallIntegerField(  
        choices=EXPERIENCE_CHOICES,  
        default=0  
    )  
    free_time_per_week = models.PositiveSmallIntegerField(  
        default=0    
    )  

    def __str__(self):  
        return f"{self.user.username} - {self.get_experience_display()}"  

class Charity(models.Model):
    id = models.AutoField(primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)
    def __str__(self):  
        return f"{self.user.user}"  


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    assigned_benefactor = models.ForeignKey(Benefactor, on_delete=models.CASCADE, null=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE) 
    age_limit_from = models.IntegerField(blank=True,null=True)
    age_limit_to = models.IntegerField(blank=True,null=True)
    date = models.DateField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    gender_limit = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')],blank=True,null=True)
    STATUS_CHOICES = [  
        ('P', 'Pending'),  
        ('W', 'Waiting'),  
        ('A', 'Assigned'),  
        ('D', 'Done'),  
    ]  
    state = models.CharField(max_length=1,choices=STATUS_CHOICES,default='P',)  
    title = models.CharField(max_length= 60)
    def __str__(self):  
        return self.charity  