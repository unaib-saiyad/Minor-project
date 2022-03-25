from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserInfo, BloodDonation


class UserValidation(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserInfoValidation(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        exclude = ['user']

    def create(self, validated_data):
        return UserInfo.objects.create(**validated_data)


class BloodDonationValidation(serializers.ModelSerializer):
    class Meta:
        model = BloodDonation
        exclude = ['user']

    def create(self, validated_data):
        return BloodDonation.objects.create(**validated_data)