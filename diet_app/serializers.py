from rest_framework  import serializers
from diet_app.models import *

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['id','username','email','password','phone']
        read_only_fields=['id']
    def create(self,validated__data):
        return CustomUser.objects.create_user(**validated__data)
    def get_profile(self,obj):
        profile_obj=UserProfile.objects.get(owner=obj)
        serializer_instance=UserProfileserializer(profile_obj)
        return serializer_instance.data

class UserProfileserializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields="__all__"
        read_only_fields=['id','bmr','owner']


class FoodLogserializer(serializers.ModelSerializer):
    class Meta:
        model=FooLog
        fields="__all__"
        read_only_fields=['owner','created_at']