from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .serializers import *
from .models import *


class Register(APIView):
    def post(self, request):
        user_serializer = UserValidation(data=request.data)
        user_info = UserInfoValidation(data=request.data)
        if User.objects.filter(username=request.data['username']).exists():
            return Response(
                {'Message': "Username already exists!..."},
                status=status.HTTP_409_CONFLICT
            )
        if User.objects.filter(username=request.data['email']).exists():
            return Response(
                {'Message': "Email already exists!..."},
                status=status.HTTP_409_CONFLICT
            )
        if user_serializer.is_valid():
            if user_info.is_valid():
                user = user_serializer.save()
                user_info.save(user=user)
                return Response(
                    {"Message": "User created!..."},
                    status=status.HTTP_201_CREATED
                )
        return Response(
            {"Message": "Invalid data!..."},
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )


class CreatePassword(APIView):
    def post(self, request):
        if not User.objects.filter(username=request.data['prn']).exists():
            return Response(
                {"Message": "Invalid prn!..."},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        user = User.objects.filter(username=request.data['prn']).get()
        user.set_password(request.data['password'])
        user.is_active = True
        user.save()
        return Response(
            {"Message": "Password created!..."},
            status=status.HTTP_201_CREATED
        )


class Login(APIView):
    def post(self, request):
        user = User.objects.filter(email=request.data['email']).first()
        if not user:
            return Response(
                {"Message": "Username doesn't exists!..."},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        user = authenticate(username=user.username, password=request.data['password'])
        if user is None:
            return Response(
                {"Message": "Incorrect password!..."},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        auth_login(self.request, user)
        return Response(
            {"Message": "Login Successfully..."},
            status=status.HTTP_200_OK
        )


@method_decorator(csrf_exempt, name='dispatch')
class Logout(LoginRequiredMixin, APIView):
    def get(self, *args, **kwargs):
        auth_logout(self.request)
        return Response(
            {"Message": "Logout Successfully..."},
            status=status.HTTP_202_ACCEPTED
        )


class ProductView(APIView):
    def get(self, *args, **kwargs):
        product_id = self.kwargs['product_id']
        if Product.objects.filter(product_id=product_id).exists():
            return Response(
                {"Message": "Done..."},
                status=status.HTTP_200_OK
            )
        return Response(
            {"Message": "Invalid product Id!..."},
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )


class JoinMeet(APIView):
    def get(self, *args, **kwargs):
        meet = EmergencyCall.objects.filter(is_activated=False).first()
        if meet is not None:
            meet.is_activated = True
            meet.save()
            return Response(
                {"link": meet.link},
                status=status.HTTP_200_OK
            )
        meet = EmergencyCall.objects.first()
        return Response(
            {"link": meet.link},
            status=status.HTTP_200_OK
        )


@method_decorator(csrf_exempt, name='dispatch')
class Blood_Donation(LoginRequiredMixin, APIView):
    def post(self, *args, **kwargs):
        blood_donation_serializer = BloodDonationValidation(data=self.request.data)
        if blood_donation_serializer.is_valid():
            blood_donation_serializer.save(user=self.request.user)
        return redirect('/')
