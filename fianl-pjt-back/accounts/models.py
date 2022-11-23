from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    # username은 기본에 있음.
    nickname = models.CharField(max_length=15)
    sex = models.CharField(max_length=10)
    age = models.IntegerField(null=True)
    # user_image = models.CharField(null=True, blank=True) # charfield는 max_length있어야함.
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    # 프로필사진용 이미지 필드 추가
    image = models.ImageField(blank=True, upload_to='images/', max_length=100)
    image_select = models.CharField(max_length=10)

# class UserImg(User):

#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to="images/", blank=True)
