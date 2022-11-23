from rest_framework import serializers
from .models import *

# class ArticleSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Article
#         fields = '__all__'

# class CommentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Comment
#         fields = '__all__'

'''
'''
# 여기 아래부터 복붙임.
class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('id', 'title', 'content')
        # fields = ('id', 'title', 'content', 'user', 'username')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', )



# class PostImageSerializer(serializers.ModelSerializer):
#     image = serializers.ImageField(use_url=True)

#     class Meta:
#         model = PostImage
#         fields = ['image']


# class PostSerializer(serializers.ModelSerializer):
#     images = serializers.SerializerMethodField()

# 	#게시글에 등록된 이미지들 가지고 오기
#     def get_images(self, obj):
#         image = obj.image.all() 
#         return PostImageSerializer(instance=image, many=True, context=self.context).data

#     class Meta:
#         model = Post
#         fields = '__all__'

#     def create(self, validated_data):
#         instance = Post.objects.create(**validated_data)
#         image_set = self.context['request'].FILES
#         for image_data in image_set.getlist('image'):
#             PostImage.objects.create(post=instance, image=image_data)
#         return instance
