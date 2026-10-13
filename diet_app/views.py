from django.shortcuts import render
from diet_app.serializers import *
from diet_app.models import *
from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView,ListAPIView,DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from diet_app.utility_func import calculate_bmr
from diet_app.permissions import IsOwner
# from django.contrib.auth.models backends
# Create your views here.

class SignUpView(CreateAPIView):
    serializer_class=Userserializer

class ProfileView(CreateAPIView):
    serializer_class=UserProfileserializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
       user_object=self.request.user
    #    data=serializer.validated_data
    #    bmr=calculate_bmr(
    #        age=data.get('age'),
    #        height=data.get('height'),
    #        weight=data.get("weight"),
    #        gender=data.get('gender'),
    #        activity_level=data.get('activity_level')

    #    )
       return serializer.save(owner=user_object)

class ProfileRetrieveView(RetrieveAPIView,UpdateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner]
    serializer_class=UserProfileserializer
    queryset=UserProfile.objects.all()

class UserRetrieveView(RetrieveAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner]
    serializer_class=Userserializer
    queryset=CustomUser.objects.all()

class FoodLogCreateView(CreateAPIView,ListAPIView,):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=FoodLogserializer
    queryset=FooLog.objects.all()

    def perform_create(self,serializer):
        return serializer.save(owner=self.request.user)
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class FoodLogRetrieveUpdateDistroy(RetrieveAPIView ,UpdateAPIView,DestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner]
    serializer_class=FoodLogserializer
    queryset=FooLog.objects.all()


