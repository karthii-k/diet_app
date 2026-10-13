from django.db import models
from django.contrib.auth.models import AbstractUser 
from diet_app.utility_func import calculate_bmr
# Create your models here.

class CustomUser(AbstractUser):
    phone=models.CharField(max_length=15,unique=True)

class UserProfile(models.Model):
    age=models.PositiveIntegerField()
    weight=models.FloatField()
    height=models.PositiveIntegerField()
    GENDER_OPTIONS=(
        ('male','male'),
        ('female','female')
    )
    gender=models.CharField(max_length=20,choices=GENDER_OPTIONS,default='male')

    ACTIVITY_OPTIONS=(
    ('1.2','sedentary (little / no exercise)'),
    ('1.375','Lightly active (exercise 1 -3 days / week)'),
    ('1.55','Moderately active (exercise 3-5 days / week)'),
    ('1.725','Very active (exercise 6-7 days / week)'),
    ('1.9','Extra active (Very intense Activity)')

    )
    activity_level=models.CharField(max_length=200,choices=ACTIVITY_OPTIONS,default='1.2')
    bmr=models.CharField(null=True)
    owner=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='profile')

    def save(self,*args,**kwargs):
        self.bmr=calculate_bmr(self.age,self.weight,self.height,self.gender,float(self.activity_level))
        return super().save(*args,**kwargs)

class FooLog(models.Model):
    name=models.CharField(max_length=200,null=True)
    MEAL_TYPE_OPTIONS=(
        ('Breakfast','BreakFast'),
        ('Lunch','Lunch'),
        ('Snack','Snack'),
        ('Dinner','Dinner')
       
    )
    meal_type=models.CharField(max_length=100,choices=MEAL_TYPE_OPTIONS,null=True)

    calories=models.PositiveBigIntegerField(null=True)
    serving_size=models.CharField(max_length=100,null=True)
    notes=models.TextField(null=True)

    picture=models.ImageField(upload_to='FoodLogs',null=True)
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="Foodentries")