from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'



class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'




#임시로 파둠
class PopularSerializer(serializers.ModelSerializer):

    class Meta:
        model = Popular
        fields = '__all__'
