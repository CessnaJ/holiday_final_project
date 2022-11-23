from django.db import models
from django.conf import settings

# # Create your models here.
# class Article(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     # 얘는 article 테이블에 존재x(중개 테이블 생성- like users라는 테이블을 따로 만들어서 나가는데, field로 article/ auth_user_model 둘의 id를 M:N로 가져온다.)
#     like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     content = models.CharField(max_length=200)


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




# class Post(models.Model):
#     # id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=50)
#     content = models.TextField()
#     status = models.CharField(max_length=2)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     # board = models.ForeignKey(Board, on_delete=models.CASCADE)

#     def __int__(self):
#         return self.id

#     class Meta:
#         db_table = 'post'




# def image_upload_path(instance, filename):
#     return f'{instance.post.id}/{filename}'


# class PostImage(models.Model):
#     id = models.AutoField(primary_key=True)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='image')
#     image = models.ImageField(upload_to=image_upload_path)

#     def __int__(self):
#         return self.id

#     class Meta:
#         db_table = 'post_image'
